<template>
  <!-- Main container -->
    <div class="component chat-container">
    <!-- Header -->
    <div class="header">
        <!-- Chat header -->
        <a href="#" class="back" v-on:click.prevent="goBack">
          <i class="fas fa-chevron-circle-left"></i>
        </a>
        <div class="title">Chat</div>
    </div>

    <!-- Main chat -->
    <div class="chat-main">

        <!-- Parameters -->
        <div class="chat-parameters">
        <!-- Param list -->
          <ul v-if="Object.keys(params).length > 0" class="param-list">

              <!-- Param template -->
              <li v-if="params.suburbs" class="param">
                  <i class="param-name fas fa-map-marked-alt"></i>
                  <span v-if="!editMode" class="param-value">{{params.suburbs}}</span>
                  <span v-else class="param-value param-edit" contenteditable="true" ref="editSuburb">{{params.suburbs}}</span>
              </li>

              <li v-if="params.accommondates" class="param">
                  <i class="param-name fas fa-users"></i>
                  <span v-if="!editMode" class="param-value">{{params.accommondates}} guests</span>
                  <span v-else class="param-value">
                    <span class="param-edit" contenteditable="true" ref="editAccommodates">{{params.accommondates}}</span>
                    <span> guests</span>
                  </span>
              </li>

              <li v-if="params.date" class="param">
                  <i class="param-name far fa-calendar-times"></i>
                  <span v-if="!editMode" class="param-value">from {{getArrival(params.date)}}</span>
                  <span v-else>
                    <span>from </span>
                    <span class="param-value param-edit" contenteditable="true" ref="editDay">{{renderDate('day')}}</span>
                    <span>/</span>
                    <span class="param-value param-edit" contenteditable="true" ref="editMonth">{{renderDate('month')}}</span>
                    <span>/</span>
                    <span class="param-value param-edit" contenteditable="true" ref="editYear">{{renderDate('year')}}</span>
                  </span>
              </li>

              <li v-if="params.duration" class="param">
                  <i class="param-name fas fa-hourglass-half"></i>
                  <span v-if="!editMode" class="param-value">{{getDuration(params.duration)}} nights</span>
                  <span v-else class="param-value">
                    <span contenteditable="true" ref="editDuration" class="param-edit">{{getDuration(params.duration)}}</span>
                    <span> nights</span>
                  </span>
              </li>

              <li v-if="params.accomodation" class="param">
                  <i class="param-name fas fa-home"></i>
                  <span v-if="!editMode" class="param-value">{{params.accomodation}}</span>
                  <span v-else class="param-value param-edit" contenteditable="true" ref="editAccommodation">{{params.accomodation}}</span>
              </li>

              <li v-if="params.price_ent" class="param">
                  <i class="param-name fas fa-dollar-sign"></i>
                  <span v-if="!editMode" class="param-value">{{getPrice(params.price_ent)}}</span>
                  <span v-else class="param-value">{{getPrice(params.price_ent)}}</span>
              </li>


          </ul> <!-- END Param list -->
          <div v-else class="empty-notif">
            You can view and edit search filters here
          </div>

          <!-- Params options -->
          <div class="params-options">

              <!-- See results -->
              <router-link v-if="!editMode" :to="{name: 'Results'}" class="see-results">
                <span>See results</span>
                <i class="fas fa-map-marker-alt"></i>
              </router-link>

              <a v-else href="#" id="params-save-button" v-on:click.prevent="saveParams">
                <span>Save</span>
              </a>


              <!-- Update params -->
              <a href="#" id="params-edit-btn" v-on:click.prevent="toggleEdit">
                <span v-if="!editMode">
                  Edit
                  <i class="far fa-edit"></i>
                </span>
                <span v-else>Cancel</span>
              </a>

              

          </div> <!-- END Params options -->

        </div> <!-- END Parameters -->


        <!-- Chat messages -->
        <div class="chat-chatbot">

        <!-- Chathead -->
        <div class="chathead">
            <img class="chathead-img" src='../assets/lorenzo-faces/face1.png' alt="">
        </div>  <!-- END Chathead -->

        <!-- Chatbot message -->
        <div class="chatbot-message">
            <p>{{chatbotMessage}}</p>
        </div><!-- END Chatbot message -->

        </div> <!-- END Chat messages -->

        <!-- Chat bar -->
        <div class="chat-bar">
        <!-- User input -->
        <form class="chatbot-input-form" @submit.prevent="addNewMessage">
          <input autocomplete="off" class="chat-bar-input" type="text" name="" value="" placeholder="Enter reply..." v-model="newUserMessage">
        </form>
        <!-- Send button -->
        <a class="chat-bar-btn" href="#" @click.prevent="addNewMessage">
            <i class="fas fa-location-arrow"></i>
        </a>
        </div>  <!-- END Chat bar -->


    </div> <!-- END Main chat  -->
    </div> <!-- END Main container -->
