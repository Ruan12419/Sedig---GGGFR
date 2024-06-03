<template>
<section class="cadastrar-orcamentos">
<div class="cadastro">
<h1>Cadastrar Orçamentos</h1>
<section class="subestacao">
<section class="row">
<div class="column" style="width: 25%;">
<div class="nomeOrcamento column marginBottom">
<label for="nomeOrcamento">Nome do Orçamento: </label>
<input type="text" v-model="selectedForm.selectedNomeOrcamento">
</div>
</div>
</section>
<section class="row">
<div class="column">
<div class="nomeSubestacao column marginBottom">
<label for="nome">Nome da Subestação: </label>
<input type="text" v-model="selectedForm.selectedNomeSubestacao">
</div>
<label for="regiao">Região</label>
<div class="row">
<div class="column columnMarginR">
<label for="estado" class="label-place">Macroregião</label>
<select id="macroregiao" v-model="selectedForm.selectedMacroregiao"
class="input-selectMarginTop">
<option disabled selected>Selecione</option>
<option v-for="regiao in subestacaoForm.macroregiao" :key="regiao">{{ regiao }}
</option>
</select>
</div>
<div class="column">
<label for="estado" class="label-place">Estado</label>
<select id="estado" class="input-selectMarginTop" v-model="selectedForm.selectedEstado">
<option disabled selected>Selecione</option>
<option
v-for="estado in (estadosPorMacroregiao[selectedForm.selectedMacroregiao] || []).slice().sort((a, b) => a === 'Todos' ? -1 : b === 'Todos' ? 1 : a === 'Nenhum' ? -1 : b === 'Nenhum' ? 1 : a.localeCompare(b))"
:key="estado">{{ estado }}</option>
</select>
</div>
</div>
</div>
<div class="column">
<label for="dataRef">Data de Referência: </label>
<div class="row">
<div class="column columnMarginR">
<label for="ano" class="label-place">Ano</label>
<select id="ano" v-model="selectedForm.selectedAno" class="input-selectMarginTop">
<option disabled selected>Selecione</option>
<option v-for="ano in subestacaoForm.ano" :key="ano">{{ ano }}</option>
</select>
</div>
<div class="column marginBottom">
<label for="mes" class="label-place">Mês</label>
<select id="mes" v-model="selectedForm.selectedMes" class="input-selectMarginTop">
<option disabled selected>Selecione</option>
<option v-for="mes in subestacaoForm.mes" :key="mes">{{ mes }}</option>
</select>
</div>
</div>
<label for="tipoInstalacao">Tipo de instalação: </label>
<div class="tipoInstSub marginBottom">
<select id="tipoInstalacao" v-model="selectedForm.selectedTipoInstalacao">
<option disabled selected>Selecione</option>
<option v-for="tipoInstalacao in subestacaoForm.tipoInstalacao" :key="tipoInstalacao">{{
tipoInstalacao }}</option>
</select>
</div>
</div>
</section>
<hr>
<section class="dados-patio">
<h2>Pátio</h2>
<div class="row">
<div class="row">
<div class="tensaoPrimaria column columnMarginR">
<label for="tensaoPrimaria">Tensão Primária: </label>
<label for="tensaoPrimaria" class="label-place">kV</label>
<select id="tensaoPrimaria" v-model="selectedForm.selectedTensaoPrimaria"
class="input-selectMarginTop">
<option disabled selected>Selecione</option>
<option v-for="tensaoPrimaria in subestacaoForm.tensaoPrimaria"
:key="tensaoPrimaria">{{ tensaoPrimaria }}</option>
</select>
</div>
<div class="arranjo column">
<label for="arranjo">Arranjo: </label>
<label for="tensaoPrimaria" class="label-place">kV</label>
<select id="arranjo" v-model="selectedForm.selectedArranjo"
class="input-selectMarginTop">
<option disabled selected>Selecione</option>
<option
v-for="tensaoPrimaria in subestacaoForm.arranjo[selectedForm.selectedTensaoPrimaria]"
:key="tensaoPrimaria">{{ tensaoPrimaria }}</option>
</select>
</div>
</div>
<div class="column"></div>
</div>
<h3 @click="showManobra = !showManobra">
Módulo de Manobra <button>{{ showManobra ? '^' : '>' }}</button>
</h3>
<div v-bind:class="{ manobra: showManobra }">

