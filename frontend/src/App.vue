<template>
  <div id="app">
    <b-loading :is-full-page="true" v-model="loading"></b-loading>

    <nav
      class="navbar is-mobile is-fixed-top"
      :class="{ 'is-inactive': $route.name == 'home' && !active.navbar }"
    >
      <div class="container is-fluid">
        <div class="navbar-brand">
          <a class="navbar-item" href="/">
            <img src="./assets/images/logo-IO2BC.svg" />
          </a>
        </div>

        <div class="navbar-menu">
          <transition name="fade">
            <div id="menu" v-if="active.menu" class="has-text-centered">
              <div>
                <ul class="is-size-3">
                  <li>
                    <router-link
                      :to="{ name: 'infomedic' }"
                      class="navbar-item"
                    >
                      Ai nevoie de echipament medical?
                    </router-link>
                  </li>
                  <li>
                    <router-link
                      :to="{ name: 'community' }"
                      class="navbar-item"
                    >
                      Donatori
                    </router-link>
                  </li>
                  <!-- <li>
                    <router-link :to="{ name: 'helping' }" class="navbar-item">
                      Vrei să te implici?
                    </router-link>
                  </li> -->
                </ul>

                <b-tooltip
                  position="is-top"
                  type="is-light"
                  size="is-large"
                  multilined
                >
                  <template v-slot:content>
                    Vei fi redirecționat către site-ul <b>Timotion</b>, care
                    pune la dispoziție modalități rapide de donație
                  </template>
                  <!-- <a
                    href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/"
                    class="button is-white is-outlined is-large"
                  >
                    Donează acum
                  </a> -->
                </b-tooltip>
              </div>
            </div>
          </transition>
          <div class="navbar-end">
            <!-- <div class="navbar-item">
              <b-tooltip
                position="is-bottom"
                type="is-light"
                size="is-large"
                multilined
              >
                <template v-slot:content>
                  Vei fi redirecționat către site-ul <b>Timotion</b>, care pune
                  la dispoziție modalități rapide de donație
                </template>
                <a
                  href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/"
                  class="button is-primary is-large is-size-6-mobile"
                >
                  <div>Donează <span class="is-hidden-mobile">acum</span></div>
                </a>
              </b-tooltip>
            </div> -->
            <div class="navbar-item">
              <a
                @click="toggleMenu"
                class="button is-primary is-outlined is-menu"
                :class="{ 'is-active': active.menu }"
              >
                <span v-if="!active.menu">MENIU</span>
                <b-icon v-else icon="times" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div>
      <router-view @loading="loading = $event" />
    </div>

    <div class="container">
      <footer class="footer">
        <div class="columns">
          <div class="column is-4">
            <p class="title">
              Alte resurse
            </p>
            <ul>
              <li>
                <a target="_blank" href="https://covid.municipiulbacau.ro/"
                  >Situația COVID-19 în Bacău</a
                >
              </li>
              <li>
                <a target="_blank" href="https://fiipregatit.ro/"
                  >Ghid situații de urgență</a
                >
              </li>
              <!-- <li>
                <a target="_blank" href="https://www.ctsBacău.ro/"
                  >Centrul regional de transfuzie sanguină</a
                >
              </li> -->
            </ul>
          </div>
          <div class="column is-4">
            <p class="title">
              <br />
            </p>
            <ul>
              <li>
                <a target="_blank" href="https://www.aspjbacau.ro/ "
                  >Direcţia de Sănătate Publică Bacău
                </a>
              </li>
              <li>
                <a target="_blank" href="https://www.cnscbt.ro/"
                  >Centrul National de Supraveghere si Control al Bolilor
                  Transmisibile</a
                >
              </li>
            </ul>
          </div>
          <div class="column is-4">
            <p class="title">
              Press Kit
            </p>

            <a
              href="https://drive.google.com/drive/folders/1JJW_90MWmPv-wyxTaM9JMnwrxfGxKj8z?usp=sharing"
              class="is-size-3 has-text-primary"
              target="_blank"
            >
              <b>Mapă materiale</b><b-icon icon="arrow-right" />
            </a>
          </div>
        </div>
        <div class="columns">
          <div class="column is-12 mt-3 has-text-centered">
            Un concept <a href="https://oxigen.primariatm.ro">
              Oxigen pentru Timișoara
              <p class="mt-3"><img src="./assets/images/Logo_short_O2TM.svg" /></p>
            </a>
          </div>
        </div>

        <!--  <br /><br />
        <p class="title">Urmărește-ne pe</p>
        <a class="is-size-2" href="#"
          ><b-icon pack="fab" icon="facebook-square"
        /></a>
        <a class="is-size-2" href="#"><b-icon pack="fab" icon="instagram"/></a> -->
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data() {
    return {
      active: {
        menu: false,
        navbar: false
      },
      navbarScrollShow: 600,
      loading: false
    }
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll)
  },
  methods: {
    toggleMenu() {
      this.active.menu = !this.active.menu
    },
    onScroll() {
      const currentScrollPosition =
        window.pageYOffset || document.documentElement.scrollTop

      if (currentScrollPosition < 0) {
        return
      }

      this.active.navbar = currentScrollPosition > this.navbarScrollShow
      // this.lastScrollPosition = currentScrollPosition
    }
  },
  watch: {
    $route() {
      this.active.menu = false
    }
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll)
  }
}
</script>
