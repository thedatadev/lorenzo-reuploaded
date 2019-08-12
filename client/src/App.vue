<template>
  <div class="container">
      <router-view/>
  </div>
</template>

<script>
import Results from "@/components/Results";
import Chat from "@/components/Chat";
import Dashboard from "@/components/Dashboard";
import Homepage from "@/components/Homepage";
import SearchHistory from "@/components/SearchHistory";
import Listing from "@/components/Listing";
import Account from "@/components/Account";
import NewAdvertise from "@/components/NewAdvertise";
import BookingHistory from "@/components/BookingHistory";
import Booking from "@/components/Booking";
import Confirmation from "@/components/Confirmation";
import MakeBooking from "@/components/MakeBooking";
import Calendar from "@/components/Calendar";
import AdvertiseHistory from "@/components/AdvertiseHistory";
import UpdateAdvertise from "@/components/UpdateAdvertise";
import Description from "@/components/Description";
import Neighbourhood from "@/components/Neighbourhood";
import Amenities from "@/components/Amenities";
import HouseRules from "@/components/HouseRules";
import Recommendations from "@/components/Recommendations";



export default {
  name: "App",
  components: {
    Results,
    Chat,
    Dashboard,
    Homepage,
    SearchHistory,
    Listing,
    Account,
    NewAdvertise,
    BookingHistory,
    Booking,
    Confirmation,
    MakeBooking,
    Calendar,
    AdvertiseHistory,
    UpdateAdvertise,
    Description,
    Neighbourhood,
    Amenities,
    HouseRules,
    Recommendations
  },
  data() {
    return {
      // authenticated: true
    };
  },
  methods: {
    isMobile(mq) {
      return mq === "sm";
    }
  }
};
</script>

<style>
/* General styling */
* {
  margin: 0;
  padding: 0;
  list-style: none;
  text-decoration: none;
  font-family: Arial;
  box-sizing: border-box;
}
#app, .container {
  height: 100vh;
}
/* Both mobile & desktop styling */

/* Component general styling */
.component {
  height: 100vh;
}
.component .header {
  background-color: white;
  border-bottom: 1px solid #ccc;
  color: rgb(48, 45, 45);
  height: 7vh;
  display: flex;
  min-height: 50px;
}
.component .content {
  height: 93vh;
}
/* Component header styling */
.component .header .title {
  flex: 10;
  text-align: center;
  font-family: Arial;
  font-weight: 100;
  letter-spacing: 1.2px;
  margin-top: 12px;
}
.component .header .back {
  margin-left: 10px;
  font-size: 1.9em;
  color: rgb(40, 197, 171);
  font-family: Arial;
  font-weight: 100;
}
.home-shortcut {
  color: black;
  margin: 10px 10px 0 0;
  font-size: 1.6em;
}
 /* homepage header styling */
  .lorenzo-header-container {
      text-align: center;
      margin-bottom: 50px;
      font-family: Arial;
  }
  /* Regstration logo styling */
  .lorenzo-header-logo {
      font-size: 2.2em;
  }
  .lorenzo-header-logo > a {
      text-decoration: none;
      color: black;
  }
  .lorenzo-header-logo .bnb {
      font-family: 'Gloria Hallelujah', cursive;
      margin-left: 8px;
      color: coral;
  }
  /* homepage slogan styling */
  .lorenzo-header-slogan {
      margin-top: 15px;
  }
  .lorenzo-header-slogan .slogan {
      letter-spacing: 2px;
  }
  .lorenzo-header-slogan .fa-map-marker-alt {
      color: coral;
  }

/* Desktop-only styling */ 
@media(min-width:768px) {
  /* Container styling */
  .container {
    display: flex;
  }
  /* Component general styling */
  .chatbot-main {
    flex: 3
  }
  .results-main {
    flex: 5
  }
}

/* Mobile-only styling */
@media(max-width:767px) {
 
  /* Component header styling */
  .component .header .button {
    flex: 2;
    border-style: none;
    background-color: transparent;
  }
  .component .header .button .fas {
    font-size: 2.2em;
    color: white;
  }
  .component .header .button:focus {
    outline: none;
  }
  .component .header .button:hover {
    cursor: pointer;
  }

}
</style>
