<template>
  <div>
    <div class="container">
      <div class="section head-section">
        <div class="columns">
          <div class="column is-6">
            <img src="../assets/images/Logo_O2TM.svg" class="logo-big" /> <br />
            <h2>
              Solidari în fața Covid-19, donăm
              <span class="has-text-primary">#OxigenPentruTimisoara</span>
            </h2>

            <div class="content">
              <br />
              <p>
                Primăria Timișoara, ONG-uri, voluntari și antreprenori și-au
                unit forțele pentru a sprijini spitalele și comunitatea în fața
                pandemiei de coronavirus. Fiecare dintre noi are puterea de a
                crește resursele cu care medicii salvează vieți. Fiecare dintre
                noi are puterea de a dona respirațiile prețioase de care au
                nevoie pacienții în drumul lor spre vindecare.
              </p>
              <p>
                <b>
                  Cu fiecare respirație suntem mai aproape de a ieși cu bine din
                  pandemie. Împreună.
                </b>
              </p>
            </div>

            <div class="buttons">
              <b-tooltip
                position="is-top"
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
                  class="button is-primary"
                >
                  Donează acum
                </a>

                <span class="is-hidden"></span>
              </b-tooltip>

              <!-- <router-link
                :to="{ name: 'infomedic' }"
                class="button is-primary is-outlined"
              >
                Informații medici și pacienți
              </router-link> -->
            </div>
          </div>
          <div class="column is-6">
            <div id="animation-scene" class="has-text-weight-bold"></div>
          </div>
        </div>
      </div>

      <div class="section">
        <div class="columns is-variable is-8">
          <div class="column is-4">
            <h1 class="is-spaced">De ce este nevoie?</h1>
          </div>
          <div class="column is-6">
            <div class="content">
              <p>
                Pulsoximetrele și concentratoarele de oxigen sunt extrem de
                necesare în monitorizarea și tratamentul pacienților Covid.
                Atunci când bolnavii cu cazuri medii sunt tratați acasă (pentru
                degrevarea spitalelor), iar cei externați sunt în perioada de
                convalescență, este esențial accesul la pulsoximetre și
                concentratoare de oxigen mobile, la cererea medicului de
                familie.
              </p>
              <p>
                <b>
                  Acest serviciu se poate dezvolta doar cu susținerea și
                  implicarea comunității.
                </b>
              </p>
            </div>
          </div>
        </div>

        <br />
        <div class="columns">
          <div class="column" v-if="data">
            <div class="columns is-multiline columns-progress is-variable is-8">
              <div
                v-for="need in data.needs"
                :key="`need-${need.id}`"
                class="column is-6-tablet is-4-desktop"
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

      <!-- <div class="section is-small">
        <div class="box">
          <div class="columns is-centered">
            <div
              class="column is-11-tablet is-10-desktop is-8-fullhd has-text-left-mobile has-text-centered"
            >
              <h2>Ai nevoie de echipament medical?</h2>
              <div class="content">
                Medicul tău de familie este legătura ta cu comunitatea medicală
                și resursele de suport disponibile. Vezi cum poți intra în
                posesia echipamentelor medicale.
              </div>

              <router-link
                :to="{ name: 'infomedic' }"
                class="button is-primary is-outlined"
              >
                Informații medici și pacienți
              </router-link>
            </div>
          </div>
        </div>
      </div> -->

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

          <div class="content">
            Soluțiile de durată se pot dezvolta doar acolo unde ne reunim
            forțele în mod constant. Crizele ne-au arătat mereu valoarea
            comunității noastre, însă este momentul să construim împreună pentru
            viitor, pentru o comunitate timișoreană funcțională, sustenabilă,
            dincolo de urgențe.
          </div>
        </div>
      </div>
    </div>

    <div class="has-background-light">
      <div class="container">
        <div class="section">
          <div class="columns">
            <div class="column"><h1>Suntem o comunitate</h1></div>
            <div class="column is-narrow">
              <router-link :to="{ name: 'community' }">
                Vezi toți donatorii<b-icon icon="arrow-right" />
              </router-link>
            </div>
          </div>

          <div class="columns">
            <div class="column is-4">
              <div class="content">
                Fiecare dintre noi are puterea de a spori resursele cu care
                medicii salvează vieți. Fiecare dintre noi are puterea de a dona
                respirațiile prețioase de care au nevoie pacienții în drumul lor
                spre vindecare.
              </div>
            </div>
          </div>

          <br />

          <div class="columns is-multiline is-centered" v-if="data">
            <div class="column is-4-widescreen">
              <h3>{{ data.campaign.companies_count }} companii</h3>

              <div
                class="carousel-container company has-text-centered has-background-white"
              >
                <p><b>Cele mai recente sponsorizări</b></p>
                <br /><br />

                <b-carousel
                  v-bind="{
                    interval: 2230,
                    pauseInfo: false,
                    arrowHover: false,
                    indicatorStyle: 'is-lines'
                  }"
                >
                  <b-carousel-item
                    v-for="(company, index) in data.companies.slice(0, 5)"
                    :key="index"
                  >
                    <figure class="image is-square">
                      <img :src="company.logo" v-if="company.logo" />
                      <img
                        src="../assets/images/Placeholder_Sponsor.png"
                        v-else
                      />
                    </figure>

                    <p class="title">
                      <b>{{ company.display_name }}</b>
                    </p>
                    <p>{{ company.amount | currency }}</p>
                  </b-carousel-item>
                </b-carousel>
              </div>

              <p>
                <a
                  target="_blank"
                  href="https://drive.google.com/file/d/1uYpkLREE7bSgcyFSNteXxrREelinv_4a/view?usp=sharing"
                >
                  Model contract sponsorizare<b-icon icon="arrow-right" />
                </a>
              </p>
            </div>
            <div class="column is-12-tablet is-8-widescreen">
              <h3>{{ data.campaign.donors_count }} cetățeni</h3>
              <div class="carousel-container quotes">
                <b-carousel
                  v-bind="{
                    autoplay: false,
                    arrowHover: false,
                    indicatorStyle: 'is-lines'
                  }"
                >
                  <b-carousel-item
                    v-for="(quote, index) in data.quotes"
                    :key="index"
                  >
                    <p
                      class="content has-text-weight-semibold is-size-5-touch is-size-4-desktop"
                      v-html="quote.comment"
                    ></p>

                    <b-icon icon="quote-left" />
                    <br />
                    <b>{{ quote.name }}</b>
                  </b-carousel-item>
                </b-carousel>
              </div>

              <!-- <p class="has-text-right">
              <router-link :to="{}">
                Trimite un gând bun<b-icon icon="arrow-right" />
              </router-link>
            </p> -->
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="section">
        <h1>Despre noi</h1>

        <div class="columns">
          <div class="column is-10-tablet is-4-desktop">
            <div class="content">
              Primăria Timișoara, ONG-uri timișorene active în comunitate,
              voluntari și antreprenori și-au unit forțele pentru sprijini
              spitalele și comunitatea în fața pandemiei de coronavirus.
            </div>
          </div>
        </div>

        <br />

        <h2>Parteneri</h2>
        <GridBoxes v-if="data" :data="data.partners" />

        <br />

        <h2>Parteneri media</h2>
        <GridBoxes v-if="data" :data="data.media_partners" />
      </div>

      <div class="section">
        <div class="box has-background-light">
          <h2 class="has-text-centered">Întrebări frecvente</h2>
          <br />

          <div class="columns is-gapless is-centered">
            <div class="column is-11-tablet is-8-desktop">
              <HomeFAQ v-if="data" :data="data.faqs" />
            </div>
          </div>
        </div>
      </div>

      <div class="section">
        <h1>Alte campanii</h1>

        <div class="columns">
          <div class="column is-4">
            <div class="content">
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

              <div class="content">
                Nevoia de sânge este permanentă. Centrul Regional de Transfuzie
                Sanguină Timișoara apelează la sprijinul comunității pentru
                asigurarea necesarului de sânge pentru tratarea cazurilor grave.
              </div>

              <a
                href="https://oxigen.primariatm.ro/media/Promovare_donare_sange_1.pdf"
                class="button is-primary is-large"
                target="_blank"
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

              <div class="content">
                Plasma este o șansă la viață pentru bolnavii cu forme grave de
                Covid-19. Trei orașe — Cluj, Sibiu și Timișoara — și-au unit
                eforturile pentru ca anul acesta, de Crăciun, să oferim cel mai
                frumos cadou: o șansă.
              </div>

              <a
                href="https://oxigen.primariatm.ro/media/Promovare_donare_plasma.pdf"
                class="button is-primary is-large"
                target="_blank"
              >
                Vezi campania
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
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
            cellClass: 'has-text-weight-bold'
          },
          {
            field: 'quantity',
            sortable: false,
            label: 'Achiziție',
            centered: true,
          },
          {
            field: 'price',
            sortable: false,
            label: 'Valoare',
            cellClass: 'has-text-weight-bold',
            centered: true,
          },
          // {
          //   field: 'available',
          //   sortable: false,
          //   label: 'Disponibile',
          //   centered: true,
          //   cellClass: 'has-text-success has-text-weight-bold'
          // },
          // {
          //   field: 'in_use',
          //   sortable: false,
          //   label: 'Utilizate',
          //   centered: true,
          //   cellClass: 'has-text-primary has-text-weight-bold'
          // }
        ]
      }
    }
  },
  mounted() {
    this.getData()
  },
  beforeDestroy() {
    oxigen_animation.stop()
  },
  methods: {
    getData() {
      this.$emit('loading', true)

      ApiService.get('dashboard/').then(response => {
        this.data = response

        this.initAnimation().then(() => this.$emit('loading', false))
      })
    },

    initAnimation() {
      oxigen_animation.init({
        element: document.querySelector('#animation-scene'),
        total_necesar: this.data.campaign.target
      })
      oxigen_animation.update({
        total_strans: this.data.campaign.amount_collected,
        donatori: this.data.campaign.donations
      })

      return ApiService.get('named-donors/').then(response => {
        oxigen_animation.animate(
          response
            .filter(e => !e.is_company)
            .map(e => {
              return { nume: e.display_name, suma: e.amount }
            })
        )
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.head-section {
  padding-bottom: 0;

  @include tablet {
    padding-top: 0;
  }

  .logo-big {
    max-width: 250px;
    margin-bottom: 40px;

    @include desktop {
      margin-bottom: 80px;
      max-width: 320px;
      width: 60%;
    }
  }

  #animation-scene {
    @include mobile {
      width: 670px;
      transform: translateX(-35%);
    }

    @include desktop {
      /deep/ svg {
        margin-right: -40px;
      }
    }
  }

  h2 > span {
    @include mobile {
      font-size: 22px;
    }
  }
}

.button-pulse {
  width: 90px;
  height: 90px;
  animation: pulse 2.5s infinite cubic-bezier(0.66, 0, 0, 1);

  margin-bottom: 30px;

  @include desktop {
    float: right;
    /*left: -80px;*/
    margin-bottom: 0;
  }

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

.columns-progress {
  .column {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }
}
</style>
