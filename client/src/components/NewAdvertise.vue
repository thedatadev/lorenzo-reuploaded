<template>
    <div class="component advertise-main">

      <!-- Header -->
      <div class="header">
        <!-- Chat header -->
        <a href="#" class="back" v-on:click.prevent="goBack">
          <i class="fas fa-arrow-left"></i>
        </a>
            
        <div class="title">Advertise</div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text"><span class="step-header">Step 1</span> - Required info</p>
        </div>
        <div class="content-wrapper">
          <div class="req-info-wrapper">
            <!-- Name of listing -->
            <div class="req-field req-name">
              <div class="req-label">Listing name</div>
              <input type="text" class="req-value"
                     placeholder="e.g. Holiday house in Manly" v-model="name">
            </div>
            <!-- Property type -->
            <div class="req-field req-type">
              <div class="req-label">Property type</div>
              <input type="radio" v-model="property_type" name="property-type" :value="'House'" checked><span>House</span>
              <input type="radio" v-model="property_type" name="property-type" :value="'Apartment'"><span>Apartment</span>
              <input type="radio" v-model="property_type" name="property-type" :value="'Townhouse'"><span>Townhouse</span>
            </div>
            <!-- Room type -->
            <div class="req-field req-type">
              <div class="req-label">Room type</div>
              <input type="radio" v-model="room_type" name="room-type" :value="'Private room'" checked><span>Private room</span>
              <input type="radio" v-model="room_type" name="room-type" :value="'Shared room'"><span>Shared room</span>
              <input type="radio" v-model="room_type" name="room-type" :value="'Entire home/apt'"><span>Entire home/apt</span>
            </div>
            <!-- Guest capacity -->
            <div class="req-field req-capacity">
              <div class="req-label">Guest capacity</div>
              <input type="number" class="req-value" placeholder="e.g. 4" v-model="accommodates">
            </div>
            <!-- Minimum nights -->
            <div class="req-field req-min-nights">
              <div class="req-label">Minimum nights</div>
              <input type="number" class="req-value" placeholder="e.g. 7" v-model="minimum_nights">
            </div>
            <!-- Maximum nights -->
            <div class="req-field req-max-nights">
              <div class="req-label">Maximum nights</div>
              <input type="number" class="req-value" placeholder="e.g. 28" v-model="maximum_nights">
            </div>
            <!-- Price -->
            <div class="req-field req-price">
              <div class="req-label">Price ($AUD)</div>
              <input type="number" class="req-value" placeholder="e.g. 70" v-model="price">
            </div>
            <!-- Neighbourhood -->
            <div class="req-field req-neighbourhood">
              <div class="req-label">Neighbourhood</div>
              <input type="text" class="req-value" placeholder="e.g. Kensington" v-model="neighbourhood">
            </div>
            <!-- Address -->
            <div class="req-field req-address">
              <div class="req-label">Address</div>
              <input type="text" class="req-value" placeholder="e.g. 1 George St" v-model="address">
            </div>
            <!-- Bedrooms -->
            <div class="req-field req-capacity">
              <div class="req-label">Bedrooms</div>
              <input type="number" class="req-value" placeholder="e.g. 4" v-model="bedrooms">
            </div>
            <!-- Beds -->
            <div class="req-field req-capacity">
              <div class="req-label">Beds</div>
              <input type="number" class="req-value" placeholder="e.g. 4" v-model="beds">
            </div>
            <!-- Bathrooms -->
            <div class="req-field req-capacity">
              <div class="req-label">Bathrooms</div>
              <input type="number" class="req-value" placeholder="e.g. 2" v-model="bathrooms">
            </div>
            <!-- Amenities -->
            <div class="req-field req-amenities">
              <div class="req-label">Amenities</div>

              <!-- Amenity list -->
              <ul class="req-list amenity-list">

                <!-- Amenity template -->
                <li v-for="(amenity, index) in amenities" :key="index" class="amenity">
                  <span class="amenity-name">{{amenity}}</span>
                </li>

                <!-- Add new amenity (bring up input field) -->
                <li v-if="!adding_amenity" class="req-add-btn">
                  <span>
                    <i v-on:click.prevent="addNewAmenity" class="fas fa-plus"></i>
                  </span>
                </li>

                <!-- Save new amenity to list -->
                <li v-if="adding_amenity" class="req-add-input">
                  <input type="text" placeholder="New amenity" v-model="new_amenity">
                  <span>
                    <i v-on:click.prevent="saveNewAmenity" class="fas fa-plus"></i>
                  </span>
                </li>


              </ul> <!-- END Amenity list -->

            </div>
          </div>
        </div>
      </div>


      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text"><span class="step-header">Step 2</span> - Accommodation (optional)</p>
        </div>
        <div class="content-wrapper">
          <div class="description-wrapper">
            <textarea v-model="description" name="name" placeholder="Write about your accommodation here..."></textarea>
          </div>
        </div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text"><span class="step-header">Step 3</span> - Transit (optional)</p>
        </div>
        <div class="content-wrapper">
          <div class="description-wrapper">
            <textarea v-model="transit" name="name" placeholder="Write about access to public transport here..."></textarea>
          </div>
        </div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text"><span class="step-header">Step 4</span>- House rules (optional)</p>
        </div>
        <div class="content-wrapper">
          <div class="description-wrapper">
            <textarea v-model="house_rules" name="name" placeholder="Write about your house rules here..."></textarea>
          </div>
        </div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text"><span class="step-header">Step 5</span> - Picture</p>
        </div>
        <div class="content-wrapper picture-upload">
          <input type="file" accept="img/*">
        </div>
      </div>

      <!-- Submit button -->
      <div class="advertise-section">
        <a id="demo-autofill" v-on:click.prevent="demoAutoFill">Demo Autofill</a>
        <a id="advertise-submit" v-on:click.prevent="postNewListing">Post listing</a>
      </div>

    </div>
