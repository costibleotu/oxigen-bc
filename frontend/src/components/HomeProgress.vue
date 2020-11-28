<template>
  <div>
    <h3 class="is-size-3">
      <b>{{ title }}</b>
    </h3>

    <div class="progress-wrapper">
      <progress v-bind="{ value, max }" class="progress is-primary">{{
        value
      }}</progress>
      <p class="progress-value" :style="getPosition">
        {{ value }}
      </p>
    </div>

    <p class="is-size-3 has-text-right has-text-weight-bold progress-label">
      {{ max }}
    </p>
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
.progress-label {
  margin-top: -1rem;
}

.progress-value {
  padding: 7px 10px;
}
</style>
