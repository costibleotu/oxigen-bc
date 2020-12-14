import Vue from 'vue'
import VueMq from 'vue-mq'

Vue.use(VueMq, {
  breakpoints: {
    xs: 450,
    sm: 769,
    md: 1080,
    lg: 1232,
    xl: Infinity
  }
})
