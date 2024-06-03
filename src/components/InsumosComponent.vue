<template>
  <section class="cadastrar-insumos">
    <div class="cadastro">
      <h1>Cadastrar Insumos</h1>
      <section class="insumos-form">
        <section class="row">
          <div class="column">
            <label for="insumo">Tipo de Insumo:</label>
            <select id="insumo" v-model="selectedForm.selectedTipoInsumo" class="input-selectMarginTop">
              <option disabled selected>Selecione</option>
              <option v-for="insumo in insumosForm.tipoInsumo" :key="insumo">{{ insumo }}</option>
            </select>
          </div>
          <div class="column">
            <label for="local">Local:</label>
            <select id="local" v-model="selectedForm.selectedLocal" class="input-selectMarginTop">
              <option disabled selected>Selecione</option>
              <option v-for="insumo in insumosForm.local" :key="insumo">{{ insumo }}</option>
            </select>
          </div>
          <div class="column" v-if="selectedForm.selectedLocal === 'Modulo de Manobra'">
            <label for="tensaoPrimaria">Tensão Primária: </label>
            <select id="tensaoPrimaria" v-model="selectedForm.selectedTensaoPrimaria" class="input-selectMarginTop">
              <option disabled selected>Selecione</option>
              <option v-for="tensao in insumosForm.tensaoPrimaria" :key="tensao">{{ tensao }}</option>
            </select>
          </div>
          <div class="column"
            v-if="selectedForm.selectedTensaoPrimaria && selectedForm.selectedLocal === 'Modulo de Manobra'">
            <label for="arranjo">Arranjo: </label>
            <select id="arranjo" v-model="selectedForm.selectedArranjo" class="input-selectMarginTop">
              <option disabled selected>Selecione</option>
              <option v-for="arranjo in insumosForm.arranjo[selectedForm.selectedTensaoPrimaria]" :key="arranjo">{{
                arranjo }}</option>
            </select>
          </div>
          <div class="column">
            <label for="nome">Nome: </label>
            <input id="nome" v-model="selectedForm.selectedNome" class="input-selectMarginTop" />
          </div>
          <div class="column">
            <label for="quantidade">Quantidade:</label>
            <input type="number" v-model="selectedForm.selectedQuantidade" class="input-selectMarginTop">
          </div>
          <div class="column">
            <label for="precoUnitario">Preço Unitário (R$):</label>
            <input type="number" v-model="selectedForm.selectedPrecoUnitario" class="input-selectMarginTop">
          </div>
          <div class="column">
            <label for="addInsumo">Adicionar Insumo:</label>
            <div class="botao-estilo" @click="adicionarInsumo">
              <font-awesome-icon icon="plus" :font-size="30" color="white" />
            </div>
          </div>
        </section>
        <hr>
        <div class="tableInsumos">
          <TabelaComponent :items="tableInsumosItens" :colunas="tableInsumosColunas"
            :editable-insumo-id="editableInsumoId">
            <template v-slot:acao="{ item }">
              <td style="width: 100%;">
                <span class="icon-container" v-if="editableInsumoId !== item.id">
                  <font-awesome-icon icon="edit" :font-size="30" color="green" @click="editItem(item)" />
                </span>
                <span class="icon-container" v-if="editableInsumoId !== item.id">
                  <font-awesome-icon icon="trash-alt" :font-size="30" color="red" @click="deleteItem(item.id)" />
                </span>
                <button @click="saveItem(item)" v-if="editableInsumoId === item.id">Salvar</button>
              </td>
            </template>
          </TabelaComponent>
        </div>
        <section class="total-cost row" v-if="tableInsumosItens.length > 0">
          <div class="column">
            <label for="totalCost">Custo Total (R$):</label>
            <input type="number" :value="custoTotal" readonly class="input-selectMarginTop">
          </div>
        </section>
      </section>
    </div>
  </section>
</template>

<script>
import http from "@/http"
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import TabelaComponent from "./TabelaComponent.vue"
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faPlus)

