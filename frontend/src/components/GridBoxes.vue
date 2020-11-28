<template>
  <div class="columns is-variable is-3 is-multiline grid-container">
    <div
      class="column is-3 is-2-widescreen"
      v-for="(item, index) in data"
      :key="`grid-${item.id || index}`"
    >
      <a :href="item.link" target="_blank">
        <figure class="image is-square">
          <img :src="item.logo" alt="" />
        </figure>

        <b class="title">
          {{ item.name }}
        </b>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GridBoxes',
  components: {},
  props: {
    data: Array
  },
  data() {
    return {}
  }
}
</script>

<style lang="scss" scoped>
.grid-container {
  margin-top: 16px;

  .column {
    .image {
      margin-bottom: 20px;
    }

    .title {
    }
  }
}
</style>
