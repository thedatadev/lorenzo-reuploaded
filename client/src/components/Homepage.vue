<template>
    <div class="component homepage-main">
        <!-- Homepage header -->
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

        <!-- Homepage navigation -->
        <!-- <div v-if="isAuthenticated" class="homepage-nav">
            <router-link class="dashboard-btn button" :to="{name: 'Register'}" >Dashboard</router-link>
            <a href="" class="logout-btn button" v-on:click.prevent="logout">Log out</a>
        </div>
        <div v-if="!isAuthenticated" class="homepage-nav">
            <router-link class="register-btn button" :to="{name: 'Register'}" >Register</router-link>
            <router-link class="login-btn button" :to="{name: 'Login'}" >Login</router-link>
        </div> -->

        <div class="homepage-nav">
            <span class="nav-elem label">Register a new account</span>
            <router-link class="nav-elem register-btn button" :to="{name: 'Register'}" >Register</router-link>
        
            <span class="nav-elem label">Already have an account?</span>
            <router-link class="nav-elem login-btn button" :to="{name: 'Login'}" >Login</router-link>
        </div>

        
        
    </div>
</template>

<script>
export default {
    name: 'Homepage',
    methods: {
        isMobile(mq) {
            return mq === "sm";
        },
        isAuthenticated() {
            const token = localStorage.getItem("lorenzo-token");
            return token !== null;
        },
        logout() {
            localStorage.removeItem("lorenzo-token");
            this.$router.push("/");
        }
  }
}
</script>

<style>
    /* homepage general styling */
    .homepage-main {
        max-width: 90%;
        margin: 0 auto;
        padding-top: 75px;
    }
    /* general homepage nav styling */
    .homepage-nav {
        display: block;
        margin: 20px auto;
        width: 60%;
    }
    .homepage-nav > .nav-elem {
        display: block;
    }
    .homepage-nav > .label {
        color: #222;
        font-family: Arial, Helvetica, sans-serif;
        margin-bottom: 6px;
    }
    .homepage-nav > a {
        background-color: #eee;
        margin-bottom: 20px;
        text-decoration: none;
        text-align: center;
        padding: 6px;
        border-radius: 4px;
        font-family: Arial;
        color: #fff;
    }
    /* register button */
    .homepage-nav .register-btn {
        background-color: rgb(42, 219, 166);
    }

    /* login button */
    .homepage-nav .login-btn {
        background-color:#417be0;
    }


    /* dashboard button */



    /* logout button */


</style>