</template>

<script>

export default {
  name: "Chat",
  data() {
    return {
      newUserMessage: '',
      editMode: false
    };
  },
  computed: {
    messages() {
      return this.$store.state.chat.messages;
    },
    chatbotMessage() {
      return this.$store.state.chat.chatbot_response;
    },
    params() {
      return this.$store.state.chat.params;
    },
    addNewMessage() {
      if (this.newUserMessage) {
        this.$store.dispatch('addNewMessage', this.newUserMessage);
        this.newUserMessage = '';
      }
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    toggleEdit() {
      this.editMode = !this.editMode;
    },
    saveParams() {
      this.editMode = false;

      console.log("Saving the following params:");
      console.log("Suburb: " + this.$refs.editSuburb.innerText);
      console.log("Guests: " + this.$refs.editAccommodates.innerText);
      console.log("Date: " + this.$refs.editDay.innerText + '/' + this.$refs.editMonth.innerText + '/' + this.$refs.editYear.innerText);
      console.log("Duration: " + this.$refs.editDuration.innerText);
      console.log("Accommodation: " + this.$refs.editAccommodation.innerText);

      let editParams = {}
      //  Add suburb
      if (this.$refs.editSuburb) {
        editParams['suburbs'] = this.$refs.editSuburb.innerText;
      }
      // Add guests
      if (this.$refs.editAccommodates) {
        editParams['accommondates'] = parseInt(this.$refs.editAccommodates.innerText);
      }
      // Add accommodation
      if (this.$refs.editAccommodation) {
        editParams['accomodation'] = this.$refs.editAccommodation.innerText;        
      }
      // Add date
      if (this.$refs.editDay && this.$refs.editMonth && this.$refs.editYear) {
        let currentDate = new Date(this.$store.state.chat.params.date);
        currentDate.setDate(this.$refs.editDay.innerText);
        currentDate.setMonth(parseInt(this.$refs.editMonth.innerText) - 1);
        currentDate.setFullYear(this.$refs.editYear.innerText);
        editParams['date'] = currentDate.toISOString().slice(0, 11) + "12:00:00+11:00";
      }
      // Add duration
      if (this.$refs.editDuration) {
        console.log("Duration is specified");
        let amount = parseInt(this.$refs.editDuration.innerText);
        const duration = {
          amount: amount,
          unit: 'day'
        }
        editParams['duration'] = duration;
      }

      console.log(editParams);

      this.$store.dispatch('saveUpdatedParams', editParams);


    },
    getArrival(arrivalDate) {
      const date = new Date(arrivalDate);
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();
      return day + '/' + month + '/' + year; 
    },
    getDuration(duration) {
      let durationAmnt = duration.amount;
      const durationUnit = duration.unit;

      if (durationUnit === "wk") {
        durationAmnt = durationAmnt * 7;
      } else if (durationUnit === "mo") {
        durationAmnt = durationAmnt * 28
      }

      return durationAmnt;
    },
    getPrice(price) {
        if (typeof(price) === 'string') {
            return price;
        } else {
            if (price.length === 1) {
                return price[0];
            } else {
                let first = price[0];
                let second = price[1];
                first = first.slice(0, first.indexOf("AUD"));
                second = second.slice(0, second.indexOf("AUD"));
                first = parseInt(first, 10);
                second = parseInt(second, 10);
                const range = Math.min(first, second) + " to " + Math.max(first, second) + " AUD per night"
                return range;
            }
        }
    },
    renderDate(mode) {

      let dateString = this.$store.state.chat.params.date;
      const date = new Date(dateString);
      const day = date.getDate();
      const month = date.getMonth() + 1;
      const year = date.getFullYear();

      if (mode === 'day') {
        return day;
      } else if (mode === 'month') {
        return month;
      } else { // mode === year
        return year;
      }
    }
  }
};
</script>

<style >
/* See results button */
.see-results {
  background-color: tomato;
}
#params-save-button {
  background-color: tomato;
}
/* Chat main */
.chat-main {
  background-color: rgb(249, 245, 245);
  display: flex;
  flex-direction: column;
  height: 93vh;
}
/* Chat parameters */
.chat-parameters {
  flex: 5;
  display: flex;
  flex-direction: column;
  box-shadow: 0 0 8px rgb(203, 209, 214);
  margin: 10px;
  background-color: white;
  position: relative;
}
.chat-parameters .param-list {
  flex: 9;
  padding: 20px;
  list-style-type: none;
}
.chat-parameters .param-list .param {
  background-color: white;
  margin: 2.5px;
  border-radius: 4px;
  font-family: Arial;
  float: left;
  padding: 2px 7px;
  box-shadow: 0 4px 8px #ccc;
}
.chat-parameters .param-list .param > * {
  display: inline-block;
}
.chat-parameters .param-list .param .param-name {
  font-weight: bold;
  font-size: 1.0em;
  background-color: rgb(90, 196, 180);
  border-radius: 75px;
  color: white;
  padding: 0.5em 0.6em;
}
.chat-parameters .param-list .param .param-value {
  padding: 10px 10px 10px 0;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}
