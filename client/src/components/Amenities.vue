<template>
    <div class="component listing-tab-main">

      <div class="listing-tab-nav">

        <a href="#" v-on:click.prevent="goBack" class="listing-tab-nav-back">
          <i class="fas fa-chevron-circle-left"></i>
        </a>

        <div class="listing-tab-nav-tabname">Amenities</div>

      </div>

      <div class="listing-tab-content">

        <div v-if="listing.amenities">
          <div v-for="(amenity, index) in preprocessAmenities" :key="index" class="amenities-tab-amenity">
            {{amenity}}
          </div>
        </div>
        <div v-else>No amenities have been provided by the host.</div>
      
      </div>

    </div>
</template>

<script>
export default {
    name: "ListingTab",
    computed: {
        listing() {
            return this.$store.state.listings.active_listing;
        },
        preprocessAmenities() {
          let amenities = this.$store.state.listings.active_listing.amenities;
          if (!amenities || amenities.length === 0) {
            console.log("There are no amenities");
            return []
          }
          if (amenities[0] === '{') {
            console.log("Opening bracket detected");
            amenities = amenities.slice(1, amenities.length);
          }
          if (amenities[amenities.length-1] === '}') {
            console.log("Closing bracket detected");
            amenities = amenities.slice(0, amenities.length-1);
          }
          amenities = amenities.split(',');
          let preprocessed = [];
          for (let i = 0; i < amenities.length; i++) {
            if (amenities[i][0] == '"' && amenities[i][-1] == '"') {
              console.log(amenities[i] + " has quotes");
              preprocessed.push(amenities[i].slice(1, amenities[i].length - 1));
            } else {
              console.log(amenities[i] + " doesnt have quotes");
              preprocessed.push(amenities[i]);
            }
          }
          return preprocessed.slice(0, Math.min(10, preprocessed.length));
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
.amenities-tab-amenity {
  float: left;
  margin: 7px 12px;
  border-radius: 15px;
  padding: 2px 6px;
  background-color: rgb(230, 230, 230);
  color: rgb(163, 157, 157);
}
</style>
