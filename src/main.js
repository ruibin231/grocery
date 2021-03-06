// import './common/rem'
import Vue from 'vue'
import App from './app.vue'
import axios from './http'
import router from './router'
import store from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'font-awesome/css/font-awesome.min.css'

Vue.use(ElementUI)

Vue.prototype.axios = axios

new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: {
        App
    }
})