</template>

<script>
export default {
    name: 'NewAdvertise',
    data() {
      return {
        name: '',
        description: '',
        neighbourhood: '',
        property_type: 'House',
        room_type: '',
        accommodates: null,
        price: null,
        transit: '',
        address: '',
        bedrooms: null,
        beds: null,
        bathrooms: null,
        amenities: [],
        new_amenity: '',
        adding_amenity: false,
        minimum_nights: null,
        maximum_nights: null,
        house_rules: ''
      }
    },
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      addNewAmenity() {
        this.adding_amenity = true;
      },
      saveNewAmenity() {
        this.amenities.push(this.new_amenity);
        this.new_amenity = '';
        this.adding_amenity = false;
      },
      postNewListing() {

        let formData = new FormData();
        var fileField = document.querySelector("input[type='file']");

        const formFields = [
          'name',
          'description',
          'neighbourhood',
          'property_type',
          'room_type',
          'accommodates',
          'price',
          'transit',
          'address',
          'bedrooms',
          'beds',
          'bathrooms',
          'amenities',
          'minimum_nights',
          'maximum_nights',
          'house_rules'
        ]

        for (let i = 0; i < formFields.length; i++) {
          formData.append(formFields[i], this[formFields[i]]);
        }

        formData.append('picture_obj', fileField.files[0]);

        this.$store.dispatch('newListing', formData);
      },
      demoAutoFill() {
        this.name = "Bondi beach house";
        this.description = "A modern, chic two-storey house by the ocean. Ideal for surfers and beachgoers";
        this.neighbourhood = "Bondi";
        this.property_type = "House";
        this.room_type = "Entire apt/home";
        this.accommodates = 6;
        this.price = 120;
        this.transit = "Close to buses. 5 min. walk from train station";
        this.address = "1 Notts Ave, Bondi Beach NSW 2026";
        this.bedrooms = 3;
        this.beds = 4;
        this.bathrooms = 3;
        this.amenities = ["Wifi", "TV"];
        this.minimum_nights = 4;
        this.maximum_nights = 90;
        this.house_rules = "No smoking; keep rooms tidy";
      }
    }
}
</script>

<style>

