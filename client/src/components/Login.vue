<template>
    <!-- Login main component -->
    <div class="component login-main">

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

        <!-- Login form -->

        <!-- Invalid login credentials -->
        <div v-if="loginWarning" class="login-warning">Invalid login credentials</div>
        <!-- Token expiration -->
        <div v-if="this.$route.params.message" class="login-warning">{{this.$route.params.message}}</div>

        <!-- Successful registration notification -->
        <div v-if="this.$route.params.successfulLogin === true" class="successful-registration">Successfully registered. Please log in</div>

        <div class="login-form-container">
            <form  @submit.prevent="submitLogin()" class="login-form" action="index.html" method="post">
            <div class="login-form-field">
                <!-- Email field -->
                <label for="email">Email</label>
                <input type="text" name="email" id="login-email-field">
            </div>
            <div class="login-form-field">
                <!-- Password field -->
                <label for="password">Password</label>
                <input  autocomplete="off" type="password" name="password" id="login-password-field">
            </div>
            <div class="login-form-field">
                <!-- Submit button -->
                <button name="login-button" id="login-button">Log In</button>
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
            loginWarning: false
        }
    },
    methods: {
    submitLogin() {

        this.loginWarning = false;

        // Gather the login credentials
        const emailField = document.getElementById("login-email-field");
        const passwordField = document.getElementById("login-password-field");
        // Login endpoint
        const API_ENDPOINT = "http://127.0.0.1:5000/login";
        // Package the credentials
        let login = {
            email: emailField.value,
            password: passwordField.value
        }
        // Reset the form fields
        emailField.value = '';
        passwordField.value = '';
        // Instantiate request        
        const request = new Request(API_ENDPOINT, {
          method: 'POST',
          headers: new Headers({
            "Content-Type": "application/json"
          }),
          body: JSON.stringify(login)
        });
        // NOTE: To make the 'this' instance accessible in 
        //       the FETCH code block, it needs to be 
        //       referenced. This might be because the FETCH
        //       scope may have its own 'this' object.
        let self = this;
        // Send the fetch request
        fetch(request)
        .then(function(response) {
            if (response.status === 200) {
                return response.json();
            } else if (response.status === 401) {
                console.log("Invalid login credentials");
                self.loginWarning = true;
            } else {
                throw new Error(response.statusText);
            }
        })
        // Handle a successful login
        .then(function(data) {
            // Store the JWT in the browser's localStorage
            localStorage.setItem('lorenzo-token', data.token);
            // Update user
            self.$store.dispatch('updateUserName', data.username);
            // Reroute the user to the dashboard
            self.$router.push('/dashboard');
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
    /* login general styling */
    .login-main {
        max-width: 90%;
        /* height: 100%; */
        margin: 0 auto;
        padding-top: 30px;
    }
    /* login form styling */
    .login-form-container {
        font-family: Arial;
    }
    .login-form-container .login-form .login-form-field {
        margin: 30px auto;
        width: 80%;
        text-align: center;
    }
    .login-form-container .login-form #login-button {
        padding: 8px;
        width: 50%;
        background-color: rgb(49, 186, 237);
        color: white;
        border-style: none;
        cursor: pointer;
        border-radius: 4px;
        font-size: 1.2em;
    }
    .login-form-container .login-form .login-form-field > input {
        font-size: 1.1em;
        padding: 6px;
    }
    .login-form-field > * {
        display: block;
        margin: 0 auto;
    }
    .login-warning {
        background-color: tomato;
        text-align: center;
        padding: 10px;
        width: 60%;
        margin: 0 auto;
        border-radius: 4px;
        color: white;
    }
    .successful-registration {
        text-align: center;
        padding: 8px;
        background-color: rgb(103, 194, 76);
        border-radius: 4px;
        color: rgb(58, 58, 58);
        width: 85%;
        margin: 0 auto;
    }
</style>