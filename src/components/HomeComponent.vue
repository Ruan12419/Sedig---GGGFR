<template>
  <section class="orcamentos-cadastrados">
    <div class="title-table">
      <h1>Orçamentos Cadastrados</h1>
      <TabelaComponent :items="tableSubestacaoItens" :colunas="tableSubestacaoColunas"
        :editable-orcamento-id="editableOrcamentoId">
        <template v-slot:acao="{ item }">
          <td>
            <span class="icon-container" v-if="editableOrcamentoId !== item.id">
              <font-awesome-icon icon="edit" :font-size="30" color="green" @click="editItem(item)" />
            </span>
            <span class="icon-container" v-if="editableOrcamentoId !== item.id">
              <font-awesome-icon icon="trash-alt" :font-size="30" color="red" @click="deleteItem(item.id)" />
            </span>
            <button @click="saveItem(item)" v-if="editableOrcamentoId === item.id">Salvar</button>
          </td>
        </template>

      </TabelaComponent>
    </div>
  </section>
</template>

<script>
import http from "@/http"
import { library } from '@fortawesome/fontawesome-svg-core';
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import TabelaComponent from './TabelaComponent.vue';

library.add(faEdit, faTrashAlt);

export default {
  name: "HomeComponent",
  components: {
    FontAwesomeIcon,
    TabelaComponent
  },
  methods: {
    editItem(item) {
      this.editableOrcamentoId = item.id;
      this.editableOrcamento = { ...item };
    },
    saveItem(orcamento) {
      http.post(`/orcamentos/edit/${orcamento.id}/`, orcamento)
        .then(response => {
          console.log(response.data.mensagem);
          this.editableOrcamentoId = null;
          this.fetchOrcamentos();
        })
        .catch(error => {
          console.error('Erro ao salvar orçamento:', error);
        });
    },
    deleteItem(orcamentoId) {
      const csrfToken = this.getCookie('csrftoken');
      http.delete(`/orcamentos/delete/${orcamentoId}`, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      })
        .then(response => {
          console.log(response.data.mensagem);
          this.tableSubestacaoItens = this.tableSubestacaoItens.filter(item => item.id !== orcamentoId);
        })
        .catch(error => {
          console.error('Erro ao deletar orçamento:', error);
        });
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    fetchOrcamentos() {
      http.get('/orcamentos')
        .then(response => {
          this.tableSubestacaoItens = response.data;
        })
        .catch(error => {
          console.error('Erro ao buscar orçamentos:', error);
        });
    }
  },
  mounted() {
    this.fetchOrcamentos();
  },
  data() {
    return {
      showDropdown: false,
      tableSubestacaoItens: [
      ],
      tableSubestacaoColunas: [
        { key: 'nomeSubestacao', label: 'Nome da Subestação' },
        { key: 'dataCotacao', label: 'Data Cotação' },
        { key: 'qtdPatios', label: 'Qtd. Pátios' },
        { key: 'qtdModulos', label: 'Qtd. Módulos' },
        { key: 'acao', label: 'Ação', sortable: false }
      ],
      editableOrcamentoId: null,
      editableOrcamento: {},
    };
  }
};
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

.icon-container {
  padding: 1% 0%;
  padding-right: 25%;
  display: inline-block;
}
</style>