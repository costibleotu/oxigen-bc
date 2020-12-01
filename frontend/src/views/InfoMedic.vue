<template>
  <div class="container">
    <div class="section">
      <h1>Cum funcționează proiectul “Oxigen pentru Timișoara”?</h1>
      <br />
      <br />

      <div class="columns is-multiline">
        <div class="column is-12">
          <h2>
            Ai nevoie de echipament medical dacă:
          </h2>
        </div>

        <div class="column is-4">
          <div class="bullet">a</div>
          Ești pacient care a trecut pe la triajul de la Spitalul „Victor Babeș”
          Timișoara, iar doctorii au decis monitorizarea la domiciliu cu
          ajutorul unui pulsoximetru
        </div>
        <div class="column is-4">
          <div class="bullet">b</div>
          Ești pacient care a trecut pe la triajul de la Spitalul „Victor Babeș”
          Timișoara, iar doctorii au decis monitorizarea la domiciliu cu
          ajutorul unui pulsoximetru și un concentrator de oxigen
        </div>
        <div class="column is-4">
          <div class="bullet">c</div>
          Ești pacient în Spitalul „Victor Babeș” Timișoara a cărui stare de
          sănătate în spital s-a îmbunătățit, dar are nevoie în continuare de
          oxigenoterapie și este externat cu pulsoximetru și concentrator pt a
          elibera locul din spital pentru cazuri mai grave
        </div>
      </div>
    </div>
    <div class="section">
      <div class="columns">
        <div class="column is-4">
          <h2>Cum intri în posesia unui concentrator de oxigen?</h2>

          <!-- <div class="box box-bubble">
            <h2>
              Call center <br />
              0372.987
            </h2>
          </div> -->
        </div>
        <div class="column">
          <ol>
            <li>
              În urma deciziei medicilor de la Spitalul „Victor Babeș” Timișoara
              de externare, pacientul va primi echipamentul (pulsoximetru și/sau
              concentrator de oxigen) și va fi instruit cum să le folosească.
            </li>
            <li>
              Simultan, este anunțat medicul de familie, care va contacta
              pacientul pentru monitorizarea de la distanță a stării de sănătate
              a pacientului aflat la domiciliu.
            </li>
            <li>
              Dacă după plecarea din spital monitorizarea s-a făcut doar cu
              pulsoximetru, iar starea de sănătate s-a agravat, medicul de
              familie face o cerere pentru un concentrator de oxigen, prin
              platforma
              <b class="has-text-primary">Medici de familie.</b>.
            </li>
            <li>
              Operatorul platformei va înregistra datele pacientului și cererea
              de livrare.
            </li>
            <li>
              Dacă există echipament disponibil, acesta va fi livrat la
              domiciliul pacientului, fiind predat pe baza unui cu un proces
              verbal de primire.
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
              Medicul de familie anunță eliberarea echipamentului prin platforma
              <b class="has-text-primary">Medici de familie.</b>
            </li>
            <li>
              Pacientul va pregăti pentru returnare echipamentul primit în
              ambalajul original, mai puțin elementele de unică folosință ale
              concentratorului (tuburile de plastic, bidonul de umidificare a
              aerului).
            </li>
            <li>
              Un voluntar va veni să ridice echipamentul, sigilându-l pentru
              transportarea în siguranță și se va semna un proces-verbal de
              preluare.
            </li>
            <li>
              Aparatul este livrat în spital pentru igienizare, dezinfectare și
              schimbarea filtrului hepa a concentratorului de oxigen.
            </li>
            <li>Aparatul va deveni disponibil pentru următorul beneficiar.</li>
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
  mounted() {}
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
  margin-left: 0;
  margin-right: 0;

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

.bullet {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 39px;
  height: 39px;
  background-color: $primary;
  border-radius: 100%;
  color: $white;
  font-size: $size-3;
  font-weight: $weight-semibold;
  margin-bottom: 20px;
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