.advertise-section {
  padding: 10px;
}
.title-wrapper {
  position: relative;
  height: 10px;
}
.title-text {
  position: absolute;
  left: 10%;
  background: white;
  padding: 0 10px;
  font-weight: bold;
}
.content-wrapper {
  border-radius: 4px;
  padding: 20px 5px 5px;
  box-shadow: 0 2px 6px rgb(140, 152, 153);
}
/* Paramater options */
.component .header .see-results > span {
  color: white;
  font-family: Arial;
  margin-right: 7px;
}
.component .header .fa-map-marker-alt {
  margin: 5px 7px 0 0;
  font-size: 1.6em;
  color: white;
}
/* Required info */
.req-info-wrapper {
  padding: 8px;
}
.req-info-wrapper > .req-field {
  margin: 10px 0;
}
.req-info-wrapper > .req-field > .req-label {
  font-size: 0.9em;
  margin-bottom: 6px;
  color: rgb(71, 205, 173);
}
.req-info-wrapper > .req-field > .req-value {
  font-size: 1.1em;
  width: 100%;
  padding-bottom: 6px;
  border-style: none;
  border-bottom: 2px solid rgb(209, 219, 215);
}
.req-info-wrapper > .req-field > .req-value:focus {
  outline: none;
  border-bottom-color: rgb(56, 168, 141);
}
.req-info-wrapper > .req-field > .req-value::placeholder {
  color: rgb(217, 224, 222);
}
/* Required accommodation type */
.req-info-wrapper .req-type {
  width: 100%;
  display: inline-block;
}
.req-info-wrapper .req-type > span {
  margin-right: 8px;
}
.req-info-wrapper .req-type > input {
  margin-right: 4px;
}
/* Required list (Amenities/Pets) */
.req-list {
  list-style-type: none;
}
.req-list > * {
  background-color: rgb(244, 246, 246);
  color: rgb(56, 170, 153);
  font-size: 0.8em;
  font-weight: 100;
  padding: 8px;
  margin: 4px;
  display: inline-block;
  border-radius: 4px;
}
.req-list > .req-add-btn {
  background-color: rgb(22, 212, 149);
  color: white;
  cursor: pointer;
}
.req-list > .req-add-input {
  background-color: rgb(22, 212, 149);
}
.req-list > .req-add-input > input {
  border-style: none;
  font-size: 1.2em;
  padding: 3px;
  width: 100px;
}
.req-list > .req-add-input > input:focus {
  outline: none;
}
.req-list > .req-add-input > input::placeholder {
  color: #ccc;
}
.req-list > .req-add-input > span {
  color: white;
  cursor: pointer;
  padding: 4px;
  font-size: 1.1em;
}
/* Description wrapper */
.description-wrapper > textarea {
  padding: 8px;
  width: 100%;
  height: 150px;
  font-size: 1.2em;
  border-style: none;
  line-height: 1.6em;
}
.description-wrapper > textarea:focus {
  outline: none;
}
.description-wrapper > textarea::placeholder {
  color: rgb(217, 220, 222);
}
/* Advertise submit button */
#advertise-submit {
  background-color: rgb(65, 210, 176);
  color: white;
  background-image: linear-gradient(rgb(65, 210, 176), rgba(46, 182, 150, 0.87) 90%);
  border-radius: 4px;
  box-shadow: 0 2px 5px rgb(190, 193, 191);
  text-align: center;
  padding: 6px;
  margin-bottom: 100px;
  cursor: pointer;
  font-size: 1.3em;
  width: 100%;
  display: block;
}
#demo-autofill {
  background-color: rgb(210, 65, 77);
  color: white;
  background-image: linear-gradient(rgb(210, 65, 77), rgba(190, 37, 50, 0.856) 90%);
  border-radius: 4px;
  box-shadow: 0 2px 5px rgb(190, 193, 191);
  text-align: center;
  padding: 6px;
  margin-bottom: 10px;
  cursor: pointer;
  font-size: 1.3em;
  width: 100%;
  display: block;
}
.picture-upload {
  padding: 22px;
  text-align: center;
}
.step-header {
  color: coral;
}
</style>
