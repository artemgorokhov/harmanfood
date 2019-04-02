import Vue from 'vue'
import App from './App'
import router from './router'
import store from '@/store'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})

router.replace('/')

// TODO: install and configure vuejs-logger https://www.npmjs.com/package/vuejs-logger
// TODO: use .env for different development phases https://cli.vuejs.org/ru/guide/mode-and-env.htm
