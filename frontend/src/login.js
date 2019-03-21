import Vue from 'vue'
import LoginApp from './LoginApp'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#loginApp',
  render: h => h(LoginApp)
});