<section class="moduloManobra row" v-if="showManobra">
<div class="column">
<div class="row">
<div class="sincDisjuntor column columnMarginR">
<label for="nome">Sincronização Disjuntor: </label>
<select id="sincDisjuntor" v-model="selectedForm.selectedSincDisjuntor">
<option disabled selected>Selecione</option>
<option v-for="sincDisjuntor in subestacaoForm.sincDisjuntor"
:key="sincDisjuntor">{{ sincDisjuntor }}</option>
</select>
</div>
<div class="tipoAplicacao column marginBottom">
<label for="regiao">Tipo Aplicação: </label>
<select id="tipoAplicacao" v-model="selectedForm.selectedTipoAplicacao">
<option disabled selected>Selecione</option>
<option v-for="tipoAplicacao in subestacaoForm.tipoAplicacao"
:key="tipoAplicacao">{{ tipoAplicacao }}</option>
</select>
</div>
</div>
<div class="moduloManobraQuantidade column">
<label for="regiao">Quantidade: </label>
<input type="text" v-model="selectedForm.selectedQuantidadeManobra">
</div>
</div>
<div class="column" style="width: 35%">
<div class="moduloManobraTipo column marginBottom">
<label for="nome">Tipo: </label>
<select id="tipo" v-model="selectedForm.selectedTipo" style="width: 100%;">
<option disabled selected>Selecione</option>
<option v-for="tipo in subestacaoForm.tipo" :key="tipo">{{ tipo }}</option>
</select>
</div>
<div class="column" style="align-items: flex-end;">
<label for="addModuloDeManobra">Adicionar Módulo de Manobra: </label>
<div class="botao-estilo" @click="adicionarModuloManobra">
<font-awesome-icon icon="add" :font-size="30" color="white" />
</div>
</div>
</div>
</section>
<div class="tableModuloManobra" v-if="showManobra">
<TabelaComponent :items="tableModuloManobraItens" :colunas="tableModuloManobraColunas"
:editable-orcamento-id="editableOrcamentoId">
<template v-slot:acao="{ item }">
<td style="width: 100%;">
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="edit" :font-size="30" color="green"
@click="editItem(item)" />
</span>
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="trash-alt" :font-size="30" color="red"
@click="deleteItem(item.id)" />
</span>
<button @click="saveItem(item)"
v-if="editableOrcamentoId === item.id">Salvar</button>
</td>
</template>
</TabelaComponent>
</div>
</div>
<hr>
<h3 @click="showEquipamento = !showEquipamento">Módulo de Equipamento <button>{{ showEquipamento ?
'^' : '>' }}</button></h3>
<div v-bind:class="{ equipamento: showEquipamento }">

<section class="moduloEquipamento row" v-if="showEquipamento">
<div class="row">
<div class="tipoEquipamento column columnMarginR">
<label for="nome">Tipo de Equipamento: </label>
<select id="tipoEquipamento" v-model="selectedForm.selectedTipoEquipamento"
style="width: 500px;">
<option disabled selected>Selecione</option>
<option v-for="tipoEquipamento in subestacaoForm.tipoEquipamento"
:key="tipoEquipamento">{{
tipoEquipamento }}</option>
</select>
</div>
<div class="moduloEquipamentoQuantidade column">
<label for="regiao">Quantidade: </label>
<input type="text" v-model="selectedForm.selectedQuantidadeEquipamento"
style="width: 300px;">
</div>
</div>
<div class="column">
<div class="column" style="align-items: flex-end;">
<label for="addModuloDeManobra">Adicionar Módulo de Equipamento: </label>
<div class="botao-estilo" @click="adicionarModuloEquipamento">
<font-awesome-icon icon="add" :font-size="30" color="white" />
</div>
</div>
</div>
</section>
<div class="tableModuloEquipamento" v-if="showEquipamento">
<TabelaComponent :items="tableModuloEquipamentoItens"
:colunas="tableModuloEquipamentoColunas" :editable-orcamento-id="editableOrcamentoId">
<template v-slot:acao="{ item }">
<td style="width: 100%;">
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="edit" :font-size="30" color="green"
@click="editItem(item)" />
</span>
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="trash-alt" :font-size="30" color="red"
@click="deleteItem(item.id)" />
</span>
<button @click="saveItem(item)"
v-if="editableOrcamentoId === item.id">Salvar</button>
</td>
</template>
</TabelaComponent>

