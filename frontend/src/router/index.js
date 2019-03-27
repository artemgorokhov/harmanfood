import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'

import Home from '@/components/home.vue'
import TheQuestion from '@/components/thequestion.vue'
import Restaurants from '@/components/restaurants.vue'
import Food from '@/components/food.vue'
import Loading from '@/components/loading.vue'

var checkDataLoaded = function (to, from, next) {
  console.log('Check data loaded: ' + store.state.loaded)
  if (!store.state.loaded) {
    next('/loading')
  } else {
    next()
  }
}

const routes = [
  { path: '/', component: TheQuestion, beforeEnter: checkDataLoaded },
  { path: '/home', component: Home, beforeEnter: checkDataLoaded,
    children: [
      { path: 'restaurants', component: Restaurants },
      { path: 'food', component: Food }
    ] },
  { path: '/loading', component: Loading }
]

Vue.use(Router)

export default new Router({
  routes,
  mode: 'abstract'
})
