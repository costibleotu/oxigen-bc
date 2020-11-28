import Vue from 'vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowRight, faArrowUp, faQuoteLeft } from '@fortawesome/free-solid-svg-icons'

import {
  faFacebookSquare,
  faInstagram
} from '@fortawesome/free-brands-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faArrowRight, faArrowUp, faQuoteLeft, faFacebookSquare, faInstagram)
Vue.component('vue-fontawesome', FontAwesomeIcon)

import {
  Button,
  Carousel,
  Icon,
  Progress,
  Table,
  Toast,
  ConfigProgrammatic
} from 'buefy'

// Components
Vue.use(Button)
Vue.use(Carousel)
Vue.use(Icon)
Vue.use(Progress)
Vue.use(Table)
Vue.use(Toast)

ConfigProgrammatic.setOptions({
  defaultTrapFocus: true,
  defaultUseHtml5Validation: false,

  defaultIconComponent: 'vue-fontawesome',
  defaultIconPack: 'fas'
})
