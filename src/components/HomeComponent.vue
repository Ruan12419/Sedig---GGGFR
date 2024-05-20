<template>
  <section class="orcamentos-cadastrados">
    <div class="title-table">
    <h1>Orçamentos Cadastrados</h1>

    <table>
      <thead>
        <th>Nome da Subestação</th>
        <th>Data Cotação</th>
        <th>Qtd. Pátios</th>
        <th>Qtd. Módulos</th>
        <th>Ação</th>
      </thead>

      <tbody>
        <tr class="imp">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="par">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="imp">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="par">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="imp">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="par">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
        <tr class="imp">
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
          <td></td>
        </tr>
      </tbody>
    </table>
    </div>
    <div></div>
  </section>
</template>

<script>
export default {
  name: "HomeComponent",
  data() {
    return {
      showDropdown: false
    }
  }
}
</script>

<style scoped>

h1 {
  padding: 20px;
}
.orcamentos-cadastrados {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.title-table {
  width: 91%;
}

table {
  border-collapse: collapse;
  width: 100%;
}

table thead {
  background-color: #F5FABF;

}

th {
  padding: 1% 20px;
}

th:first-child {
  border-top-left-radius: 15px;
}

th:last-child {
  border-top-right-radius: 15px;
}
tbody tr {
  box-shadow: inset 0px 0px 10px rgba(0, 0, 0, 0.05);
}

.imp {
  background-color: #99C7E8;
  border: none;
}

.par {
  background-color: #66AADD;
  margin: 0;
}

td {
  border: none;
  padding: 1% 7%;
  text-align: center;
}

.orcamentos {
  background-color: #EEE;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10%;
  height: 100%;
}

</style>