<template>
<!-- Advertise main -->
    <div class="component advertise-history-main">

      <!-- Header -->
      <div class="header">
        <a href="#" class="back" v-on:click.prevent="goBack">
            <i class="fas fa-arrow-circle-left"></i>
        </a>
        <div class="title">Advertise History</div>
        <router-link class="home-shortcut" :to="{ name: 'Dashboard' }">
            <i class="fas fa-bars"></i>
        </router-link>
      </div>

      <!-- Post new listing -->
      <router-link class="advertise-new-btn" :to="{ name: 'NewAdvertise' }">Post new listing</router-link>

      <!-- Flash message to user after API response -->
      <div v-if="this.$route.params.flash" class="flash-message">
        <div :class="{ 'advertise-flash': true, 'status-ok': this.$route.params.flash.status === 200 }">
          {{ this.$route.params.flash.message  }}
        </div>

      </div>

      <!-- Advertise content -->
      <div class="advertise-history-content">

        <!-- Advertise history item -->
        <div class="advertise-history-item" v-for="listing in listings" :key="listing.id">
          <div class="advertise-history-title">
            <div class="advertise-history-type">{{listing.room_type}} in {{listing.property_type}}</div>
            <div class="advertise-history-location">
              <i class="fas fa-map-marker-alt"></i>
              <span>{{listing.neighbourhood}}</span>
            </div>
          </div>
          <div class="advertise-history-summary">

            <div class="advertise-history-info">
              <i class="fas fa-users"></i>
              <span>{{listing.accommodates}} guests</span>
            </div>

            <div class="advertise-history-info">
              <i class="fas fa-bed"></i>
              <span>{{listing.beds}} beds</span>
            </div>

            <div class="advertise-history-info">
              <i class="fas fa-dollar-sign"></i>
              <span>{{listing.price}} per night</span>
            </div>

          </div>
          <!-- Nav -->
          <div class="advertise-history-nav">
            <div class="advertise-history-delete-nav" @click.prevent="unimplementedNotification">Delete listing</div>
            <router-link class="advertise-history-update-nav" :to="{ name: 'Listing', params: { listing_id: listing.id } }">View listing</router-link>
          </div>
        </div>
      </div>

    </div>
</template>

<script>
export default {
    name: 'AdvertiseHistory',
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      unimplementedNotification() {
        alert("Sorry, property deletion has not been implemented.");
      }
    },
    computed: {
      listings() {
        return this.$store.state.advertise.history;
      }
    },
    beforeMount() {
      this.$store.dispatch('getAdvertiseHistory');
    }
    
}
</script>


<style>
/* New listing button */
.advertise-new-btn {
  background-color: rgb(82, 199, 118);
  background-image: linear-gradient(rgb(82, 199, 118), rgb(45, 181, 87) 90%);
  display: block;
  width: 75%;
  margin: 20px auto 0;
  text-align: center;
  padding: 10px;
  border-radius: 4px;
  font-size: 1.3em;
  color: white;
  box-shadow: 0 2px 12px #ccc;
}
/* Booking history */
.advertise-history-content {
  padding: 6px;
}
.advertise-history-item {
  box-shadow: 0 2px 8px #ccc;
  padding: 8px;
  margin-top: 24px;
}
.advertise-history-title {
  padding: 6px;
  overflow: auto;
}
.advertise-history-title > div {
  display: inline-block;
}
.advertise-history-type {
  color: rgb(107, 214, 188);
}
.advertise-history-location {
  float: right;
}
.advertise-history-location > i {
  color: coral;
}
.advertise-history-summary {
  background: rgb(235, 238, 238);
  border-radius: 6px;
  padding: 8px;
}
.advertise-history-info {
  display: inline-block;
  width: 32%;
}
.advertise-history-info > span {
  color: rgb(121, 126, 133);
  font-weight: 100;
}
.advertise-history-nav {
  margin-top: 6px;
  overflow: auto;
}
.advertise-history-nav > * {
  width: 45%;
  float: left;
  text-align: center;
  padding: 6px;
  margin: 0 2.5%;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
.advertise-history-delete-nav {
  background: tomato;

}
.advertise-history-update-nav {
  background: rgb(107, 214, 188);

}
.flash-message {
  display: block;
  width: 50%;
  margin: 30px auto 5px;
  
}
.advertise-flash {

  text-align: center;
  font-size: 1.2em;
  color: white;
  padding: 10px;
  background-color: tomato;
  border-radius: 4px;
  box-shadow: 0 5px 12px rgb(170, 170, 170);
}
.status-ok {
  background-color: rgb(41, 109, 212);
}
</style>
