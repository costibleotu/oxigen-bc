<template>
  <div class="container">
    <div class="section">
      <h1>Ai nevoie de echipament medical?</h1>

      <div class="columns">
        <div class="column is-4">
          <div class="content is-small">
            Medicul tau de familie este legatura ta cu comunitatea medicala si
            resursele de suport disponibile. Supraveghetorul parcursului bolii
            fiecarui pacient din gestiunea sa, poate recunoaste momentul in care
            intervine nevoia de echipament si o poate semnala.
          </div>
        </div>
      </div>

      <br>

      <div class="columns">
        <div class="column is-4">
          <h2>Cum intrii în posesia unui concentrator de oxigen?</h2>

          <div class="box box-bubble">
            <h2>
              Call center <br />
              0372.987
            </h2>
          </div>
        </div>
        <div class="column">
          <ol>
            <li>
              Medicul de familie anunta necesitatea prin platforma
              <b class="has-text-primary">Medici de familie.</b>
            </li>
            <li>
              Operatorul platformei va inregistra datele pacientului si cererea.
            </li>
            <li>
              Daca exista echipament disponibil, curierul ti-l va livra acasa
              impreuna cu un proces verbal de primire pe care trebuie sa il
              semnezi.
            </li>
            <li>
              Daca nu exista echipament disponibil, vei fi pus intr-o coada de
              asteptare pana la eliberarea unui echipament sau pana la
              urmatoarea runda de achizitii.
            </li>
            <li>
              Medicul de familie va fi informat in oricare din cazuri de
              disponibilitate.
            </li>
          </ol>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="columns">
        <div class="column is-4">
          <h2>Cum returnezi echipamentul?</h2>
        </div>
        <div class="column">
          <ol>
            <li>
              Medicul de familie anunta eliberarea echipamentului prin platforma
              <b class="has-text-primary">Medici de familie.</b>
            </li>
            <li>
              Curierul va veni sa ridice echipamentul si iti va cere sa semnezi
              procesul verbal de predare.
            </li>
            <li>
              Aparatul este livrat in zona de dezinfectare pentru igienizare si
              verificare.
            </li>
            <li>
              Daca aparatul este functional el va fi dus in zona de stocare si
              va redeveni disponibil.
            </li>
            <li>
              Daca aparatul nu este functional el va fi dus in service pentru
              repratii.
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InfoMedic',
  components: {},
  mounted() {},
}
</script>

<style lang="scss" scoped>
.box-bubble {
  margin-top: 43px;
  text-align: center;
  border-radius: 10px;
  background-color: $primary;
  color: $white;
  position: relative;
  padding: 29px 12px 32px;

  &:after {
    position: absolute;
    content: '';
    pointer-events: none;
    top: 100%;
    right: auto;
    bottom: auto;
    left: 36px;
    transform: translateX(-50%);
    border-top: 13px solid $primary;
    border-right: 13px solid transparent;
    border-left: 13px solid transparent;
  }

  h2 {
    margin: 0;
  }
}

ol {
  list-style: none;

  li {
    position: relative;
    border-top: 2px solid $border;
    padding: 29px 0 29px 84px;

    &:before {
      content: counter(list-item);
      font-weight: $weight-bold;
      font-size: $size-4;
      display: inline-flex;
      position: absolute;
      top: calc(50% - 21px);
      align-items: center;
      justify-content: center;
      margin-left: -64px;
      width: 39px;
      height: 39px;
      margin-right: 20px;
      border-radius: 100%;
      border: 4px solid $primary;
    }
  }
}
</style>
