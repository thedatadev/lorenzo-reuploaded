// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueChatScroll from 'vue-chat-scroll'
import VueMq from 'vue-mq'
import { store } from './store/store'

Vue.use(VueMq, {
  breakpoints: { // default breakpoints - customize this
    sm: 767,
    // sm: 450,
    md: 1250,
    lg: Infinity,
  }
})


Vue.use(VueChatScroll)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store: store,
  components: { App },
  template: '<App/>'
})
