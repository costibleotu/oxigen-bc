import Vue from 'vue'
import VueMq from 'vue-mq'

Vue.use(VueMq, {
  breakpoints: {
    sm: 769,
    md: 1080,
    lg: 1440,
    xl: Infinity
  }
})
