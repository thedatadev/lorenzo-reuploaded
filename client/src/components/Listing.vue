<template>
    <div class="component full-listing">
        <!-- listing main -->
        <div  v-if="listing != null" class="component listing-main">

        <!-- picture -->
        <div class="listing-picture" :style="{ backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.97) 95%), url(' + listing.picture_url + ')' }">
            <!-- picture nav -->
            <div class="picture-nav">
            <a href="#" v-on:click.prevent="goBack" class="listing-back">
                <i class="fas fa-arrow-left"></i>
            </a>
            <!-- <router-link :to="{ name: 'Results' }" class="listing-back">
                <i class="fas fa-arrow-left"></i>
            </router-link> -->
            <a href="#" class="view-photos" @click.prevent="unimplementedNotification">View photos</a>
            </div>
            <!-- picture gap -->
            <div class="picture-gap"></div>
            <!-- title -->
            <div class="listing-title">
            <!-- room type -->
            <p class="listing-title-type">
                <span>{{listing.room_type}}</span>
                <span> in </span>
                <span>{{listing.property_type}}</span>
            </p>
            <!-- listing name -->
            <p :class="{'listing-title-name': true, 'short-title': isShort(listing.name), 'medium-title': isMed(listing.name), 'long-title': isLong(listing.name) }">{{listing.name}}</p>
            </div>
        </div>

        <!-- main info -->
        <div class="listing-main-info">
            <div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Guests</p>
                <p class="listing-main-info-content-value">{{ listing.accommodates }}</p>
            </div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Min nights</p>
                <p class="listing-main-info-content-value">{{ listing.minimum_nights }}</p>
            </div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Max nights</p>
                <p class="listing-main-info-content-value">{{ listing.maximum_nights }}</p>
            </div>
            </div>
            <div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Bathrooms</p>
                <p class="listing-main-info-content-value">{{ listing.bathrooms }}</p>
            </div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Bedrooms</p>
                <p class="listing-main-info-content-value">{{ listing.bedrooms }}</p>
            </div>
            <div class="listing-main-info-content">
                <p class="listing-main-info-content-label">Beds</p>
                <p class="listing-main-info-content-value">{{ listing.beds }}</p>
            </div>
            </div>
        </div>

        <!-- tabs -->
        <div class="listing-main-tabs">
            <!-- Description -->
            <router-link :to="{ name: 'Description' }"  class="listing-tab">
                <p>Description</p>
                <i class="fas fa-chevron-circle-right"></i>
            </router-link>
            
            <!-- Neighbourhood (with map) & transit -->
            <router-link :to="{ name: 'Neighbourhood' }"  class="listing-tab">
                <p>Neighbourhood</p>
              <i class="fas fa-chevron-circle-right"></i>
            </router-link>
            <!-- Amenities -->
            <router-link :to="{ name: 'Amenities' }"  class="listing-tab">
              <p>Amenities</p>
              <i class="fas fa-chevron-circle-right"></i>
            </router-link>
            <!-- House rules -->
            <router-link :to="{ name: 'HouseRules' }"  class="listing-tab">
              <p>House Rules</p>
              <i class="fas fa-chevron-circle-right"></i>
            </router-link>

        </div>

        <!-- Calendar -->
        <Calendar />

        <!-- Similar listings -->
        <div class="listing-main-similar">
            <a href="#" v-on:click.prevent="getSimilarListings">View similar listings</a>
        </div>

        <!-- Booking link (fixed) -->
        <div class="listing-main-book">
            <div class="listing-price">${{ listing.price }} per night</div>
            <div class="listing-booking-btn">
            <router-link :to="{ name: 'MakeBooking' }">Make a booking</router-link>
            </div>
        </div>

        </div>
        <div v-else>
                There is NO active listing!
        </div>

    </div>
</template>

<script>
import Calendar from "@/components/Calendar";

export default {
    name: "Listing",
    components: {
      Calendar
    },
    computed: {
        listing() {
            return this.$store.state.listings.active_listing;
        }
    },
    methods: {
        goBack() {
          this.$router.go(-1);
        },
        isShort(name) {
            return name.length <= 30;
        },
        isMed(name) {
            return 30 < name.length && name.length <= 60;;
        },
        isLong(name) {
            return name.length > 60;
        },
        getSimilarListings() {
          this.$store.dispatch('getRecommendations');
        },
        unimplementedNotification() {
          alert("Sorry, the photo album has not been implemented.");
        }
    },
    beforeMount() {
      this.$nextTick(function () {
        console.log("Attempting a fetch request for listing " + this.$route.params.listing_id);
        this.$store.dispatch("getListing", this.$route.params.listing_id);
      });
    }
}
</script>

