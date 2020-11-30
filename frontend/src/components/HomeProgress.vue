<template>
  <div class="progress-component">
    <div class="columns is-mobile is-variable">
      <div class="column">
        <p class="is-size-4">
          {{ title }}
        </p>
      </div>
      <div class="column is-narrow">
        <p class="is-size-4 has-text-right has-text-weight-bold">
          {{ max }}
        </p>
      </div>
    </div>

    <div class="progress-wrapper">
      <progress v-bind="{ value, max }" class="progress is-primary">{{
        value
      }}</progress>
      <p class="progress-value" :style="getPosition">
        {{ value }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeProgress',
  components: {},
  props: {
    title: String,
    value: Number,
    max: Number
  },
  computed: {
    getPosition() {
      const p = Math.round((this.value / this.max) * 100)
      const min = 4,
        max = 95

      if (p < min) return { left: 0, transform: 'none' }
      if (p > max) return { right: 0, left: 'auto', transform: 'none' }

      return { left: p + '%' }
    }
  }
}
</script>

<style lang="scss" scoped>
.progress-component {
  @include desktop {
    padding-top: 15px;
    padding-bottom: 15px;
  }

  .columns:not(:last-child) {
    margin-bottom: 0;
  }

  .progress-value {
    padding: 7px 10px;
  }
}
</style>
