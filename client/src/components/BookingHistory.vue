<template>
    <!-- Bookings main -->
    <div class="component booking-history-main">

      <!-- Header -->
      <div class="header">
        <!-- Chat header -->
        <a href="#" class="back" v-on:click.prevent="goBack">
          <i class="fas fa-arrow-circle-left"></i>
        </a>
        <div class="title">Booking History</div>
        <router-link class="home-shortcut" :to="{ name: 'Dashboard' }">
            <i class="fas fa-bars"></i>
        </router-link>
      </div>

      <!-- Successful booking notification -->
      <div v-if="this.$route.params.successfulBooking === true" class="successful-booking">Your booking was successful! View it below</div>

      <!-- Bookings content -->
      <div v-if="bookings.length > 0" class="booking-history-content">

        <!-- Booking history item -->
        <div class="booking-history-item" v-for="booking in bookings" :key="booking.id">
          <div class="booking-history-title">
            <div class="booking-history-type">{{booking.listing_room_type}} in {{booking.listing_property_type}}</div>
            <div class="booking-history-location">
              <i class="fas fa-map-marker-alt"></i>
              <span>{{booking.neighbourhood}}</span>
            </div>
          </div>
          <div class="booking-history-summary">
            <div class="booking-history-period">
              <div class="booking-history-checkin">
                {{getArrivalDate(booking.start_date)}}
              </div>
              <div class="booking-history-arrow">
                <i class="fas fa-arrow-right"></i>
              </div>
              <div class="booking-history-checkout">
                {{ getDeparture(booking.start_date, booking.num_nights) }}
              </div>
            </div>
            <div class="booking-history-price">${{booking.price}}</div>
          </div>
          <!-- Nav -->
          <div class="booking-history-nav">
            <div class="booking-history-listing-nav">
              <router-link :to="{ name: 'Listing', params: { listing_id: booking.listing_id } }">See listing</router-link>
            </div>
            <div class="booking-history-booking-nav">
              <router-link :to="{ name: 'Booking', params: { booking: booking } }">See booking</router-link>
            </div>
          </div>
        </div>
      </div>
      <div v-else>No bookings to display</div>

    </div>
</template>

<script>
export default {
    name: 'BookingHistory',
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      getArrivalDate(start_date) {
          let arrivalDate = new Date(start_date);
          const day = arrivalDate.getDate();
          const month = arrivalDate.getMonth() + 1;
          const year = arrivalDate.getFullYear();
          return day + '/' + month + '/' + year; 
      },
      getDeparture(start_date, num_nights) {

          let arrivalDate = new Date(start_date);
          const departureDate = new Date();
          departureDate.setDate(arrivalDate.getDate() + num_nights);

          const day = departureDate.getDate();
          const month = departureDate.getMonth() + 1;
          const year = departureDate.getFullYear();
          return day + '/' + month + '/' + year; 

      }
    },
    computed: {
      bookings() {
        return this.$store.state.bookings.history;
      }
    },
    beforeMount() {
      this.$store.dispatch('getBookingHistory');
    }
}
</script>

<style>
/* Booking history */
.booking-history-content {
  padding: 6px;
}
.booking-history-item {
  box-shadow: 0 2px 8px #ccc;
  padding: 8px;
  margin-top: 24px;
}
.booking-history-title {
  padding: 6px;
  overflow: auto;
}
.booking-history-title > div {
  display: inline-block;
}
.booking-history-type {
  color: rgb(107, 214, 188);
}
.booking-history-location {
  float: right;
}
.booking-history-location > i {
  color: coral;
}
.booking-history-summary {
  background: rgb(235, 238, 238);
  border-radius: 6px;
  padding: 8px;
}
.booking-history-summary > div {
  display: inline-block;
}
.booking-history-price {
  float: right;
  font-size: 1.1em;
  font-weight: bold;
}
.booking-history-period > div {
  display: inline-block;
  margin-left: 12px;
}
.booking-history-nav {
  margin-top: 6px;
  overflow: auto;
}
.booking-history-nav > div {
  display: inline-block;
  width: 45%;
  float: left;
  text-align: center;
  padding: 6px;
  margin: 0 2.5%;
  border-radius: 4px;
  cursor: pointer;
}
.booking-history-nav > div > a {
  color: white;
}
.booking-history-listing-nav {
  background: coral;
}
.booking-history-booking-nav {
  background: rgb(107, 214, 188);
}
.successful-booking {
  display: block;
  margin: 20px auto 0;
  padding: 10px;
  width: 60%;
  border-radius: 4px;
  background-color: rgb(55, 201, 79);
  text-align: center;
  color: white;
}

</style>
