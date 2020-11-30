<template>
  <div>
    <div class="container" v-if="data.campaign">
      <div class="section">
        <h1>Suntem o comunitate</h1>

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

        <h2>
          <span class="has-text-primary">{{
            data.campaign.companies_count
          }}</span>
          companii susțin cauza
        </h2>
        <h2>
          <span class="has-text-primary">{{
            data.campaign.companies_sum | currency
          }}</span>
          donați
        </h2>

        <GridBoxes v-if="data.donors" :data="companies" />
      </div>
    </div>

    <div class="box is-paddingless">
      <div class="section container" v-if="data.campaign">
        <h2>
          <span class="has-text-primary">{{ data.campaign.donors_count }}</span>
          donatori individuali
        </h2>
        <h2>
          <span class="has-text-primary">{{
            data.campaign.donors_sum | currency
          }}</span>
          donați
        </h2>

        <br />

        <div class="columns">
          <div class="column is-4" v-if="people.data">
            <h3 class="is-size-4">Donatori</h3>

            <div class="box-list">
              <div
                class="box"
                v-for="(donor, index) in people.visible"
                :key="`donor-${index}`"
              >
                <b class="is-pulled-right has-text-primary">
                  {{ donor.amount | currency }}
                </b>

                <h3 class="is-size-4">{{ donor.display_name }}</h3>

                <p class="is-size-5 has-text-grey" v-html="donor.comment">
                </p>
              </div>
            </div>

            <p
              class="has-text-centered"
              v-if="people.visible.length < people.data.length"
            >
              <br /><a @click="loadMore('people')">Vezi mai multe</a>
            </p>
          </div>
          <div class="column">
            <h3 class="is-size-4" v-if="stories.data">
              Povești scurte din carantină
            </h3>

            <div class="box-list">
              <div
                class="box is-large"
                v-for="(story, index) in stories.visible"
                :key="`story-${index}`"
              >
                <div class="content">
                  <p>{{ story.comment }}</p>
                </div>

                <p class="quote">
                  <b-icon icon="quote-left" />
                  <b>{{ story.name }}</b>
                </p>
              </div>
            </div>

            <p
              class="has-text-centered"
              v-if="stories.visible.length < stories.data.length"
            >
              <br /><a @click="loadMore('stories')">Vezi mai multe</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ApiService from '@/services/api'

import GridBoxes from '@/components/GridBoxes'

export default {
  name: 'Community',
  components: { GridBoxes },
  data() {
    return {
      data: {
        donors: null,
        campaign: null,
        quotes: null
      },
      people: {
        data: [],
        visible: [],
        increment: 10,
        index: 0
      },
      stories: {
        data: [],
        visible: [],
        increment: 4,
        index: 0
      },
      companies: null
    }
  },
  mounted() {
    ApiService.get('donors/').then(response => {
      this.data.donors = response

      this.people.data = this.data.donors.filter(e => !e.is_company)
      this.companies = this.data.donors.filter(e => e.is_company)

      this.loadMore('people')
    })

    ApiService.get('campaigns/').then(response => {
      this.data.campaign = response[0]
    })

    ApiService.get('quotes/').then(response => {
      this.stories.data = response
      this.loadMore('stories')
    })
  },
  methods: {
    loadMore(type) {
      // console.log('loadItems', type)

      this[type].index += this[type].increment
      this[type].visible = this[type].data.slice(0, this[type].index)
    }
  }
}
</script>

<style lang="scss" scoped>
.box-list {
  .box {
    background-color: $white;
    padding: 30px;
    border-radius: 10px;
    overflow: hidden;

    h3 {
      margin-bottom: 10px;
    }

    &.is-large {
      padding: 20px;

      @include desktop {
        padding: 40px;
      }

      h3 {
        margin-bottom: 28px;
      }

      .quote {
        margin-top: 32px;

        .icon {
          color: $grey-light;
          font-size: $size-2;
          margin-right: 16px;
        }
      }
    }
  }
}
</style>
