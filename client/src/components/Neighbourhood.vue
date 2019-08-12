<template>
    <div class="component listing-tab-main">

      <div class="listing-tab-nav">

        <a href="#" v-on:click.prevent="goBack" class="listing-tab-nav-back">
          <i class="fas fa-chevron-circle-left"></i>
        </a>

        <div class="listing-tab-nav-tabname">Neighbourhood</div>

      </div>

      <div class="listing-tab-content">

        <div class="listing-neighbourhood-info neighbourhood-name">
          <i class="fas fa-map-marker-alt"></i>
          <p>{{ listing.neighbourhood }}</p>
        </div>

        <div class="listing-neighbourhood-info">
          <p class="transit-title">
            <i class="fas fa-bus-alt"></i>
            <span>Transit</span>  
          </p>
          <p>{{ listing.transit }}</p>
        </div>

        <div v-if="listing.places" class="listing-neighbourhood-info">
          <p class="poi-title">
            <i class="fas fa-street-view"></i>
            <span>Places of interest</span>
          </p>
          
          <div class="poi-counts">

            <div class="poi-row">
              <div class="poi-col">
                <i class="fas fa-money-check-alt"></i>
                <span>ATM</span>
                <span class='place-count'>{{listing.places.ATM}}</span>
              </div>
              <div class="poi-col">
                <i class="fas fa-wine-glass-alt"></i>
                <span>Bar</span>
                <span class='place-count'>{{listing.places.bar}}</span>
              </div>
            </div>

            <div class="poi-row">
              <div class="poi-col">
                <i class="fas fa-bus"></i>
                <span>Bus</span>
                <span class='place-count'>{{listing.places.bus_station}}</span>
              </div>
              <div class="poi-col">
                <i class="fas fa-subway"></i>
                <span>Train</span>
                <span class='place-count'>{{listing.places.train_station}}</span>
              </div>
            </div>

            <div class="poi-row">
              <div class="poi-col">
                <i class="fas fa-coffee"></i>
                <span>Cafe</span>
                <span class='place-count'>{{listing.places.cafe}}</span>
              </div>
              <div class="poi-col">
                <i class="fas fa-utensils"></i>
                <span>Restaurant</span>
                <span class='place-count'>{{listing.places.restaurant}}</span>
              </div>
            </div>




          </div>

        </div>

      
      </div>

    </div>
</template>

<script>
export default {
    name: "ListingTab",
    computed: {
        listing() {
            return this.$store.state.listings.active_listing;
        }
    },
    methods: {
      goBack() {
          this.$router.go(-1);
        }
    }
}
</script>

<style>
.listing-tab-nav {
  border-bottom: 1px solid #ccc;
  padding: 12px;
}

.listing-tab-nav > * {
  display: inline-block;
}

.listing-tab-nav-back > i {
  font-size: 2.6em;
  color: rgb(66, 214, 188);
}

.listing-tab-nav-tabname {
  font-size: 1.4em;
  width: 80%;
  text-align: center;
}

.listing-tab-content {
  padding: 15px;
  line-height: 1.6em;
  color: rgb(65, 68, 70);
}
.listing-neighbourhood-info {
  margin-top: 35px;
}
.neighbourhood-name, .transit-title, .poi-title {
  font-size: 1.5em;
  margin-bottom: 20px;
}
.neighbourhood-name > * {
  display: inline-block;
}
.neighbourhood-name > i {
  display: inline-block;
  color: coral;
}
.transit-title > i {
  color: coral;
}
.poi-title > i {
  color: coral;
}
.poi-row {
  width: 90%;
  margin: 10px auto;
}
.poi-col {
  display: inline-block;
  width: 35%;
  margin-right: 30px;
}
.poi-col > * {
  display: inline-block;
}
.place-count {
  color: rgb(44, 206, 198);
  float: right;
  font-weight: bold;
  font-size: 1.1em;
}
</style>