<style>

/* Listing main general */
.listing-main {
  position: relative;
}
/* Picture */
.listing-picture {
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 300px;
}
.listing-picture .picture-nav {
  height: 20%;
}
.listing-picture .picture-gap {
  height: 60%;
}
.listing-picture .picture-nav .listing-back {
  color: rgb(64, 218, 167);
  height: 40px;
  width: 40px;
  background-color: white;
  font-size: 1.4em;
  padding: 10px;
  border-radius: 50%;
  margin: 12px 0 0 10px;
  display: inline-block;
}
.listing-picture .picture-nav .view-photos {
  float: right;
  background-color: white;
  padding: 8px;
  border-radius: 4px;
  box-shadow: 0 1px 5px rgba(96, 95, 95, 0.77);
  color: black;
  margin: 12px 10px 0 0;
}
.listing-picture .listing-title {
  height: 20%;
  padding: 6px;
}
.listing-picture .listing-title .listing-title-type {
  color: rgb(64, 218, 167);
}
.listing-picture .listing-title .listing-title-name {
  color: white;
}
.short-title {
    font-size: 1.5em;
}
.medium-title {
    font-size: 1.0em;
}
.long-title {
    font-size: 0.6em;
}
/* Main listing info */
.listing-main-info {
  margin-top: 20px;
  padding: 10px;
}
.listing-main-info > div {
  margin-bottom: 10px;
}
.listing-main-info > div > .listing-main-info-content {
  display: inline-block;
  width: 32%;
  margin: 0 auto;
}
.listing-main-info > div > .listing-main-info-content > p {
  display: inline-block;
  color: rgb(112, 107, 107);
}
.listing-main-info > div > .listing-main-info-content > .listing-main-info-content-value {
  float: right;
  margin-right: 12px;
  font-weight: bold;
  color: rgb(61, 189, 147);
}
.listing-main-info > div > .listing-main-info-content > .listing-main-info-content-label {
  font-size: 0.8em;
}

/* Booking bar */
.listing-main .listing-main-book {
  position: fixed;
  bottom: 0;
  left: 0;
  background-color: white;
  z-index: 100;
  width: 100%;
  height: 10vh;
}
.listing-main .listing-main-book > * {
  display: inline-block;
}
.listing-main .listing-main-book > .listing-price {
  color: rgb(243, 65, 104);
  font-weight: bold;
  font-size: 1.4em;
  margin: 18px 0 0 30px;
}
.listing-main .listing-main-book > .listing-booking-btn {
  float: right;
  background-color: rgb(61, 218, 114);
  background-image: linear-gradient(rgb(61, 218, 114), rgba(26, 200, 85, 0.88) 90%);
  box-shadow: 0 2px 6px rgb(173, 173, 173);
  padding: 10px;
  border-radius: 6px;
  margin: 10px 5px 0 0;
}
.listing-main .listing-main-book > .listing-booking-btn > a{
  color: white;
}
/* Tabs */
.listing-main-tabs {
  width: 95%;
  margin: 0 auto
}
.listing-main-tabs > .listing-tab {
  display: block;
  padding: 10px;
  background-color: rgb(249, 249, 249);
  margin: 10px 0;
  cursor: pointer;
}
.listing-main-tabs > .listing-tab > * {
  display: inline-block;
  font-size: 1.7em;
  color: rgb(71, 66, 66);
}
.listing-main-tabs > .listing-tab > *:nth-child(2) {
  color: rgb(64, 218, 167);
  float: right;
  margin-right: 20px;
  font-size: 2.0em;
}
/* Similar listings */
.listing-main-similar {
  margin-top: 20px;
  margin-bottom: 100px;
  width: 100%;
}
.listing-main-similar > a {
  width: 80%;
  display: block;
  margin: 10px auto;
  background-color: white;
  color: rgb(36, 205, 165);
  text-align: center;
  padding: 12px;
  font-size: 1.4em;
  border-radius: 4px;
  box-shadow: 0 3px 8px rgba(168, 168, 168, 0.82);
}

</style>
