<template>
  <div class="component history-container">
    <div class="header">
      <!-- Chatbot header -->
      <a href="#" class="back" v-on:click.prevent="goBack">
        <i class="fas fa-chevron-circle-left"></i>
      </a>
      <div class="title">Search History</div>
      <router-link class="home-shortcut" :to="{ name: 'Dashboard' }">
          <i class="fas fa-bars"></i>
      </router-link>
    </div>

    <div class="history-main">

        <!-- New search -->
        <div class="new-search">
            <a class="new-search-btn" href="" v-on:click.prevent="createConversation">
                <span>New search</span>
                <i class="fas fa-comments"></i>
            </a>
        </div>

        <!-- List of chat histories -->
        <div v-if="conversations.length > 0" class="search-history">
            <div class="search-history-title">Past searches</div>
            <ul class="search-history-list">
                <li class="search-history-item" v-for="conversation in conversations" :key="conversation.id">
                    <div class="search-history-conversation-id">
                        <!-- <a href="" v-on:click.prevent="viewConversation(conversation)">ID: {{ conversation.id }}</a> -->
                        <span class="search-date">11/10/18</span>
                    </div>
                    <div class="search-history-tags">
                        <div v-if="conversation.suburbs" class="search-history-listing-tag">{{conversation.suburbs}}</div>
                        <div v-if="conversation.price_ent" class="search-history-listing-tag">{{getPrice(conversation.price_ent)}}</div>
                        <div v-if="conversation.accomodation" class="search-history-listing-tag">{{conversation.accomodation}}</div>
                        <div v-if="conversation.date" class="search-history-listing-tag">from {{getArrival(conversation.date)}}</div>
                        <div v-if="conversation.duration" class="search-history-listing-tag">{{getDuration(conversation.duration)}} nights</div>
                        <div v-if="conversation.accommondates" class="search-history-listing-tag">{{conversation.accommondates}} guests</div>
                        <div v-if="!conversation.suburbs &&
                                   !conversation.accomodation && 
                                   !conversation.price_ent && 
                                   !conversation.date &&
                                   !conversation.duration &&
                                   !conversation.accommondates " class="search-history-listing-empty">No preferences to display!</div>
                    </div>
                    <div class="search-history-item-nav">
                        <div class="search-history-item-search">
                            <a href="#" v-on:click.prevent="viewConversation(conversation.id)">Resume search</a>
                        </div>
                        <div class="search-history-item-results">
                            <a href="#" v-on:click.prevent="viewResults(conversation.id)">See results</a>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
        <div v-else class="empty-history">
            <p>Your search history is empty!</p>
            <p>Start a new conversation by clicking the button above</p>
        </div>

    </div>
  </div>
</template>

<script>
export default {
    name: 'ChatHistory',
    computed: {
        conversations() {
            return this.$store.state.chat.chat_history;
        }
    },
    methods: {
        isMobile(mq) {
            return mq === "sm";
        },
        createConversation() {
            console.log("Attempting to create conversation");
            this.$store.dispatch("createConversation");
            // Reroute the user to the chatbot view
            this.$router.push('/chat');
        },
        viewConversation(conversation_id) {
            console.log("Attempting to view chat history for conversation" + conversation_id);
            this.$store.dispatch("updateConversation", conversation_id);
            this.$store.dispatch("getMessages");
            // Reroute the user to the chatbot view
            this.$router.push('/chat');
        },
        viewResults(conversation_id) {
            console.log("Attempting to view search results for conversation" + conversation_id);
            this.$store.dispatch("updateConversation", conversation_id);
            this.$store.dispatch("getMessages");
            this.$store.dispatch("getSearchResults");
            // Reroute the user to the chatbot view
            this.$router.push('/results');
        },
        goBack() {
            this.$router.go(-1);
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
        }
  },
  beforeMount() {
    console.log("Attempting to view chat history");
    this.$store.dispatch("viewChatHistory");
  }
}
</script>

<style >
    /* Search history general styling */
    .history-main {
        width: 90%;
        display: block;
        margin: 0 auto;
    }
    /* New search button */
    .new-search {
        text-align: center;
        padding: 8px;
    }
    .new-search .new-search-btn {
        margin-top: 12px;
        display: inline-block;
        background-color: #ffffff;
        font-size: 1.5em;
        color: #000;
        border-radius: 3px;
        padding: 3px 15px;
        box-shadow: 0 7px 12px #ccc;
    }
    .new-search .new-search-btn > * {
        display: inline-block;
    }
    .new-search .new-search-btn > span {
        margin: 16px 6px 0 0;
        float: left;
        color: rgb(40, 197, 171);
    }
    .new-search .new-search-btn > i {
        color: white;
        background: rgb(40, 197, 171);
        font-size: 1.6em;
        padding: 9px;
        border-radius: 50%;
    }
    /* Search history */
    .search-history {
        margin-top: 25px;
    }
    .search-history-title {
        color: rgb(121, 120, 120);
        font-size: 1.2em;
    }
    .search-history .search-history-list {
        list-style: none;
        padding: none;
    }
    .search-history-item {
        margin: 10px auto;
        background-color: #fff;
        padding: 8px;
        box-shadow: 2px 2px 8px #ccc;
    }
    .search-date {
        float: right;
        color: rgb(109, 108, 108);
        font-size: 0.8em;
    }
    .search-history-tags {
        clear: both;
        overflow: auto;
        padding-bottom: 10px;
        border-bottom: 1px solid #ccc;
    }
    .search-history-tags .search-history-listing-tag {
        float: left;
        background-color: rgb(40, 197, 171);
        color: white;
        margin: 2px 6px;
        padding: 4px 10px;
        font-size: 0.8em;
        border-radius: 15px;
    }
    /* Search history item nav */
    .search-history-item-nav {
        padding: 12px 6px 6px 6px;
    }
    .search-history-item-nav > * {
        display: inline-block;
        width: 40%;
        margin: 0 3%;
        text-align: center;
        padding: 8px;
        border-radius: 4px;
        font-size: 0.9em;
        cursor: pointer;
    }
    .search-history-item-nav > * > a {
        color: white;
    }
    .search-history-item-search {
        background-color: rgb(21, 141, 221);
    }
    .search-history-item-results {
        background-color: coral;
    }
    /* Empty search history message */
    .empty-history {
        margin-top: 50px;
        font-family: Arial;
        color: #868d99;
        text-align: center;
        font-size: 1.5em;
    }
    .search-history-listing-empty {
        padding: 10px;
        color: rgb(145, 145, 145);
    }


</style>
