import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ApiService from '@/services/api'

import './buefy'
import './vue-mq'
import './assets/style/base.scss'

ApiService.init(process.env.VUE_APP_ROOT_API)

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
  return value.replace(/(<([^>]+)>)/gi, '')
})

//

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
