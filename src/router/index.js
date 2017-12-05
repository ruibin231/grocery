import Vue from 'vue'
import Router from 'vue-router'
import Base from 'pages/Base'
import PropertyList from 'pages/PropertyList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '首页',
      component: Base,
      redirect: '/home',
      children: [
      	{path: 'home', component: PropertyList, name: '资产列表'}
      ]
    }
  ]
})
