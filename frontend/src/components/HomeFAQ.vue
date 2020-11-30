<template>
  <div>
    <b-collapse
      class="question"
      animation="slide"
      v-for="(question, index) of data"
      :key="index"
      :open="isOpen == index"
      @open="isOpen = index"
    >
      <a slot="trigger" class="question-header is-size-3 is-flex" role="button">
        <b-icon icon="question-circle" class="has-text-primary" />
        <span>{{ question.question }}</span>
      </a>

      <div class="content" v-html="question.answer"></div>
    </b-collapse>
  </div>
</template>

<script>
export default {
  name: 'HomeFAQ',
  components: {},
  props: {
    data: Array
  },
  data() {
    return {
      isOpen: null
    }
  }
}
</script>

<style lang="scss" scoped>
.question {
  border-top: 1px solid $border;
  padding: 20px 0;

  .question-header {
    color: $black;
    flex-direction: row-reverse;
    justify-content: space-between;

    @include tablet {
      flex-direction: row;
      justify-content: flex-start;
    }

    .icon {
      margin-left: 15px;

      @include tablet {
        margin-left: 0;
        margin-right: 30px;
      }
    }

    &:hover {
      color: $primary;
    }
  }

  .content {
    padding: 12px 12px 0 0px;

    @include tablet {
      padding: 12px 12px 0 50px;
    }
  }
}
</style>
