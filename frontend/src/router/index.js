import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'
import InfoMedic from '@/views/InfoMedic.vue'
import Community from '@/views/Community.vue'
import Volunteering from '@/views/Volunteering.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: '',
    },
  },
  {
    path: '/ai-nevoie-de-echipament-medical',
    name: 'infomedic',
    component: InfoMedic,
    meta: {
      title: 'Informații medici și pacienți',
    },
  },
  {
    path: '/comunitate',
    name: 'community',
    component: Community,
    meta: {
      title: 'Comunitate',
    },
  },
  {
    path: '/implică-te',
    name: 'volunteering',
    component: Volunteering,
    meta: {
      title: 'Vrei să te implici?',
    },
  },
]

const router = new VueRouter({
  routes,
})

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched
    .slice()
    .reverse()
    .find((r) => r.meta && r.meta.title)

  document.title =
    'Oxigen pentru Timișoara - ' +
    (nearestWithTitle && nearestWithTitle.meta.title)

  window.scrollTo(0, 0)

  next()
})

export default router
