import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ApiService from '@/services/api'

import './buefy'
import './vue-mq'
import './assets/style/base.scss'

const API_PATH = 'https://oxigen.primariatm.ro/api/'
ApiService.init(API_PATH)

// filters

let currencyFormatter = new Intl.NumberFormat('ro-RO', {
  // style: 'currency',
  // currency: 'RON',
  // currencyDisplay: 'symbol'
})

Vue.filter('currency', function(value) {
  if (!value) return '0'
  return currencyFormatter.format(String(value)) + ' lei'
})

Vue.filter('striptags', function(value) {
  return value.replace(/(<([^>]+)>)/gi, "");
})

//

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
