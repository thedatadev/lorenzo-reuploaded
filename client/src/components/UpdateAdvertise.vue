<template>
    <div class="component advertise-main">

      <!-- Header -->
      <div class="header">
        <!-- Chat header -->
        <a href="#" class="back" v-on:click.prevent="goBack">
            <i class="fas fa-arrow-left"></i>
        </a>
        <div class="title">Edit listing</div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text">Required info</p>
        </div>
        <div class="content-wrapper">
          <div class="req-info-wrapper">
            <!-- Name of listing -->
            <div class="req-field req-name">
              <div class="req-label">Listing name</div>
              <input type="text" class="req-value"
                     placeholder="e.g. Holiday house in Manly">
            </div>
            <!-- Accommodation type -->
            <div class="req-field req-type">
              <div class="req-label">Accommodation type</div>
              <input type="radio" name="accommodation-type" value="House" checked><span>House</span>
              <input type="radio" name="accommodation-type" value="Apartment"><span>Apartment</span>
              <input type="radio" name="accommodation-type" value="Townhouse"><span>Townhouse</span>
            </div>
            <!-- Guest capacity -->
            <div class="req-field req-capacity">
              <div class="req-label">Guest capacity</div>
              <input type="number" class="req-value" placeholder="e.g. 4">
            </div>
            <!-- Minimum nights -->
            <div class="req-field req-min-nights">
              <div class="req-label">Minimum nights</div>
              <input type="number" class="req-value" placeholder="e.g. 7">
            </div>
            <!-- Maximum nights -->
            <div class="req-field req-max-nights">
              <div class="req-label">Maximum nights</div>
              <input type="number" class="req-value" placeholder="e.g. 28">
            </div>
            <!-- Price -->
            <div class="req-field req-price">
              <div class="req-label">Price ($AUD)</div>
              <input type="text" class="req-value" placeholder="e.g. 70">
            </div>
            <!-- Suburb -->
            <div class="req-field req-suburb">
              <div class="req-label">Suburb</div>
              <input type="text" class="req-value" placeholder="e.g. Kensington">
            </div>
            <!-- Address -->
            <div class="req-field req-address">
              <div class="req-label">Address</div>
              <input type="text" class="req-value" placeholder="e.g. 1 George St">
            </div>
            <!-- Bedrooms -->
            <div class="req-field req-capacity">
              <div class="req-label">Bedrooms</div>
              <input type="number" class="req-value" placeholder="e.g. 4">
            </div>
            <!-- Bathrooms -->
            <div class="req-field req-capacity">
              <div class="req-label">Bathrooms</div>
              <input type="number" class="req-value" placeholder="e.g. 2">
            </div>
            <!-- Amenities -->
            <div class="req-field req-amenities">
              <div class="req-label">Amenities</div>

              <!-- Amenity list -->
              <ul class="req-list amenity-list">
                <!-- Amenity template -->
                <li class="amenity">
                  <span class="amenity-name">Wifi</span>
                </li>

                <li class="amenity">
                  <span class="amenity-name">PS4</span>
                </li>

                <li class="amenity">
                  <span class="amenity-name">Netflix</span>
                </li>

                <li id="add-amenity" class="req-add-btn">
                  <span>
                    <i class="fas fa-plus"></i>
                  </span>
                </li>


              </ul> <!-- END Amenity list -->

            </div>


            <!-- Pets -->
            <div class="req-field req-pets">
              <div class="req-label">Pets</div>

              <!-- Pet list -->
              <ul class="req-list pet-list">
                <!-- Pet template -->
                <li class="pet">
                  <span class="pet-name">Dog</span>
                </li>

                <li class="pet">
                  <span class="pet-name">Cat</span>
                </li>

                <li id="add-pet" class="req-add-btn">
                  <span>
                    <i class="fas fa-plus"></i>
                  </span>
                </li>

              </ul> <!-- END Pet list -->
            </div>
          </div>
        </div>
      </div>


      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text">Description (optional)</p>
        </div>
        <div class="content-wrapper">
          <div class="description-wrapper">
            <textarea name="name" placeholder="Write about your listing here..."></textarea>
          </div>
        </div>
      </div>

      <div class="advertise-section">
        <div class="title-wrapper">
          <p class="title-text">Picture</p>
        </div>
        <div class="content-wrapper picture-upload">
          <input type="file" accept="img/*">
        </div>
      </div>

      <!-- Submit button -->
      <div class="advertise-section">
        <div id="advertise-submit">Save changes</div>
      </div>

    </div>
</template>

<script>
export default {
    name: 'UpdateAdvertise',
    methods: {
      goBack() {
        this.$router.go(-1);
      }
    }
}
</script>

<style>
/* .advertise-main {
} */
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
}
.picture-upload {
  padding: 22px;
  text-align: center;
}
</style>
