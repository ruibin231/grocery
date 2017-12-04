import Vue from 'vue'
import Router from 'vue-router'
import Base from 'pages/Base'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '首页',
      component: Base
    }
  ]
})
