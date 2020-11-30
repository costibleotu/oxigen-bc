import Vue from 'vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faAngleLeft,
  faAngleRight,
  faArrowRight,
  faArrowUp,
  faQuoteLeft,
  faQuestionCircle,
  faTimes
} from '@fortawesome/free-solid-svg-icons'

import {
  faFacebookSquare,
  faInstagram
} from '@fortawesome/free-brands-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(
  faAngleLeft,
  faAngleRight,
  faArrowRight,
  faArrowUp,
  faQuoteLeft,
  faQuestionCircle,
  faTimes,
  faFacebookSquare,
  faInstagram
)
Vue.component('vue-fontawesome', FontAwesomeIcon)

import {
  Button,
  Carousel,
  ConfigProgrammatic,
  Collapse,
  Icon,
  Progress,
  Table,
  Toast,
  Tooltip
} from 'buefy'

// Components
Vue.use(Button)
Vue.use(Carousel)
Vue.use(Collapse)
Vue.use(Icon)
Vue.use(Progress)
Vue.use(Table)
Vue.use(Toast)
Vue.use(Tooltip)

ConfigProgrammatic.setOptions({
  defaultTrapFocus: true,
  defaultUseHtml5Validation: false,

  defaultIconComponent: 'vue-fontawesome',
  defaultIconPack: 'fas'
})
