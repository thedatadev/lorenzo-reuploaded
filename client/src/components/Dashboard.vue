<template>
    <div class="component dashboard-main">

        <!-- New search -->
        <a href="" v-on:click.prevent="createConversation" class="start-new-search-btn">
            <img class='dashboard-lorenzo-face' src="../assets/lorenzo-faces/face1.png" alt="">  
            <div class='dashboard-lorenzo-greet' >
                <div><strong class="click-here-prompt">Click here</strong> to start chatting, {{user()}}</div>
                <i class="fas fa-arrow-right"></i>
            </div>         
        </a>

        <!-- Dashboard portal -->
        <div class="dashboard-portal">
            <!-- Search / search history -->
            <router-link :to="{ name: 'SearchHistory' }">
                <i class="fas fa-search portal-btn-icon"></i>            
                <span class="portal-btn-title">History</span>
                <p class="portal-btn-description">
                    Start a new search and monitor your search history
                </p>
            </router-link>
            <!-- Bookings -->
            <router-link :to="{ name: 'BookingHistory' }">
                <i class="fas fa-home portal-btn-icon"></i>
                <span class="portal-btn-title">Bookings</span>
                <p class="portal-btn-description">
                    View and manage your bookings
                </p>
            </router-link>
            <!-- Advertising -->
            <router-link :to="{ name: 'AdvertiseHistory' }">
                <i class="fas fa-dollar-sign portal-btn-icon"></i>
                <span class="portal-btn-title">Advertise</span>
                <p class="portal-btn-description">
                    Advertise and manage your listings
                </p>
            </router-link>
            <!-- Account settings -->
            <router-link :to="{name: 'Account'}">
                <i class="fas fa-user-cog portal-btn-icon"></i>
                <span class="portal-btn-title">Account</span>
                <p class="portal-btn-description">
                    View and manage your personal account
                </p>
            </router-link>

        </div>
        
    </div>
</template>

<script>
export default {
    name: 'Dashboard',
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
    user() {
        return this.$store.state.user.name;
    }
  }
}
</script>

<style>
    .component {
        margin: 0;
    }
    .dashboard-main {
        background-image: linear-gradient(rgba(0, 0, 0, 0.527)), url(../assets/sydney-blurry.png);
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        padding-top: 20px;
    }
    .dashboard-portal {
        width: 90%;
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .dashboard-portal > a {
        flex: 1 30%;
        margin: 10px;
        height: 150px;
        text-decoration: none;
        background-color: white;
        padding: 12px 20px;
        font-family: Arial;
        color: #000;
        border-radius: 6px;
        box-shadow: 0 1px 7px rgba(0, 0, 0, 0.527);
        text-align: center;
    }
    .start-new-search-btn {
        display: block;
        margin: 0 auto 20px auto;
        width: 85%;
        padding: 10px;
        font-size: 1.3em;
        color: white;
        background-color: rgb(39, 218, 188);
        border-radius: 6px;
        box-shadow: 0 1px 7px rgba(0, 0, 0, 0.527);
    }
    .dashboard-portal > a {
        display: flex;
        flex-direction: column;
    }
    .dashboard-portal > a .portal-btn-icon {
        font-size: 1.9em;
        color: rgb(39, 218, 188);
    }
    .dashboard-portal > a .portal-btn-title {
        padding-top: 20px;
        color: rgba(0, 0, 0, 0.747);
        font-weight: 500;
    }
    .dashboard-portal > a .portal-btn-description {
        margin-top: 5px;
        padding-top: 15px;
        border-top: 1px solid #ccc;
        font-size: 0.8em;
        color: rgba(0, 0, 0, 0.507);
    }
    .dashboard-lorenzo-face {
        width: 90px;
        height: 90px;
        border-radius: 50%;
    }
    .dashboard-lorenzo-greet {
        width: 60%;
        float: right;
        /* padding: 16px 0 0 12px; */
    }
    .dashboard-lorenzo-greet > i {
        float: right;
        margin: 4px 12px 0 0;
        font-size: 1.6em;
    }
    /* .click-here-prompt {

    } */
    
</style>

