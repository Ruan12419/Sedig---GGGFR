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
                  <TabelaComponent :items="tableInsumosItens" :colunas="tableInsumosColunas" />
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
      adicionarInsumo() {
          if (this.selectedForm.selectedTipoInsumo && this.selectedForm.selectedQuantidade && this.selectedForm.selectedPrecoUnitario) {
              this.tableInsumosItens.push({
                  tipoInsumo: this.selectedForm.selectedTipoInsumo,
                  quantidade: this.selectedForm.selectedQuantidade,
                  precoUnitario: this.selectedForm.selectedPrecoUnitario,
                  custo: this.calcularCusto(this.selectedForm.selectedQuantidade, this.selectedForm.selectedPrecoUnitario),
              });
              this.resetForm();
          } else {
              alert('Por favor, preencha todos os campos antes de adicionar um insumo.');
          }
      },
      calcularCusto(quantidade, precoUnitario) {
          return quantidade * precoUnitario;
      },
      resetForm() {
          this.selectedForm.selectedTipoInsumo = null;
          this.selectedForm.selectedQuantidade = null;
          this.selectedForm.selectedPrecoUnitario = null;
      },
  },
  computed: {
      custoTotal() {
          return this.tableInsumosItens.reduce((total, item) => total + item.custo, 0);
      }
  },
  data() {
      return {
          selectedForm: {
              selectedTipoInsumo: null,
              selectedQuantidade: null,
              selectedPrecoUnitario: null,
          },
          insumosForm: {
              tipoInsumo: ["Material", "Mão de Obra", "Equipamento"],
          },
          tableInsumosItens: [],
          tableInsumosColunas: [
              { key: 'tipoInsumo', label: 'Tipo de Insumo' },
              { key: 'quantidade', label: 'Quantidade' },
              { key: 'precoUnitario', label: 'Preço Unitário (R$)' },
              { key: 'custo', label: 'Custo (R$)' },
          ],
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
