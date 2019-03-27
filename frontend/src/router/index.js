import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'

var checkDataLoaded = function (to, from, next) {
  console.log('Check data loaded: ' + store.state.loaded)
  if (!store.state.loaded) {
    next('/loading')
  } else {
    next()
  }
}

const routerOptions = [
  { path: '/', component: 'thequestion', beforeEnter: checkDataLoaded },
  { path: '/restaurants', component: 'restaurants', beforeEnter: checkDataLoaded },
  { path: '/loading', component: 'loading' },
  { path: '/food', component: 'food', beforeEnter: checkDataLoaded }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'abstract'
})
