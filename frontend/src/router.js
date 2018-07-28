import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/new',
      name: 'create-item',
      component: () => import('./views/CreateItem.vue')
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/items',
      name: 'my-items',
      component: () => import('./views/MyItems.vue')
    },
    {
      path: '/signin',
      name: 'sign-in',
      components: () => import('./views/SignIn.vue')
    },
    {
      path: '/terms',
      name: 'terms',
      components: () => import('./views/Terms.vue')
    }
  ]
})