</div>
</div>
<hr>
<section class="salva-patio row" style="justify-content: flex-end; margin-top: 100px;">
<div class="column">
<label for="addPatio">Cancelar: </label>
<div class="botao-estilo botao-estilo-cancelar" @click="showAlert">
<font-awesome-icon icon="arrow-left" :font-size="30" color="white" />
</div>
</div>
<div class="column">
<label for="addPatio">Adicionar Pátio: </label>
<div class="botao-estilo" @click="adicionarPatio">
<font-awesome-icon icon="add" :font-size="30" color="white" />
</div>
</div>
</section>

<div class="tablePatio">
<TabelaComponent :items="tablePatioItens" :colunas="tablePatioColunas"
:editable-orcamento-id="editableOrcamentoId">
<template v-slot:acao="{ item }">
<td style="width: 100%;">
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="edit" :font-size="30" color="green"
@click="editItem(item)" />
</span>
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="trash-alt" :font-size="30" color="red"
@click="deleteItem(item.id)" />
</span>
<button @click="saveItem(item)"
v-if="editableOrcamentoId === item.id">Salvar</button>
</td>
</template>
</TabelaComponent>
</div>
</section>
<hr>
<section class="salva-subestacao row" style="justify-content: flex-end; margin-top: 100px;">
<div class="column">
<label for="addSubestacao">Cancelar: </label>
<div class="botao-estilo botao-estilo-cancelar" @click="showAlert">
<font-awesome-icon icon="arrow-left" :font-size="30" color="white" />
</div>
</div>
<div class="column">
<label for="addSubestacao">Adicionar Subestação: </label>
<div class="botao-estilo" @click="adicionarSubestacao">
<font-awesome-icon icon="add" :font-size="30" color="white" />
</div>
</div>
</section>

<div class="tableSubestacao">
<TabelaComponent :items="tableSubestacaoItens" :colunas="tableSubestacaoColunas"
:editable-orcamento-id="editableOrcamentoId">
<template v-slot:acao="{ item }">
<td style="width: 100%;">
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="edit" :font-size="30" color="green"
@click="editItem(item)" />
</span>
<span class="icon-container" v-if="editableOrcamentoId !== item.id">
<font-awesome-icon icon="trash-alt" :font-size="30" color="red"
@click="deleteItem(item.id)" />
</span>
<button @click="saveItem(item)"
v-if="editableOrcamentoId === item.id">Salvar</button>
</td>
</template>
</TabelaComponent>
</div>
<hr>
<section class="salva-orcamento row" style="justify-content: flex-end; margin-top: 100px;">
<div class="column">
<label for="addOrcamento">Adicionar Orçamento: </label>
<div class="botao-estilo" @click="salvarOrcamentoCompleto">
<font-awesome-icon icon="add" :font-size="30" color="white" />
</div>
</div>
</section>
</section>
</div>
</section>
<section class="gerar-excel">
<label for="gerarExcel"></label>
<font-awesome-icon icon="file-excel" :font-size="45" color="white" />
</section>

</template>





