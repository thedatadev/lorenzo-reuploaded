import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import router from '../router'

Vue.use(Vuex)

/*
                    Vuex store description

1) Database (state)

The Vuex store acts as a central database to store all data 
fetched from the API. This is more convenient than localising
data in separate components and having to pass data around from
component to component.

2) HTTP services (actions and mutations)

Each request made to the API is made from the Vuex store. Whenever
data is required by a component, it calls an action in this file
which then fires a HTTP request to the API for the required data,
updates state it required (through mutations) and then re-routes
to another page if required.

*/

const API_URL = "http://127.0.0.1:5000/";


export const store = new Vuex.Store({
    plugins: [createPersistedState()],
    state: {
        user: {
            name: "Guest"
        },
        chat: {
            chatbot_response: "Hi there!",
            params: {},
            active_conversation: null,
            chat_history: [],
            messages: []
        },
        listings: {
            active_listing: null,
            results: [],
            recommendations: [],
            full_calendar: [[[]]],
            active_calendar: [[]],
            active_calendar_month: 0,
            base_month: 9,
            months: ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"],
            active_month: "January"
        },
        bookings: {
          history: []
        },
        advertise: {
          history: []
        }
    },
    getters: {
      // No getters required for this client
    },
    mutations: {
        updateUserName: (state, payload) => {
          state.user.name = payload;
        },
        addNewMessage: (state, payload) => {
            state.chat.messages.push(payload);
        },
        displaySearchResults: (state, payload) => {
            state.listings.results = payload;
        },
        updateMessages: (state, payload) => {
            state.chat.messages = payload;
        },
        updateConversationID: (state, payload) => {
            state.chat.active_conversation = payload;
        },
        updateChatHistory: (state, payload) => {
            state.chat.chat_history = payload;
        },
        updateActiveListing: (state, payload) => {
            state.listings.active_listing = payload;
        },
        updateChatbotResponse: (state, payload) => {
            state.chat.chatbot_response = payload;
        },
        updateChatParams: (state, payload) => {
            state.chat.params = payload;
        },
        updateBookingHistory: (state, payload) => {
            state.bookings.history = payload;
        },
        updateAdvertiseHistory: (state, payload) => {
            state.advertise.history = payload;
        },
        displayRecommendations: (state, payload) => {
            state.listings.recommendations = payload;
        },
        updateCalendar: (state, payload) => {
            state.listings.full_calendar = payload.calendar;
            state.listings.base_month= payload.base_month;
            state.listings.active_month = state.listings.months[state.listings.base_month]
        },
        updateCalendarMonth: (state, payload) => {
            state.listings.active_calendar_month = state.listings.active_calendar_month + payload;
            state.listings.active_calendar = state.listings.full_calendar[state.listings.active_calendar_month];
            state.listings.active_month = state.listings.months[(state.listings.base_month + state.listings.active_calendar_month) % 12]
        }
    },
    actions: {
        updateUserName: (context, payload) => {
          context.commit('updateUserName', payload);
        },
        addNewMessage: (context, payload) => {

          console.log("Adding a new message for conversation: " + context.state.chat.active_conversation);

          // Group together message data
          let newUserMessage = {
            content: payload,
            isChatbot: false,
            conversation_id: context.state.chat.active_conversation
          };
                
          // New message endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/message";
  
          // Instantiate the request object
          const request = new Request(API_ENDPOINT, {
            method: 'POST',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            }),
            body: JSON.stringify(newUserMessage)
          });

          // Send the new message to the new message endpoint
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              console.log("Token expried. Login is required");
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          .then(function(response_payload) {

            console.log("Received the following response after sending new message:");
            console.log(response_payload);
            
            const chatbot_response = response_payload.chatbot_response;
            const params = response_payload.params;

            context.commit('updateChatbotResponse', chatbot_response);
            context.commit('updateChatParams', params);
  
          })
          .catch(err => {
            console.log(err)
          });
        },
        getSearchResults: context => {
            // Makes a GET request to the localhost endpoint for the top 10 listings
      
            // API endpoint to get search results
            const API_ENDPOINT = "http://127.0.0.1:5000/search/" + context.state.chat.active_conversation;
      
            const request = new Request(API_ENDPOINT, {
              method: 'GET',
              headers: new Headers({
                "Content-Type": "application/json",
                "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
              })
            });
      
            // Send request payload to API_ENDPOINT via HTTP request
            fetch(request)
            .then(function(response) {
              if (response.status === 200) {
                return response.json();
              } else if (response.status === 401) {
                router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
              } else {
                throw new Error(response.statusText);
              }
            })
            .then(function(payload) {
      
              // NOTE: No status code error checking is currently done.
              //       i.e. assume all responses are 200 OK
      
              // Update the list of search results
              context.commit('displaySearchResults', payload.listings);
              
            })
            .catch(err => {
              console.log(err);
            });
        },
        createConversation: context => {
          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/conversation";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'POST',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {
              // Extract the token and store it in the conversations list
              const conversation_id = data.conversation_id;
              console.log("Created a new conversation with ID: " + conversation_id);
              // Set the user's current conversation to the new conversation
              context.commit('updateConversationID', conversation_id);
              // context.commit('updateMessages', []); // clear messages for new conversation
              context.commit('updateChatbotResponse', 'Hi there!');
              context.commit('updateChatParams', {});
          })
          .catch(function(error) {
              console.log(error);
          });
        },
        viewChatHistory: context => {
          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/chathistory";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {
              // Extract the token and store it in the conversations list
              const chat_histories = data.chat_histories;
              context.commit('updateChatHistory', chat_histories);
          })
          .catch(function(error) {
              console.log(error);
          });
        },
        getMessages: context => {
          // Makes a GET request for all messages of particular conversation
          const API_ENDPOINT = "http://127.0.0.1:5000/chatparams/" + context.state.chat.active_conversation;
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send request payload to API_ENDPOINT via HTTP request
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          .then(function(response_payload) {

            const chatbot_response = response_payload.chatbot_response;
            const params = response_payload.params;

            context.commit('updateChatbotResponse', chatbot_response);
            context.commit('updateChatParams', params);
            
          })
          .catch(err => {
            console.log(err);
          });

        },
        updateConversation: (context, payload) => {
          context.commit('updateConversationID', payload);
        },
        getListing: (context, payload) => {
          // Makes a GET request to the localhost endpoint for the top 5 listings
      
          const API_ENDPOINT = "http://127.0.0.1:5000/listings/" + payload;
      
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
    
          // Send request payload to API_ENDPOINT via HTTP request
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          .then(function(payload) {
    
            // Update the list of search results
            context.commit('updateActiveListing', payload.listing);
            
          })
          .catch(err => {
            console.log(err);
          });
        },
        editParams: context => {
          console.log("Upating params");
          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/conversation/" + context.state.chat.active_conversation + "/parameters";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'PUT',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            }),
            body: context.state.chat.params
          });
          // Send the fetch request
          console.log("Sending fetch request");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            const updatedParams = data.params;
            context.commit('updateChatParams', updatedParams);

          })
          .catch(function(error) {
              console.log(error);
          });
        },
        makeBooking: (context, payload) => {
          console.log("Making booking");

          const start_date = payload.start_date;
          const num_nights = payload.num_nights;
          const listing_id = payload.listing_id;

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/listings/" + listing_id + "/bookings";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'POST',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            }),
            body: JSON.stringify({ start_date: start_date, num_nights: num_nights })
          });
          // Send the fetch request
          console.log("Sending fetch request to make new booking");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return '';
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            console.log("Booking was made!");
            router.push({name: 'BookingHistory', params: {successfulBooking: true}});

          })
          .catch(function(error) {
              console.log(error);
          });
        },
        getBookingHistory: context => {
          console.log("Getting user's booking history");

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/user/bookings";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request to get booking history");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            console.log("Booking history retrieved!");
            context.commit('updateBookingHistory', data.bookings);

          })
          .catch(function(error) {
              console.log(error);
          });
        },
        newListing: (context, payload) => {
          console.log("Posting a new listing");

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/listing";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'POST',
            headers: new Headers({
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            }),
            body: payload
          });
          // Send the fetch request
          console.log("Sending fetch request to post a new listing");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return { status: 200, message: "New listing was posted!" };
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else if (response.status === 404) {
              return { status: 404, message: "New listing could NOT be posted" };
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(msg) {

            console.log(msg);
            router.push({ name: 'AdvertiseHistory', params: { flash: { status: msg.status, message: msg.message } }});

          })
          .catch(function(error) {
              console.log(error);
          });
        },
        getAdvertiseHistory: context => {
          console.log("Getting user's advertising history");

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/listings/advertise";
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request to get advertise history");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            console.log("Advertise history retrieved!");
            context.commit('updateAdvertiseHistory', data.listings);

          })
          .catch(function(error) {
              console.log(error);
          });   
        },
        getRecommendations: context => {
          console.log("Getting recommendations for listing: " + context.state.listings.active_listing.id);

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/listing_recommendations/" + context.state.listings.active_listing.id;
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request to get recommendations for listing: " + context.state.listings.active_listing.id);
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            console.log("Listing recommendations retrieved!");
            context.commit('displayRecommendations', data.listings);
            router.push('/recommendations');

          })
          .catch(function(error) {
              console.log(error);
          });  
        },
        saveUpdatedParams: (context, payload) => {
          console.log("Updating preference params for conversation: " + context.state.chat.active_conversation);

          // Create conversation endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/chatparams/" + context.state.chat.active_conversation;
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'PUT',
            headers: new Headers({
              "Content-Type": "application/json",
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            }),
            body: JSON.stringify(payload)
          });
          // Send the fetch request
          console.log("Sending fetch request to get recommendations for conversation: " + context.state.chat.active_conversation);
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            console.log("Saved updated params!");
            context.commit('updateChatParams', data.params);

          })
          .catch(function(error) {
              console.log(error);
          }); 
        },
        getCalendar: context => {
          // Calendar endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/available_dates/" + context.state.listings.active_listing.id;
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'GET',
            headers: new Headers({
              "AUTH_TOKEN": localStorage.getItem('lorenzo-token')
            })
          });
          // Send the fetch request
          console.log("Sending fetch request for calendar");
          fetch(request)
          .then(function(response) {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              router.push({ name: 'Login', params: { message: 'Your token has expired. Please log in to continue' }});
            } else {
              throw new Error(response.statusText);
            }
          })
          // Handle successful creation
          .then(function(data) {

            context.commit('updateCalendar', data);

          })
          .catch(function(error) {
              console.log(error);
          });
        },
        updateCalendarMonth: (context, payload) => {
          context.commit("updateCalendarMonth", payload);
        }
        
    }
})