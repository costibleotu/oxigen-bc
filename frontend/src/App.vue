<template>
  <div id="app">
    <nav
      class="navbar is-mobile is-fixed-top"
      :class="{ 'is-inactive': $route.name == 'home' && !active.navbar }"
    >
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item" href="/">
            <h1><span class="has-text-primary is-size-2">O2</span>TM</h1>
            <img
              style="display: none"
              src="https://bulma.io/images/bulma-logo.png"
            />
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
                  <li>
                    <router-link
                      :to="{ name: 'helping' }"
                      class="navbar-item"
                    >
                      Vrei să te implici?
                    </router-link>
                  </li>
                </ul>

                <a
                  href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/"
                  class="button is-white is-outlined is-large"
                >
                  Donează acum
                </a>
              </div>
            </div>
          </transition>
          <div class="navbar-end">
            <div class="navbar-item">
              <a
                href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/"
                class="button is-primary is-large"
              >
                Donează acum
              </a>
            </div>
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
      <router-view />
    </div>

    <div class="container">
      <footer class="footer">
        <div class="columns">
          <div class="column is-3">
            <p class="title">
              Alte resurse
            </p>

            <ul>
              <li><a href="#">www.timotion.ro</a></li>
              <li><a href="#">Primăria Timișoara</a></li>
              <li><a href="#">Contactează-ne</a></li>
            </ul>
          </div>
          <div class="column is-3">
            <p class="title">
              Alte resurse
            </p>

            <ul>
              <li><a href="#">www.timotion.ro</a></li>
              <li><a href="#">Primăria Timișoara</a></li>
              <li><a href="#">Contactează-ne</a></li>
            </ul>
          </div>
          <div class="column is-4">
            <p class="title">
              Press Kit
            </p>

            <p>Distribuie nostru folosind materialele noastre promotionale</p>
            <br />

            <a href="#" class="is-size-3 has-text-primary">
              <b>Folder materiale</b><b-icon icon="arrow-right" />
            </a>
          </div>
        </div>

        <br /><br />
        <p class="title">Urmărește-ne pe</p>
        <a class="is-size-2" href="#"
          ><b-icon pack="fab" icon="facebook-square"
        /></a>
        <a class="is-size-2" href="#"><b-icon pack="fab" icon="instagram"/></a>
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
      }
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

      this.active.navbar = currentScrollPosition > 300
      // this.lastScrollPosition = currentScrollPosition
    }
  },
  watch: {
    '$route'() {
      this.active.menu = false
    }
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll)
  }
}
</script>
