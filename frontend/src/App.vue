<template>
  <div id="app">
    <nav class="navbar is-fixed-top">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item" href="/">
            <img src="https://bulma.io/images/bulma-logo.png" />
          </a>
        </div>

        <div class="navbar-menu">
          <div class="navbar-end">
            <div class="navbar-item">
              <a href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/" class="button is-primary is-large">Donează acum</a>
            </div>
            <div class="navbar-item">
              <a
                href=""
                class="button is-primary is-outlined is-menu has-text-weight-normal"
                >@TODO: MENIU</a
              >
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
  components: {}
}
</script>