export default {
  name: "InsumosComponent",
  components: {
    FontAwesomeIcon,
    TabelaComponent,
  },
  methods: {
    generateId() {
      return this.nextId++;
    },
    /*adicionarInsumo() {
      if (this.selectedForm.selectedTipoInsumo && this.selectedForm.selectedNome && this.selectedForm.selectedQuantidade && this.selectedForm.selectedPrecoUnitario) {
        this.tableInsumosItens.push({
          id: this.generateId(),
          tipoInsumo: this.selectedForm.selectedTipoInsumo,
          nome: this.selectedForm.selectedNome,
          local: this.selectedForm.selectedLocal,
          quantidade: this.selectedForm.selectedQuantidade,
          precoUnitario: this.selectedForm.selectedPrecoUnitario,
          custo: this.calcularCusto(this.selectedForm.selectedQuantidade, this.selectedForm.selectedPrecoUnitario),
        });
        this.resetForm();
      } else {
        alert('Por favor, preencha todos os campos antes de adicionar um insumo.');
      }
    },*/
    calcularCusto(quantidade, precoUnitario) {
      const total = (quantidade * precoUnitario).toFixed(2);
      return parseFloat(total);
    },
    resetForm() {
      this.selectedForm.selectedTipoInsumo = null;
      this.selectedForm.selectedLocal = null;
      this.selectedForm.selectedNome = null;
      this.selectedForm.selectedQuantidade = null;
      this.selectedForm.selectedPrecoUnitario = null;
    },
    editItem(item) {
      this.editableInsumoId = item.id;
      this.editableInsumo = { ...item };
    },
    adicionarInsumo() {
      if (this.selectedForm.selectedTipoInsumo && this.selectedForm.selectedNome && this.selectedForm.selectedQuantidade && this.selectedForm.selectedPrecoUnitario) {
        const novoInsumo = {
          tipo_insumo: this.selectedForm.selectedTipoInsumo,
          nome: this.selectedForm.selectedNome,
          local: this.selectedForm.selectedLocal,
          quantidade: this.selectedForm.selectedQuantidade,
          preco_unitario: this.selectedForm.selectedPrecoUnitario,
          custo: this.calcularCusto(this.selectedForm.selectedQuantidade, this.selectedForm.selectedPrecoUnitario),
        };
        http.post('/insumos/add/', novoInsumo)
          .then(response => {
            console.log(response.data.mensagem);
            this.tableInsumosItens.push({ ...novoInsumo, id: this.generateId() });
            this.resetForm();
          })
          .catch(error => {
            console.error('Erro ao adicionar insumo:', error);
          });
      } else {
        alert('Por favor, preencha todos os campos antes de adicionar um insumo.');
      }
    },
    saveItem(insumo) {
      http.post(`/insumos/update/${insumo.id}/`, insumo)
        .then(response => {
          console.log(response.data.mensagem);
          this.editableInsumoId = null;
        })
        .catch(error => {
          console.error('Erro ao salvar insumo:', error);
        });
    },
    deleteItem(insumoId) {
      http.delete(`/insumos/delete/${insumoId}`)
        .then(response => {
          console.log(response.data.mensagem);
          this.tableInsumosItens = this.tableInsumosItens.filter(item => item.id !== insumoId);
        })
        .catch(error => {
          console.error('Erro ao deletar insumo:', error);
        });
    },
    listarInsumos() {
      http.get('/insumos/')
        .then(response => {
          this.tableInsumosItens = response.data;
        })
        .catch(error => {
          console.error('Erro ao listar insumos:', error);
        });
    },
  },
  created() {
    this.listarInsumos();
  },
  computed: {
    custoTotal() {
      const total = this.tableInsumosItens.reduce((total, item) => total + item.custo, 0);
      return total.toFixed(2);
    }
  },
  data() {
    return {
      selectedForm: {
        selectedTipoInsumo: null,
        selectedLocal: null,
        selectedNome: null,
        selectedQuantidade: null,
        selectedPrecoUnitario: null,
        selectedTensaoPrimaria: null,
        selectedArranjo: null,
      },
      insumosForm: {
        tipoInsumo: ["Instalação", "Material", "Mão de Obra", "Equipamento"],
        local: ["Pátio", "Módulo de Manobra", "Módulo de Equipamento"],
        tensaoPrimaria: [13.8, 69, 138, 230, 345, 500],
        arranjo: {
          13.8: ["BPT", "BS"],
          69: ["BD5", "BPT", "BS"],
          138: ["BD4", "BD5", "BPT", "BS"],
          230: ["BD4", "BD5", "BPT"],
          345: ["AN", "BD4", "DJM"],
          500: ["AN", "BDDD", "DJM"],
        },
      },
      tableInsumosItens: [],
      tableInsumosColunas: [
        { key: 'tipo_insumo', label: 'Tipo de Insumo' },
        { key: 'local', label: 'Local' },
        { key: 'nome', label: 'Nome' },
        { key: 'quantidade', label: 'Quantidade' },
        { key: 'preco_unitario', label: 'Preço Unitário (R$)' },
        { key: 'custo', label: 'Custo (R$)' },
      ],
      nextId: 1,
      editableInsumoId: null,
      editableInsumo: {},
    }
  }
}
</script>

<style scoped>
h1 {
  padding: 20px;
  color: black;
}

.cadastrar-insumos {
  display: flex;
  align-items: center;
  flex-direction: column;
  color: #0D9488;
}

.cadastro {
  width: 91%;
}

.insumos-form {
  background-color: #f5f5f5;
  padding: 6%;
}

label {
  font-size: 22px;
}

.input-selectMarginTop {
  margin-top: 10px;
}

input,
select {
  height: 40px;
  border: none;
  margin-top: 30px;
}

select {
  width: 180px;
}

option {
  font-size: 18px;
}

.tableInsumos {
  margin-top: 20px;
}

.total-cost {
  margin-top: 20px;
}

.botao-estilo {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 45px;
  height: 45px;
  background-color: #46b341;
  padding: 1px 20px;
  border-radius: 15px;
  cursor: pointer;
}
</style>
