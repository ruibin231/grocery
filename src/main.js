// import './common/rem'
import Vue from 'vue'
import App from './app.vue'
import axios from './http'
import router from './router'
import Vant from 'vant'
import 'vant/lib/vant-css/index.css'

Vue.use(Vant)

new Vue({
    el: '#app',
    axios,
    router,
    template: '<App/>',
    components: {
        App
    }
})

// new Vue({
//     router,
//     el: '#app',
//     render: h => h(App)
// });