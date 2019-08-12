<template>
  <div class="component results-main" id="active-component">

    <div class="header">
      <a href="" v-on:click.prevent="goBack" class="back">
        <i class="fas fa-chevron-circle-left"></i>
      </a>
      <!-- Search results header -->
      <div class="title">Search results</div>
      <router-link class="home-shortcut" :to="{ name: 'Dashboard' }">
            <i class="fas fa-bars"></i>
        </router-link>
        
    </div>

    <div class="content search-results">
      <!-- Search results main screen -->
      <ul  class="display-listings">

        <!-- Listing template -->
        <li class="listing" v-for="listing in listings" :key="listing.id">
          <!-- Listing banner image -->
          <div class="listing-img">
            <!-- <img src="../assets/holiday_house.jpg" alt="Holiday House"> -->
            <div class="results-listing-picture" :style="{ backgroundImage: 'linear-gradient(rgba(255, 255, 255, 0), rgba(22, 21, 21, 0.945) 90%), url(' + listing.picture_url + ')' }">
              <div class="results-listing-picture-gap"></div>
              <div class="results-listing-picture-title">
                <div class="results-listing-picture-title-type">{{listing.room_type}} in {{listing.property_type}}</div>
                <div :class="{'results-listing-picture-title-name': true, 'short-title': isShort(listing.name), 'medium-title': isMed(listing.name), 'long-title': isLong(listing.name) }">{{listing.name}}</div>
              </div>
            </div>

          </div>
          <!-- Listing summary info -->
          <div class="listing-info">
            <div class="listing-info-body">

              <div class="listing-info-body-row">
                <div class="listing-info-body-item">
                  <i class="fas fa-map-marker-alt"></i>
                  <span v-if="listing.neighbourhood !== null">{{ listing.neighbourhood}}</span>
                  <span v-else>{{ listing.neighbourhood_cleansed }}</span>
                </div>
                <div class="listing-info-body-item">
                  <i class="fas fa-dollar-sign"></i>
                  <span>${{listing.price}} per night</span>
                </div>
              </div>

              <div class="listing-info-body-row">
                <div class="listing-info-body-item">
                  <i class="fas fa-users"></i>
                  <span>{{listing.accommodates}} guests</span>
                </div>
                <div class="listing-info-body-item">
                  <i class="fas fa-hourglass-half"></i>
                  <span>{{listing.minimum_nights}} - {{listing.maximum_nights}} nights</span>
                </div>
              </div>

            </div>
          </div>
          <!-- Listing link to individual page -->
          <div class="listing-link">
            <router-link :to="{ name: 'Listing', params: { listing_id: listing.id } }">More info</router-link>
            <!-- <a href="" v-on:click.prevent="getListing(listing.id)">More info</a> -->
          </div>
        </li>
        <!-- END of listing template -->
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: "Results",
  computed: {
    listings() {
      return this.$store.state.listings.results;
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1);
    },
    isMobile(mq) {
      return mq === "sm";
    },
    getListing(listing_id) {
      console.log("Attempting a fetch request for listing " + listing_id);
      this.$store.dispatch("getListing", listing_id);
      this.$router.push("/listing");
    },
    isShort(name) {
            return name.length <= 25;
        },
        isMed(name) {
            return 30 < name.length && name.length <= 60;;
        },
        isLong(name) {
            return name.length > 60;
        }
  },
  beforeMount() {
    // Before the Results component gets rendered, makes a HTTP GET request
    // for a list of search results to save to 'listings'
    this.$nextTick(function () {
      this.$store.dispatch('getSearchResults');
    });
  }
};
</script>

<style >
/* Both mobile & desktop styling */ 

/* Search results styling */
.display-listings {
  list-style: none;
  overflow: scroll;
  font-family: Arial;
  padding: 8px;
}
.display-listings .listing {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  /* background-color: rgb(227, 241, 236); */
  padding-bottom: 20px;
}
/* Listings styling */
.results-listing-picture {
    flex: 6;
    height: 280px;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
.results-listing-picture-gap {
  height: 80%;
}
.results-listing-picture-title {
  height: 20%;
  padding-left: 10px;
}
.results-listing-picture-title-type {
  color: rgb(40, 197, 171);
}
.results-listing-picture-title-name {
  color: white;
  font-size: 1.2em;
}
.listing .listing-info {
  flex: 2;
  display: flex;
  flex-direction: column;
}
.listing .listing-info .listing-info-header {
  font-size: 16px;
  padding: 8px 0;
  border-bottom: 1px solid rgb(211, 222, 218);
}
.listing .listing-info .listing-info-body {
  padding: 4px;
  margin: 6px 0;
}
.listing .listing-info .listing-info-body .listing-info-body-item {
  display: inline-block;
  width: 45%;
  margin-top: 6px;
}
.listing .listing-info .listing-info-body .listing-info-body-item > i {
  color: rgb(40, 197, 171);
  font-size: 1.4em;
}
.listing .listing-info .listing-info-body .listing-info-body-item > *:nth-child(1) {
  width: 20%;
  text-align: center;
}
.listing .listing-info .listing-info-body .listing-info-body-item > *:nth-child(2) {
  width: 80%;
}
.listing .listing-info .listing-info-body .listing-info-body-row > *:nth-child(1){
  padding-left: 10px;
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

/* More info button */ 
.listing .listing-link {
  width: 100%;
  text-align: center;
  background-color: rgb(40, 197, 171);
  padding: 7px 0;
  cursor: pointer;
  border-radius: 3px;
  margin-top: 10px;
  box-shadow: 0 3px 6px #ccc;
}
.listing .listing-link a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 16px;
}
/* Desktop-only styling */ 
@media(min-width:768px) {
  /* Search results styling */
  .results-main {
    overflow: scroll;
  }
}

/* Mobile-only styling */
@media(max-width:767px) {
  /* Search results styling */
  .display-listings {
    display: flex;
    flex-direction: column;
  }
  .display-listings .listing {
    flex: 1;
    margin: 0;
  }

}
</style>
