<template>
  <div class="container">
    <div class="section head-section">
      <div class="columns">
        <div class="column is-6">
          <div class="box">@TODO: LOGO BIG <br /></div>
          <h2>
            Solidari în fața Covid-19, donăm
            <span class="has-text-primary">#OxigenPentruTimisoara</span>
          </h2>

          <div class="content is-small">
            <br />
            <p>
              Primăria Timișoara, ONG-uri timișorene active în comunitate,
              voluntari și antreprenori și-au unit forțele pentru a sprijini
              spitalele și comunitatea în fața pandemiei de coronavirus. <br />
              Fiecare dintre noi are puterea de a spori resursele cu care
              medicii salvează vieți. Fiecare dintre noi are puterea de a dona
              respirațiile prețioase de care au nevoie pacienții în drumul lor
              spre vindecare.
            </p>
            <p class="has-text-weight-bold">
              Cu fiecare respirație suntem mai aproape de a ieși cu bine din
              pandemie. Împreună.
            </p>
          </div>

          <div class="buttons">
            <a
              href="https://www.timotion.ro/proiecte-2020/solidari-in-fata-covid-19/"
              class="button is-primary"
            >
              Donează acum
            </a>
            <router-link
              :to="{ name: 'infomedic' }"
              class="button is-primary is-outlined"
            >
              Informații medici și pacienți
            </router-link>
          </div>
        </div>
        <div class="column is-6">
          <div id="animation-scene" class="has-text-weight-bold"></div>
        </div>
      </div>
    </div>

    <div class="section">
      <h1 class="is-spaced">De ce este nevoie?</h1>
      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            <p>
              Oxigen pentru Timișoara își propune să vină în sprijinul
              comunității prin prioritizarea nevoilor în mai multe etape
              adaptate contextului pandemic în care ne aflăm.
              <br />Astfel în prima etapă urgența este reprezentată de
              achiziționarea de instalații de oxigen, concentratoare de oxigen
              și pulsoximetre, extrem de necesare pentru tratarea la domiciliu,
              sub supravegherea medicilor de familie, a pacienților infectați cu
              coronavirus, dar și pentru recuperarea ulterioară a pacienților,
              după depășirea fazei critice. Avem nevoie de donațiile voastre
              pentru ca aceste dispozitive medicale a ajunge la cât mai mulți
              timișoreni.
            </p>
          </div>

          <router-link :to="{ name: 'infomedic' }">
            Ai nevoie de suport medical?<b-icon icon="arrow-right" />
          </router-link>
        </div>

        <div class="column" v-if="data">
          <div class="columns is-multiline">
            <div
              v-for="need in data.needs"
              :key="`need-${need.id}`"
              class="column is-6"
            >
              <HomeProgress
                :title="need.name"
                :value="need.stock"
                :max="need.quantity"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="columns" v-if="data">
        <div class="column is-4">
          <h2>Ce s-a reușit până acum</h2>

          <p class="is-size-2">
            <b>{{ data.campaign.donors_count }}</b>
          </p>
          Donații individuale
          <h2 class="has-text-primary currency">
            {{ data.campaign.donors_sum | currency }}
          </h2>
          <br />

          <p class="is-size-2">
            <b>{{ data.campaign.companies_count }}</b>
          </p>
          Companii
          <h2 class="has-text-primary currency">
            {{ data.campaign.companies_sum | currency }}
          </h2>
        </div>
        <div class="column">
          <b-table
            v-if="data && data.expenses"
            :data="data.expenses"
            :columns="tablecolumns.expenses"
            class="is-size-4"
          ></b-table>
        </div>
      </div>
    </div>

    <hr />

    <div class="section">
      <div class="has-text-centered">
        <router-link
          :to="{ name: 'helping' }"
          class="button button-pulse is-primary is-size-1"
        >
          <b-icon icon="arrow-right" />
        </router-link>

        <h2>Vrei să te implici?</h2>

        <div class="content is-small">
          Motivatie pentru publicul larg sa se implice in actiunea demarata de
          Primarie + ONGs.
        </div>
      </div>
    </div>

    <div class="section">
      <h1>Suntem o comunitate</h1>
      <router-link :to="{ name: 'community' }">
        Vezi toți donatorii<b-icon icon="arrow-right" />
      </router-link>

      <br /><br />

      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            Fiecare dintre noi are puterea de a spori resursele cu care medicii
            salvează vieți. Fiecare dintre noi are puterea de a dona
            respirațiile prețioase de care au nevoie pacienții în drumul lor
            spre vindecare.
          </div>
        </div>
      </div>

      <div class="columns" v-if="data">
        <div class="column is-4">
          <h3>{{ data.campaign.companies_count }} companii</h3>

          <div class="carousel-container company has-text-centered">
            <p><b>Cele mai recente sponsorizări</b></p>
            <br /><br />

            <b-carousel
              v-bind="{
                autoplay: false,
                arrowHover: false,
                indicatorStyle: 'is-lines',
              }"
            >
              <b-carousel-item
                v-for="(company, index) in data.companies.slice(0, 5)"
                :key="index"
              >
                <figure class="image is-square">
                  <img :src="company.logo" alt="" />
                </figure>

                <p class="title">
                  <b>{{ company.display_name }}</b>
                </p>
                <p>{{ company.amount | currency }}</p>
              </b-carousel-item>
            </b-carousel>
          </div>

          <p>
            <router-link :to="{}">
              Model contract sponsorizare<b-icon icon="arrow-right" />
            </router-link>
          </p>
        </div>
        <div class="column">
          <h3>{{ data.campaign.donors_count }} cetățeni</h3>
          <div class="carousel-container quotes">
            <b-carousel
              v-bind="{
                autoplay: false,
                arrowHover: false,
                indicatorStyle: 'is-lines',
              }"
            >
              <b-carousel-item
                v-for="(quote, index) in data.quotes"
                :key="index"
              >
                <h2 class="content has-text-weight-semibold is-italic">
                  {{ quote.comment }}
                </h2>

                <b-icon icon="quote-left" />
                <br />
                <b>{{ quote.name }}</b>
              </b-carousel-item>
            </b-carousel>
          </div>

          <p class="has-text-right">
            <router-link :to="{}">
              Trimite un gând bun<b-icon icon="arrow-right" />
            </router-link>
          </p>
        </div>
      </div>
    </div>

    <div class="section">
      <h1>Despre noi</h1>

      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            Primăria Timișoara, ONG-uri timișorene active în comunitate,
            voluntari și antreprenori și-au unit forțele pentru sprijini
            spitalele și comunitatea în fața pandemiei de coronavirus.
          </div>
        </div>
      </div>

      <br />

      <h2>Parteneri</h2>
      <GridBoxes v-if="data" :data="data.partners" />

      <h2>Parteneri media</h2>
      <GridBoxes v-if="data" :data="data.media_partners" />
    </div>

    <div class="section">
      <div class="container box has-background-light">
        <h2 class="has-text-centered">Întrebări frecvente</h2>
        <br />

        <div class="columns is-gapless is-centered">
          <div class="column is-8">
            <HomeFAQ v-if="data" :data="data.faqs" />
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <h1>Alte campanii</h1>

      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            Alte campanii similare in lupta cu COVID-19.
          </div>
        </div>
      </div>

      <div class="columns">
        <div class="column is-6">
          <div class="box">
            <h1 class="has-text-primary">
              Donează sânge
            </h1>

            <div class="content is-small">
              Primăria Timișoara, ONG-uri timișorene active în comunitate,
              voluntari și antreprenori și-au unit forțele pentru sprijini
              spitalele și comunitatea în fața pandemiei de coronavirus.
            </div>

            <a
              href="https://oxigen.primariatm.ro/media/Promovare_donare_sange_1.pdf"
              class="button is-primary is-large"
            >
              Vezi campania
            </a>
          </div>
        </div>
        <div class="column is-6">
          <div class="box">
            <h1 class="has-text-primary">
              Donează plasmă
            </h1>

            <div class="content is-small">
              Plasma este o șansă la viață pentru bolnavii cu forme grave de
              Covid-19. Trei orașe — Cluj, Sibiu și Timișoara — și-au unit
              eforturile pentru ca anul acesta, de Crăciun, să oferim cel mai
              frumos cadou: o șansă.
            </div>

            <a
              href="https://oxigen.primariatm.ro/media/Promovare_donare_plasma.pdf"
              class="button is-primary is-large"
            >
              Vezi campania
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="section"></div>
  </div>
