<template>
    <!-- Make booking main -->
      <div class="component make-bk-main">

        <!-- Header -->
        <div class="header">
          <!-- Chat header -->
          <a href="#" class="back" v-on:click.prevent="goBack">
            <i class="fas fa-arrow-circle-left"></i>
          </a>
          <div class="title">Make a booking</div>
        </div>

        <!-- listing summary -->
        <div class="listing-summary">
          <div class="listing-summary-info">
            <div class="listing-summary-pic" :style="{ 'backgroundImage': 'linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.76) 95%), url(' + listing.picture_url + ')' }">
              <div class="listing-summary-pic-gap">

              </div>
              <div class="listing-summary-pic-content">
                <p>{{listing.room_type}} in {{listing.property_type}}</p>
                <p v-if="listing.neighbourhood !== null">{{ listing.neighbourhood}}</p>
                <p v-else>{{ listing.neighbourhood_cleansed }}</p>
              </div>
            </div>
          </div>

        </div>
        <!-- checkin / checkout -->
        <div class="checkin-checkout">
          <div class="checkin">
            <p>Arrival</p>
            <p>
              <p v-if="this.$store.state.chat.params.date">{{getArrival}}</p>
              <input class="price-summary-param-req" v-else type="text" placeholder='DD/MM/YY' :value="arrivalDateInput">
            </p>
          </div>
          <div class="checkin-arrow">
            <i class="fas fa-arrow-right"></i>
          </div>
          <div class="checkout">
            <p>Departure</p>
            <p>
              <p v-if="this.$store.state.chat.params.duration">{{getDeparture}}</p>
              <p v-else class="price-summary-param-req">....</p>
            </p>
            
          </div>
        </div>
        <!-- price summary -->
        <div class="price-summary">

          <div class="price-summary-row">
            <!-- Placeholder -->
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Length of stay</div>
            <div class="price-summary-value">
              <input class="price-summary-param-req" v-if="!this.$store.state.chat.params.duration.amount" type="number" placeholder="How many nights?" :value="durationInput">
              <span v-else>{{this.getDuration}} nights</span>
            </div>
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Cost per night</div>
            <div class="price-summary-value">${{listing.price}} AUD</div>
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Discount coupon</div>
            <div class="price-summary-value">
              <input class="discount-coupon" type="text" value="L0R3NZ02018">
            </div>
          </div>

          <div class="price-summary-row">
            <div class="price-summary-label">Total cost</div>
            <div class="price-summary-value">${{listing.price * getDuration}} AUD</div>
          </div>

        </div>
        <!-- submit button -->
        <div class="make-bk-btn">
          <a href="#" v-on:click.prevent="makeBooking">Confirm booking</a>
        </div>
      </div>
</template>

<script>
export default {
    name: "MakeBooking",
    data() {
      return {
        monthNames: [
            "January", "February", "March",
            "April", "May", "June", "July",
            "August", "September", "October",
            "November", "December"
          ],
        arrivalDateInput: '',
        durationInput: ''
      }
    },
    computed: {
        listing() {
            return this.$store.state.listings.active_listing;
        },
        getArrival() {
          const date = new Date(this.$store.state.chat.params.date);
          const day = date.getDate();
          const monthIndex = date.getMonth();
          const year = date.getFullYear();
          return day + ' ' + this.monthNames[monthIndex] + ' ' + year; 
        },
        getDeparture() {
          let durationAmnt = this.$store.state.chat.params.duration.amount;
          const durationUnit = this.$store.state.chat.params.duration.unit;

          if (durationUnit === "wk") {
            durationAmnt = durationAmnt * 7;
          } else if (durationUnit === "mo") {
            durationAmnt = durationAmnt * 28
          }

          let arrivalDate = new Date(this.$store.state.chat.params.date);
          const departureDate = new Date();
          departureDate.setDate(arrivalDate.getDate() + durationAmnt);

          const day = departureDate.getDate();
          const monthIndex = departureDate.getMonth();
          const year = departureDate.getFullYear();
          return day + ' ' + this.monthNames[monthIndex] + ' ' + year; 

        },
        getDuration() {
          let durationAmnt = this.$store.state.chat.params.duration.amount;
          const durationUnit = this.$store.state.chat.params.duration.unit;

          if (durationUnit === "wk") {
            durationAmnt = durationAmnt * 7;
          } else if (durationUnit === "mo") {
            durationAmnt = durationAmnt * 28
          }

          return durationAmnt;
        }
    },
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      makeBooking() {
        // Check that all required params exist, and if not, that the user has provided them
        let arrivalDate = null;
        let duration = null;
        let listing_id = this.$store.state.listings.active_listing.id;

        // TODO: Number guests??

        // Arrival
        if (this.$store.state.chat.params.date) {
          arrivalDate = this.$store.state.chat.params.date;
        } else if (this.arrivalDateInput) {
          arrivalDate = this.arrivalDateInput;
        }

        // Duration
        if (this.$store.state.chat.params.duration.amount) {

          let durationAmnt = this.$store.state.chat.params.duration.amount;
          const durationUnit = this.$store.state.chat.params.duration.unit;

          if (durationUnit === "wk") {
            durationAmnt = durationAmnt * 7;
          } else if (durationUnit === "mo") {
            durationAmnt = durationAmnt * 28
          }

          duration = durationAmnt;

        } else if (this.durationInput) {
          duration = this.durationInput;
        }

        // Check if all parameters provided
        if (!arrivalDate || !duration) {

        } else {

          let bookingInfo = {
            start_date: arrivalDate,
            num_nights: duration,
            listing_id: listing_id
          }

          console.log(bookingInfo);

          this.$store.dispatch('makeBooking', bookingInfo);
        }




      }
    }
}
</script>

<style>
.make-bk-main {
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
.price-summary-row:nth-child(4) {
  border-bottom: 1px solid #ccc;
}
.price-summary-row:nth-child(5) {
  font-size: 1.3em;
  color: rgb(52, 219, 174);
}
.make-bk-btn {
  margin: 20px auto 0 auto;
  text-align: center;
  width: 85%;
  background-color: rgb(52, 219, 174);
  background-image: linear-gradient(rgb(52, 219, 174), rgba(31, 185, 144, 0.78) 90%);
  padding: 10px;
  border-radius: 6px;
  box-shadow: 0 3px 8px #ccc;
}
.make-bk-btn > a {
  color: white;
}
.discount-coupon {
  font-size: 0.9em;
  width: 100px;
  color: #ccc;
  padding: 2px;
}
.price-summary-param-req {
  font-size: 0.7em;
  padding: 4px 4px 6px 4px;
  border-style: none;
  border-bottom: 2px solid tomato;
}
.price-summary-param-req::placeholder {
    color: tomato;
}
</style>
