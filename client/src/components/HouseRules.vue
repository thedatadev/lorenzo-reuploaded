<template>
    <div class="component listing-tab-main">

      <div class="listing-tab-nav">

        <a href="#" v-on:click.prevent="goBack" class="listing-tab-nav-back">
          <i class="fas fa-chevron-circle-left"></i>
        </a>

        <div class="listing-tab-nav-tabname">House rules</div>

      </div>

      <div class="listing-tab-content">

        <p v-if="listing.house_rules">{{ listing.house_rules }}</p>
        <p v-else>No house rules have been specified by the host.</p>
      
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
</style>