</template>

<script>
import GridBoxes from '@/components/GridBoxes'
import HomeProgress from '@/components/HomeProgress'
import HomeFAQ from '@/components/HomeFAQ'

import ApiService from '@/services/api'
import * as oxigen_animation from 'oxigen-animation'

export default {
  name: 'Home',
  components: { GridBoxes, HomeProgress, HomeFAQ },
  data() {
    return {
      data: null,
      tablecolumns: {
        expenses: [
          {
            field: 'name',
            sortable: false,
            label: 'Necesar',
            cellClass: 'has-text-weight-bold',
          },
          {
            field: 'price',
            sortable: false,
            label: 'Valoare',
          },
          {
            field: 'quantity',
            sortable: false,
            label: 'Achizitie',
            centered: true,
            cellClass: 'has-text-weight-bold',
          },
          {
            field: 'available',
            sortable: false,
            label: 'Disponibile',
            centered: true,
            cellClass: 'has-text-success has-text-weight-bold',
          },
          {
            field: 'in_use',
            sortable: false,
            label: 'Utilizate',
            centered: true,
            cellClass: 'has-text-primary has-text-weight-bold',
          },
        ],
      },
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      ApiService.get('dashboard/').then((response) => {
        this.data = response
        this.initAnimation()
      })
    },

    initAnimation() {
      window.addEventListener('load', () => {
        oxigen_animation.init({
          element: document.querySelector('#animation-scene'),
          total_necesar: this.data.campaign.target,
        })
        oxigen_animation.update({
          total_strans: this.data.campaign.amount_collected,
          donatori: this.data.campaign.donations,
        })
        oxigen_animation.animate({
          suma: 2,
          nume: 'Alex',
        })
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.head-section {
  padding-bottom: 0;
}

.button-pulse {
  position: relative;
  width: 90px;
  height: 90px;
  float: right;
  left: -80px;
  animation: pulse 2.5s infinite cubic-bezier(0.66, 0, 0, 1);

  .icon {
    transform: rotate(-45deg);
  }

  &:after {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    animation: pulse-big 2.5s infinite cubic-bezier(0.3, 0, 0, 1);
  }

  &,
  &:after {
    border-radius: 100%;
    box-shadow: 0 0 0 0 rgba(225, 10, 20, 0.45);
  }
}

.currency {
  margin-top: 10px;
}

nav.navbar {
}
</style>