<script>
import http from "@/http"
import { library } from '@fortawesome/fontawesome-svg-core'
import { faAdd, faArrowLeft, faPlus, faFileExcel } from '@fortawesome/free-solid-svg-icons'
import TabelaComponent from "./TabelaComponent.vue"
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faAdd, faArrowLeft, faPlus, faFileExcel)
export default {
name: "OrcamentosComponent",
components: {
FontAwesomeIcon,
TabelaComponent,
},
methods: {
showAlert() {
const certeza = confirm('Esta ação não pode ser revertida. Tem certeza de que deseja cancelar o cadastro?');
if (certeza) {
window.location.reload();
window.scrollTo(0, 0);
}
},
generateId() {
return this.nextId++;
},
adicionarModuloManobra() {
this.tableModuloManobraItens.push({
id: this.generateId(),
tipo: this.selectedForm.selectedTipo,
quantidade: this.selectedForm.selectedQuantidadeManobra,
acao: '',
sincDisjuntor: this.selectedForm.selectedSincDisjuntor,
tipoAplicacao: this.selectedForm.selectedTipoAplicacao,
});
},
adicionarModuloEquipamento() {
this.tableModuloEquipamentoItens.push({
id: this.generateId(),
equipamento: this.selectedForm.selectedTipoEquipamento,
quantidade: this.selectedForm.selectedQuantidadeEquipamento,
acao: '',
});
},
adicionarPatio() {
this.tablePatioItens.push({
id: this.generateId(),
patio: "Pátio-" + this.selectedForm.selectedTensaoPrimaria + "-" + this.selectedForm.selectedArranjo,
tensaoPrimaria: this.selectedForm.selectedTensaoPrimaria,
arranjo: this.selectedForm.selectedArranjo,
qtdModuloManobra: this.selectedForm.selectedQuantidadeManobra,
qtdModuloEquipamento: this.selectedForm.selectedQuantidadeEquipamento,
acao: '',
});
},
adicionarSubestacao() {
this.tableSubestacaoItens.push({
id: this.generateId(),
nomeSubestacao: this.selectedForm.selectedNomeSubestacao,
dataCotacao: this.selectedForm.selectedAno + "/" + this.selectedForm.selectedMes,
arranjo: this.selectedForm.selectedArranjo,
qtdModuloManobra: this.selectedForm.selectedQuantidadeManobra,
qtdModuloEquipamento: this.selectedForm.selectedQuantidadeEquipamento,
acao: '',
});
},
salvarOrcamentoCompleto() {
const orcamentoData = {
nomeOrcamento: this.selectedForm.selectedNomeOrcamento,
nomeSubestacao: this.selectedForm.selectedNomeSubestacao,
macroregiao: this.selectedForm.selectedMacroregiao,
estado: this.selectedForm.selectedEstado,
ano_referencia: this.selectedForm.selectedAno,
mes_referencia: this.selectedForm.selectedMes,
tipo_instalacao: this.selectedForm.selectedTipoInstalacao,
tensaoPrimaria: this.selectedForm.selectedTensaoPrimaria,
arranjo: this.selectedForm.selectedArranjo,
modulosManobra: this.tableModuloManobraItens,
modulosEquipamento: this.tableModuloEquipamentoItens,
};

http.post('/cadastrarOrcamento', orcamentoData)
.then(response => {
console.log(response);
alert('Orçamento completo adicionado com sucesso!');
})
.catch(error => {
console.error('Erro ao adicionar o orçamento:', error);
});
},
editItem(item) {
this.editableOrcamentoId = item.id;
this.editableOrcamento = { ...item };
},
saveItem(item) {
const index = this.tableSubestacaoItens.findIndex(i => i.id === item.id);
if (index !== -1) {
this.tableSubestacaoItens[index] = { ...item };
}
this.editableOrcamentoId = null;
},
deleteItem(orcamentoId) {
this.tableSubestacaoItens = this.tableSubestacaoItens.filter(item => item.id !== orcamentoId);
},
},
data() {
return {
showManobra: false,
showEquipamento: false,
selectedForm: {
selectedNomeOrcamento: null,
selectedNomeSubestacao: null,
selectedAno: null,
selectedMes: null,
selectedMacroregiao: null,
selectedEstado: null,
selectedTipoInstalacao: null,
selectedTensaoPrimaria: null,
selectedArranjo: null,
selectedSincDisjuntor: null,
selectedTipoAplicacao: null,
selectedTipo: "",
selectedQuantidadeManobra: null,
selectedTipoEquipamento: null,
selectedQuantidadeEquipamento: null,
},
subestacaoForm: {
macroregiao: ["Centro Oeste", "Norte", "Nordeste", "Sudeste", "Sul", "Brasil"],
ano: [2020, 2021, 2022, 2023],
mes: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
tipoInstalacao: ["Convencional", "Compacta", "SF6"],
tensaoPrimaria: [13.8, 69, 138, 230, 345, 500],
arranjo: {
13.8: ["BPT", "BS"],
69: ["BD5", "BPT", "BS"],
138: ["BD4", "BD5", "BPT", "BS"],
230: ["BD4", "BD5", "BPT"],
345: ["AN", "BD4", "DJM"],
500: ["AN", "BDDD", "DJM"],
},
sincDisjuntor: { true: "Sim", false: "Não" },
tipoAplicacao: ["Medição", "Proteção", "Med./Prot."],
tipo: ["CCP - Conexão de Banco de Capacitores Paralelo",
"CCSS - Conexão de capacitor serie",
"CRL - Conexão de Reator de Linha Manobrável",
"CT - Conexão de transformador"],
tipoEquipamento: ["BCP - Banco de capacitores derivação",
"RA - Reator de Aterramento",
"RT - Reator trifásico",
"TM - Auto/Transformador monofásico"],
},
estadosPorMacroregiao: {
"Centro Oeste": ["Goiás", "Mato Grosso", "Mato Grosso do Sul"],
"Norte": ["Acre", "Amapá", "Amazonas", "Pará"],
"Nordeste": ["Alagoas", "Bahia", "Ceará", "Pernambuco", "Rio Grande do Norte", "Sergipe"],
"Sudeste": ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
"Sul": ["Paraná", "Rio Grande do Sul", "Santa Catarina"],
"Brasil": ["Acre", "Alagoas", "Amapá", "Bahia", "Pernambuco"],
},
tableModuloManobraItens: [
],
tableModuloManobraColunas: [
{ key: 'tipo', label: 'Tipo' },
{ key: 'quantidade', label: 'Quantidade' },
{ key: 'acao', label: 'Ação' },
],
tableModuloEquipamentoItens: [
],
tableModuloEquipamentoColunas: [
{ key: 'equipamento', label: 'Equipamento' },
{ key: 'quantidade', label: 'Quantidade' },
{ key: 'acao', label: 'Ação' },
],
tablePatioItens: [
],
tablePatioColunas: [
{ key: 'patio', label: 'Pátio' },
{ key: 'tensaoPrimaria', label: 'Tensão Primária' },
{ key: 'arranjo', label: 'Arranjo' },
{ key: 'qtdModuloManobra', label: 'Qtd. Módulos de Manobra' },
{ key: 'qtdModuloEquipamento', label: 'Qtd. Módulos de Equipamento' },
{ key: 'acao', label: 'Ação' },
],
tableSubestacaoItens: [
],
tableSubestacaoColunas: [
{ key: 'nomeSubestacao', label: 'Nome Subestação' },
{ key: 'dataCotacao', label: 'Data Cotação' },
{ key: 'qtdModuloManobra', label: 'Qtd. Módulos de Manobra' },
{ key: 'qtdModuloEquipamento', label: 'Qtd. Módulos de Equipamento' },
{ key: 'acao', label: 'Ação' },
],
nextId: 1,
editableOrcamentoId: null,
editableOrcamento: {},
}
}
}
</script>

