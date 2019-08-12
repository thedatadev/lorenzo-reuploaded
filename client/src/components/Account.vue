<template>
    <!-- Main container -->
      <div class="component account-container">


        <!-- Header -->
        <div class="header">
          <a href="#" class="back" v-on:click.prevent="goBack">
            <i class="fas fa-arrow-left"></i>
          </a>
          <div class="title">Account</div>
          <div class='logout-btn' v-on:click.prevent="logOut">Logout</div>
        </div>

        <!-- Account main -->
        <div class="account-main">
          <!-- Account update form -->
          <div class="account-update-form">
            <!-- Account email -->
            <div class="account-form-label" for="account-email">Email</div>
            <input class="account-form-value" type="text" id="account-email" value="edrian123@gmail.com">
            <!-- Account username -->
            <div class="account-form-label" for="account-username">Username</div>
            <input class="account-form-value" type="text" id="account-username" value="edrian">
            <!-- Account password -->
            <div class="account-form-label" for="account-new-password">New password</div>
            <input class="account-form-value" type="password" id="account-new-password" value="edrian123">
            <!-- Account confirm password -->
            <div class="account-form-label" for="account-confirm-password">Confirm password</div>
            <input class="account-form-value" type="password" id="account-confirm-password" value="">
          </div>
          <!-- Account update button -->
          <a href="#" id="account-update-btn" @click.prevent="unimplementedNotification">Update account</a>
        </div>

      </div> <!-- END Main container -->
</template>

<script>
export default {
    name: 'Account',
    methods: {
      goBack() {
        this.$router.go(-1);
      },
      logOut() {
        localStorage.removeItem('lorenzo-token');
        this.$router.push('/');
      },
      unimplementedNotification() {
        alert("Sorry, account updates have not been implemented.");
      }
    }
}
</script>

<style>
/* Account-main styling */
.account-main {
  width: 60%;
  margin: 0 auto;
  margin-top: 50px;
  /* text-align: center; */
}
.account-main > div {
  margin: 0 auto;
  width: 80%;
}
.account-main .account-update-form .account-form-label {
  margin-top: 20px;
  color: rgb(71, 205, 173);
  font-size: 1.3em;
}
.account-main .account-update-form .account-form-value {
  margin-top: 8px;
  font-size: 1.1em;
  padding: 8px;
  border-style: none;
  border-bottom: 2px solid rgb(209, 219, 215);
}
.account-main .account-update-form .account-form-value:focus {
  outline: none;
  border-bottom-color: rgb(56, 168, 141);
}
.account-main .account-update-form > input:focus {
  outline: none;
}
#account-update-btn {
  display: block;
  margin: 30px auto 0;
  width: 60%;
  color: white;
  background-color: tomato;
  padding: 10px;
  border-radius: 6px;
  text-align: center;
  box-shadow: 0 2px 7px rgb(194, 201, 197);
}
.logout-btn {
  background-color: tomato;
  padding: 10px;
  color: white;
  cursor: pointer;
}
</style>
