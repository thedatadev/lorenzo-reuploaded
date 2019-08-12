<template>
<div class="component booking-main">

        <!-- Header -->
        <div class="header">
          <!-- Chat header -->
          <a href="#" class="back" v-on:click.prevent="goBack">
            <i class="fas fa-arrow-circle-left"></i>
          </a>
          <div class="title">View booking</div>
        </div>

        <!-- listing summary -->
        <div class="listing-summary">
          <div class="listing-summary-info">
            <div class="listing-summary-pic" :style="{ 'backgroundImage': 'linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.76) 99%),url(' + booking.picture_url + ')' }">
              <div class="listing-summary-pic-gap">

              </div>
              <div class="listing-summary-pic-content">
                <p>{{booking.listing_room_type}} in {{booking.listing_property_type}}</p>
                <p>{{booking.neighbourhood}}</p>
              </div>
            </div>
          </div>

        </div>
        <!-- checkin / checkout -->
        <div class="checkin-checkout">
          <div class="checkin">
            <p>Arrival</p>
            <p>{{getArrivalDate(booking.start_date)}}</p>
          </div>
          <div class="checkin-arrow">
            <i class="fas fa-arrow-right"></i>
          </div>
          <div class="checkout">
            <p>Departure</p>
            <p>{{ getDepartureDate(booking.start_date, booking.num_nights) }}</p>
          </div>
        </div>
        <!-- price summary -->
        <div class="price-summary">

          <div></div>

          <div class="price-summary-row">
            <div class="price-summary-label">Length of stay</div>
            <div class="price-summary-value">{{booking.num_nights}} nights</div>
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Cost per night</div>
            <div class="price-summary-value">${{booking.price}} AUD</div>
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Total cost</div>
            <div class="price-summary-value">${{booking.price * booking.num_nights}} AUD</div>
          </div>

        </div>

      </div>
</template>

<script>
export default {
    name: 'Booking',
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      getArrivalDate(start_date) {
          const arrivalDate = new Date(start_date);
          const day = arrivalDate.getDate();
          const month = arrivalDate.getMonth() + 1;
          const year = arrivalDate.getFullYear();
          return day + '/' + month + '/' + year; 
      },
      getDepartureDate(start_date, num_nights) {

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
      booking() {
        return this.$route.params.booking;
      }
    }
}
</script>

<style>
.booking-main {
  padding: 4px;
}
.listing-summary-info > div {
  display: inline-block;
}
.listing-summary-pic {
  background-size: cover;
  background-position: center;
  height: 200px;
  width: 100%;
  box-shadow: 0 2px 8px #ccc;
}
.listing-summary-pic-gap {
  height: 70%;
}
.listing-summary-pic-content {
  padding-left: 10px;
}
.listing-summary-pic-content > p:nth-child(1) {
  color: rgb(48, 208, 174);
}
.listing-summary-pic-content > p:nth-child(2) {
  color: white;
  font-size: 1.5em;
}
.checkin-checkout {
  margin-top: 20px;
  padding: 6px;
  box-shadow: 0 2px 8px #ccc;
  overflow: auto;
}
.checkin-checkout > div {
  display: inline-block;
  height: 50px;
  float: left;
  text-align: center;
}
.checkin-checkout > .checkin,
.checkin-checkout > .checkout {
  width: 40%;
}
.checkin-checkout > .checkin-arrow {
  width: 20%;
  color: #ccc;
  font-size: 2.6em;
}
.checkin-checkout > div > p:nth-child(1) {
  color: rgb(52, 219, 174);
}
.checkin-checkout > div > p:nth-child(2) {
  font-size: 1.4em;
  padding-top: 6px;
}
.price-summary {
  padding: 6px;
  box-shadow: 0 1px 8px #ccc;
  margin-top: 15px;
}
.price-summary-row {
  width: 100%;
  overflow: auto;
  padding: 6px 0;
}
.price-summary-row > div {
  float: left;
}
.price-summary-label {
  width: 70%;
}
.price-summary-value {
  width: 30%;
}
.price-summary-row:nth-child(3) {
  border-bottom: 1px solid #ccc;
}
.price-summary-row:nth-child(4) {
  font-size: 1.3em;
  color: rgb(52, 219, 174);
}
.booking-btn {
  margin: 20px auto 0 auto;
  text-align: center;
  width: 40%;
  padding: 10px;
  border-radius: 6px;
  box-shadow: 0 3px 8px #ccc;
  display: inline-block;
  float: left;
  margin: 20px 5% 0;
}
.booking-btn > a {
  color: white;
}
.see-listing-btn {
  background-color: rgb(238, 135, 85);
  background-image: linear-gradient(rgb(238, 135, 85), rgb(232, 121, 67) 90%);
}
.cancel-btn {
  background-color: rgb(238, 103, 103);
  background-image: linear-gradient(rgb(238, 103, 103), rgb(224, 84, 84) 90%);
}

</style>