<style scoped>
h1,
h2,
h3 {
padding: 20px;
color: black;
}

.cadastrar-orcamentos {
display: flex;
align-items: center;
flex-direction: column;
color: #0D9488;
}

.cadastro {
width: 91%;
}

.subestacao {
background-color: #f5f5f5;
padding: 6%;
}

label {
font-size: 22px;
}

.label-place {
font-size: 15px;
margin-top: 20px;
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

.dados-patio {
background-color: #ececec;
padding: 2%;
}

.manobra,
.equipamento {
background-color: #e7e7e7;
padding: 2%;
}

button {
background-color: #46b341;
width: 40px;
color: #FFF;
font-size: 20px;
border: none;
border-radius: 15px;
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
}

.icon-container {
padding: 10px 0%;
padding-right: 20%;
display: inline-block;
}

.botao-estilo-cancelar {
background-color: #b8b5b5;
margin-right: 30px;
}

.gerar-excel {
display: flex;
justify-content: center;
margin: 30px 35%;
background-color: #46b341;
padding: 15px 20px;
border-radius: 15px;
}

.salva-subestacao {
margin-top: 100px;
}

.column {
display: flex;
flex-direction: column;
}

.columnMarginR {
margin-right: 80px;
}

.row {
display: flex;
flex-direction: row;
justify-content: space-between;
}

.marginBottom {
margin-bottom: 40px;
}
</style>
