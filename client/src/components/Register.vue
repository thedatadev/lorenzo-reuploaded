<template>
    <!-- Registration main component -->
      <div class="component registration-main">

        <!-- Header -->
        <div class="lorenzo-header-container">
            <div class="lorenzo-header-logo">
                <!-- Logo -->
                <router-link  class="button" :to="{name: 'Homepage'}" >
                    <span>L</span>
                    <span><i class="far fa-comment"></i></span>
                    <span>R E N Z</span>
                    <span><i class="far fa-comment fa-flip-horizontal"></i></span>
                    <span class="bnb">BnB</span>
                </router-link>
            </div>
            <div class="lorenzo-header-slogan">
              <!-- Slogan -->
              <span class="slogan">Straight to the p<i class="fas fa-map-marker-alt"></i>int</span>
            </div>
        </div>

        <div v-if="registerWarning" class="register-warning">An account with that email already exists</div>

        <!-- Registration form -->
        <div class="registration-form-container">
          <form @submit.prevent="submitRegistration()" class="registration-form">
            <div class="registration-form-field">
              <!-- Email field -->
              <label for="username">Email</label>
              <input autocomplete="off" type="text" name="email" id="register-email-field">
            </div>
             <div class="registration-form-field">
              <!-- Username field -->
              <label for="username">Username</label>
              <input autocomplete="off" type="text" name="username" id="register-username-field">
            </div>
            <div class="registration-form-field">
              <!-- Password field -->
              <label for="password">Password</label>
              <input autocomplete="off" type="password" name="password" id="register-password-field">
            </div>
            <div class="registration-form-field">
              <!-- Submit button -->
              <button name="register-button" id="register-button">Register</button>
            </div>
          </form>
        </div>
      </div>
</template>

<script>
export default {
    name: 'Homepage',
    data() {
      return {
        registerWarning: false
      }
    },
    methods: {
      submitRegistration() {

          this.registerWarning = false;

          // Gather all user credentials
          const emailField = document.getElementById("register-email-field");
          const usernameField = document.getElementById("register-username-field");
          const passwordField = document.getElementById("register-password-field");
          // Registration endpoint
          const API_ENDPOINT = "http://127.0.0.1:5000/register";
          // Package the credentials into an object
          let registration = {
              email: emailField.value,
              username: usernameField.value,
              password: passwordField.value
          }
          // Reset the form fields
          emailField.value = '';
          usernameField.value = '';
          passwordField.value = '';
          // Instantiate the request
          const request = new Request(API_ENDPOINT, {
            method: 'POST',
            headers: new Headers({
              "Content-Type": "application/json"
            }),
            body: JSON.stringify(registration)
          });
          // NOTE: To make the 'this' instance accessible in 
          //       the FETCH code block, it needs to be 
          //       referenced. This might be because the FETCH
          //       scope may have its own 'this' object.
          let self = this;
          // Send the fetch request
          fetch(request)
          .then(function(response) {

              console.log(request);
              // Upon successful registration, reroute the user to the login page
              if (response.status === 200) {
                  const payload = response.json();
                  console.log(payload);
                  self.$router.push({name: 'Login', params: { successfulLogin: true }})

              } else if (response.status === 401) {
                  self.registerWarning = true;
              } else {
                throw new Error(response.statusText);
              }
          })
          .catch(function(error) {
              console.log(error);
          });
          
      }
  }
}
</script>

<style>
    /* General styling */
    * {
      margin: 0;
      padding: 0;
    }
    .container {
      width: 100%;
      height: 100vh;
    }
    /* Registration general styling */
    .registration-main {
      max-width: 90%;
      margin: 0 auto;
      padding-top: 25px;
    }
    /* Registration form styling */
    .registration-form-container {
      font-family: Arial;
    }
    .registration-form-container .registration-form .registration-form-field {
      margin: 30px auto;
      width: 80%;
      text-align: center;
    }
    .registration-form-container .registration-form .registration-form-field > * {
      display: block;
      margin: 0 auto;
    }
    .registration-form-container .registration-form .registration-form-field > input {
      display: block;
      padding: 6px;
    }
    .registration-form-container .registration-form #register-button {
      padding: 8px;
      width: 50%;
      background-color: rgb(42, 219, 166);
      color: white;
      border-style: none;
      cursor: pointer;
      border-radius: 4px;
      font-size: 1.2em;
    }
    .registration-form-container .registration-form .registration-form-field > input {
      font-size: 1.1em;
      padding: 6px;
    }
    .register-warning {
      background-color: tomato;
      text-align: center;
      padding: 10px;
      width: 60%;
      margin: 0 auto;
      border-radius: 4px;
      color: white;
    }
</style>
