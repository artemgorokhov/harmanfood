import Vue from 'vue'
import App from './App'
import router from './router'
import store from '@/store'
import socket from '@/socket'
import Scrollspy, { Easing } from 'vue2-scrollspy'


Vue.config.productionTip = false

Vue.use(socket)

Vue.use(Scrollspy, {
    easing: Easing.Quartic.InOut
})

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
