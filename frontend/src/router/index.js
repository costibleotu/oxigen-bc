import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import InfoMedic from '@/views/InfoMedic.vue'
import Community from '@/views/Community.vue'
import Helping from '@/views/Helping.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: ''
    }
  },
  {
    path: '/echipament-medical',
    name: 'infomedic',
    component: InfoMedic,
    meta: {
      title: 'Informații medici și pacienți'
    }
  },
  {
    path: '/comunitate',
    name: 'community',
    component: Community,
    meta: {
      title: 'Comunitate'
    }
  },
  {
    path: '/implica-te',
    name: 'helping',
    component: Helping,
    meta: {
      title: 'Vrei să te implici?'
    }
  }
]

const router = new VueRouter({
  // mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find(r => r.meta && r.meta.title)

  // console.log(nearestWithTitle != null && nearestWithTitle.meta.title)

  document.title =
    'Oxigen pentru Bacău' +
    (nearestWithTitle ? ` - ${nearestWithTitle.meta.title}` : '')

  window.scrollTo(0, 0)

  next()
})

export default router
