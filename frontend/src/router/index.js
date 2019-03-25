import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'thequestion' },
  { path: '/restaurants', component: 'restaurants' },
  { path: '/loading', component: 'loading' },
  { path: '/food', component: 'food'}
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
  mode: 'history'
})
