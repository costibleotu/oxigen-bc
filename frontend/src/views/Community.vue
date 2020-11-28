<template>
  <div>
    <div class="container">
      <div class="section">
        <h1>Suntem o comunitate</h1>

        <div class="columns">
          <div class="column is-4">
            <div class="content is-small">
              Fiecare dintre noi are puterea de a spori resursele cu care
              medicii salvează vieți. Fiecare dintre noi are puterea de a dona
              respirațiile prețioase de care au nevoie pacienții în drumul lor
              spre vindecare.
            </div>
          </div>
        </div>

        <h2>
          <span class="has-text-primary">80</span> de companii susțin cauza
        </h2>
        <h2><span class="has-text-primary">234.567lei</span> donați</h2>

        <div class="box">
          @TODO: ONG List
        </div>
      </div>
    </div>

    <div class="box is-paddingless">
      <div class="section container">
        <h2><span class="has-text-primary">120</span> donatori individuali</h2>
        <h2><span class="has-text-primary">234.567lei</span> donați</h2>

        <br>

        <div class="columns">
          <div class="column is-4">
            <h3 class="is-size-4">Donatori</h3>

            <div class="box-list">
              <div class="box">
                <b class="is-pulled-right has-text-primary">200lei</b>

                <h3 class="is-size-4">Alex Iliescu</h3>
                <p class="is-size-5 has-text-grey">
                  #oxigenpentrutimisoara #o2tm
                </p>
              </div>
            </div>
          </div>
          <div class="column">
            <h3 class="is-size-4">Povesti scurte din carantina</h3>

            <div class="box-list">
              <div class="box is-large">
                <h3>
                  If you find it in your heart to care for somebody else, you
                  have succeeded. This is the story format for up to 250
                  characters.
                </h3>

                <div class="content">
                  <p>Hello, content.</p>
                </div>

                <p class="quote">
                  <b-icon icon="quote-left" />
                  <b>Maya - Timisoara</b>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Community',
  components: {},
  mounted() {},
}
</script>

<style lang="scss" scoped>
.box-list {
  .box {
    background-color: $white;
    padding: 30px;
    border-radius: 10px;

    h3 {
      margin-bottom: 10px;
    }

    &.is-large {
      padding: 40px;

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
