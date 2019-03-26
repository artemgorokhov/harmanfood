import Vue from 'vue'
import App from './App'
import router from './router'
import HF from './assets/js/hfplugin/hf-plugin'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

Vue.use(HF)

router.replace('/')
