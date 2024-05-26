<template>
  <div class="tableModuloManobra">
    <div class="title-table">
      <table>
        <thead>
          <th v-for="coluna in colunas" :key="coluna.key">{{ coluna.label }}</th>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="index" :class="{ imp: index % 2 === 0, par: index % 2 !== 0 }">
            <td v-for="coluna in colunas" :key="coluna.key">{{ item[coluna.key] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      required: true,
    },
    colunas: {
      type: Array,
      required: true,
      default: () => [
        { key: 'tipo', label: 'Tipo' },
        { key: 'quantidade', label: 'Quantidade' },
      ],
    },
  },
};
</script>

<style scoped>
.title-table {
  width: 100%;
  margin: 55px 0px;
  display: flex;
  justify-content: center;
}

table {
  border-collapse: collapse;
  width: 90%;
}

table thead {
  background-color: #F5FABF;

}

th {
  padding: 1% 20px;
  color: #000;
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
  margin-top: 1%;
}

td {
  border: none;
  padding: 1.4% 2%;
  text-align: center;
  color: #000;
}

.font-awesome-icon {
  font-size: 200px !important;
  color: red !important;
}
</style>