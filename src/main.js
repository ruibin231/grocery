import Vue from 'vue'
import App from './app.vue'
import axios from './http'
import router from './router'

new Vue({
    el: '#app',
    axios,
    router,
    template: '<App/>',
    components: {
      App
    }
})