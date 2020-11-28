<template>
  <div class="container">
    <div class="section">
      <div class="columns">
        <div class="column is-5">
          <div class="box">@TODO: LOGO BIG <br /></div>
          <h2>
            Solidari în fața Covid-19, donăm
            <span class="has-text-primary">#OxigenPentruTimisoara</span>
          </h2>

          <div class="content is-small">
            <br />
            <p>
              Primăria Timișoara, ONG-uri, voluntari și antreprenori și-au unit
              forțele pentru a sprijini spitalele și comunitatea în fața
              pandemiei de coronavirus. Fiecare dintre noi are puterea de a
              spori resursele cu care medicii salvează vieți.
            </p>
            <p class="has-text-weight-bold">
              Cu fiecare respirație suntem mai aproape de a ieși cu bine din
              pandemie. Împreună.
            </p>
          </div>

          <div class="buttons">
            <router-link :to="{}" class="button is-primary">
              Donează acum
            </router-link>
            <router-link
              :to="{ name: 'infomedic' }"
              class="button is-primary is-outlined"
            >
              Informații medici și pacienți
            </router-link>
          </div>
        </div>
        <div class="column is-7">
          <div class="box">
            <div id="animation-scene">@TODO: Animation</div>
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <h1 class="is-spaced">De ce este nevoie?</h1>
      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            <p>
              Avem nevoie de cât mai multe pulsoximetre și concentratoare de
              oxigen, extrem de necesare pentru tratarea la domiciliu, sub
              supravegherea medicilor de familie, a pacienților infectați cu
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

        <div class="column">
          <div class="columns is-multiline">
            <div class="column is-6">
              <HomeProgress
                title="Concentratoare oxigen"
                :value="12"
                :max="500"
              />
            </div>
            <div class="column is-6">
              <HomeProgress title="Pulsoximetre" :value="10" :max="10" />
            </div>
            <div class="column is-6">
              <HomeProgress
                title="Echipament protecție"
                :value="245"
                :max="520"
              />
            </div>
            <div class="column is-6">
              <HomeProgress title="Voluntari" :value="5" :max="10" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="columns">
        <div class="column is-4">
          <h2>Ce s-a reușit până acum<br /></h2>

          <h2>120</h2>
          Donații individuale

          <h2 class="has-text-primary">
            234.567 lei
          </h2>
          <br />

          <h2>80</h2>
          Companii
          <h2 class="has-text-primary">
            234.567 lei
          </h2>
        </div>
        <div class="column">
          <b-table
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
        <div class="button button-pulse is-primary is-size-1">
          <b-icon icon="arrow-right" />
        </div>

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

      <div class="columns">
        <div class="column is-4">
          <h3>40 companii</h3>
          <div class="box">@TODO: Carousel</div>

          <p>
            <router-link :to="{}">
              Model contract sponsorizare<b-icon icon="arrow-right" />
            </router-link>
          </p>
        </div>
        <div class="column">
          <h3>1323 cetateni</h3>
          <div class="box">@TODO: Carousel</div>

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

      <div class="box">@TODO: ONG Grid</div>
    </div>

    <div class="section has-text-centered">
      <div class="container box">
        <h2>Intrebări frecvente</h2>
        <div>@TODO: FAQ</div>
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

            <a href="#" class="button is-primary is-large">
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

            <a href="#" class="button is-primary is-large">
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
import ApiService from '@/services/api'
import HomeProgress from '@/components/HomeProgress'
// import * as oxigen_animation from 'oxigen-animation'

export default {
  name: 'Home',
  components: { HomeProgress },
  data() {
    return {
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
      data: {
        campaign: {
          id: 1,
          companies_count: 0,
          companies_sum: null,
          donors_count: 298,
          donors_sum: 1851402,
          name: 'Oxigen pentru Timisoara',
          target: 2500000.0,
          amount_collected: 925901.0,
          donations: 151,
        },
        needs: [],
        expenses: [
          {
            id: 1,
            name:
              '2 aparate oxigen High Flow Therapy +consumabilele pentru 40 pacienti',
            supplier: 'Linde Gaz Romania',
            document: 'fact. nr. 110/17.11.2020',
            status: 'in curs de livrare',
            quantity: 71756.0,
            in_use: 0.0,
            available: 0.0,
            price: 0.0,
            comment: 'pentru Spitalul de Boli Infecțioase Victor Babeș',
          },
          {
            id: 2,
            name: '500 pulsoximetre',
            supplier: 'Dante International S.A',
            document: '\nfact. nr. 627281\n/19.11.20\n',
            status: 'in curs de livrare',
            quantity: 27600.0,
            in_use: 0.0,
            available: 0.0,
            price: 0.0,
            comment:
              'pentru persoane fizice cu forme moderate ale bolii Covid19',
          },
        ],
        quotes: [],
        faqs: [],
        covid_stats: {
          hospitals_ocupation_rate: null,
          new_cases: null,
          infection_rate: null,
          date: null,
        },
        partners: [],
      },
    }
  },
  mounted() {
    // this.getData()
    // oxigen_animation.init({
    //   element: document.querySelector('#animation-scene'),
    //   total_necesar: 250000000,
    // })
  },
  methods: {
    getData() {
      ApiService.get('dashboard/').then((response) => {
        this.data = response.dashboard
        console.log(this.data)
      })
    },
  },
  destroyed() {
    // document.body.classList.remove('home-view')
  },
}
</script>

<style lang="scss" scoped>
.button-pulse {
  position: relative;
  width: 90px;
  height: 90px;
  float: right;
  left: -80px;
  border-radius: 100%;
  box-shadow: 0 0 0 0 rgba(225, 10, 20, 0.45);
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
    border-radius: 100%;
    box-shadow: 0 0 0 0 rgba(225, 10, 20, 0.45);
    animation: pulse-big 2.5s infinite cubic-bezier(0.3, 0, 0, 1);
  }
}
</style>
