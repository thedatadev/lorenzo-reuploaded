import Vue from "vue";
import Router from "vue-router";
import Chat from "@/components/Chat";
import Results from "@/components/Results";
import Register from "@/components/Register";
import Login from "@/components/Login";
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
import AdvertiseHistory from "@/components/AdvertiseHistory";
import UpdateAdvertise from "@/components/UpdateAdvertise";
import Description from "@/components/Description";
import Neighbourhood from "@/components/Neighbourhood";
import Amenities from "@/components/Amenities";
import HouseRules from "@/components/HouseRules";
import Recommendations from "@/components/Recommendations";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Homepage",
      component: Homepage
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: Dashboard
    },
    {
      path: "/register",
      name: "Register",
      component: Register
    },
    {
      path: "/login",
      name: "Login",
      component: Login
    },
    {
      path: "/chat",
      name: "Chat",
      component: Chat
    },
    {
      path: "/results",
      name: "Results",
      component: Results
    },
    {
      path: "/history",
      name: "SearchHistory",
      component: SearchHistory
    },
    {
      path: "/listing",
      name: "Listing",
      component: Listing
    },
    {
      path: "/account",
      name: "Account",
      component: Account
    },
    {
      path: "/newAdvertise",
      name: "NewAdvertise",
      component: NewAdvertise
    },
    {
      path: "/bookingHistory",
      name: "BookingHistory",
      component: BookingHistory
    },
    {
      path: "/booking",
      name: "Booking",
      component: Booking
    },
    {
      path: "/confirmation",
      name: "Confirmation",
      component: Confirmation
    },
    {
      path: "/makeBooking",
      name: "MakeBooking",
      component: MakeBooking
    },
    {
      path: "/advertiseHistory",
      name: "AdvertiseHistory",
      component: AdvertiseHistory
    },
    {
      path: "/updateAdvertise",
      name: "UpdateAdvertise",
      component: UpdateAdvertise
    },
    {
      path: "/description",
      name: "Description",
      component: Description
    },
    {
      path: "/neighbourhood",
      name: "Neighbourhood",
      component: Neighbourhood
    },
    {
      path: "/amenities",
      name: "Amenities",
      component: Amenities
    },
    {
      path: "/houseRules",
      name: "HouseRules",
      component: HouseRules
    },
    {
      path: "/recommendations",
      name: "Recommendations",
      component: Recommendations
    }
    
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
});