.param-edit {
  font-weight: bold;
  color: tomato;
}
.empty-notif {
  text-align: center;
  color: rgb(151, 151, 151);
  padding-top: 50px;
}
/* Params options */ 
.chat-parameters .params-options {
  flex: 2;
  padding-bottom: 10px;
  position: absolute;
  bottom: 0;
  right: 0;
}
.chat-parameters .params-options > a {
  float: right;
  margin-right: 10px;
  padding: 10px;
  border-radius: 4px;
  color: white;
}
.chat-parameters .params-options #params-edit-btn {
  color: rgb(40, 197, 171);
  background-color: white;
  border: 2px solid rgb(224, 219, 219);
}
/* Chatbot message */
.chat-chatbot {
  flex: 3;
  display: flex;
  flex-direction: row;
}
.chat-chatbot .chathead {
  flex: 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 1%;
}
.chat-chatbot .chathead .chathead-img {
  height: 15vh;
  width: 15vh;
  border-radius: 50%;
  background-color: black;
  box-shadow: 0 12px 22px #ccc;
}
.chat-chatbot .chatbot-message {
  flex: 8;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 1%;
}
.chat-chatbot .chatbot-message > p {
  padding: 10px;
  background-color: rgb(67, 137, 228);
  margin-right: 10px;
  border-radius: 6px;
  color: white;
  box-shadow: 0 4px 9px rgb(180, 191, 198);
}
/* Chat bar */
.chat-bar {
  flex: 1;
  width: 100%;
}
.chat-bar  > * {
  float: left;
}
.chatbot-input-form {
  width: 80%;
}
.chat-bar-input {
  width: 100%;
  border-style: none;
  font-size: 1.3em;
  padding: 10px;
  height: 100%;
}
.chat-bar-input:focus {
  outline: none;
}
.chat-bar-btn {
  background-color: white;
  width: 20%;
  font-size: 2.4em;
  color: rgb(20, 214, 214);
  text-align: center;
}
</style>
