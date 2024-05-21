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
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="par">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="imp">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="par">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="imp">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="par">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
          <tr class="imp">
            <td>Olinda</td>
            <td>2023</td>
            <td>3</td>
            <td>7</td>
            <td>
              <font-awesome-icon icon="edit" :font-size="20" color="green"/>
              <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div></div>
  </section>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faEdit, faTrashAlt)
export default {
  name: "HomeComponent",
  components: {
    FontAwesomeIcon,
  },
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
td:last-child {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  margin-top: 8%;
}

td {
  border: none;
  padding: 1% 7%;
  text-align: center;
}
.font-awesome-icon {
  font-size: 200px !important;
  color: red !important;
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