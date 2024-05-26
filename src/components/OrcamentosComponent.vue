<template>
    <section class="cadastrar-orcamentos">
    <div class="cadastro">
    <h1>Cadastrar Orçamentos</h1>
    <section class="subestacao">
    <section class="row">
    <div class="column">
    <div class="nomeSubestacao column marginBottom">
    <label for="nome">Nome Subestação: </label>
    <input type="text">
    </div>
    <label for="regiao">Região</label>
    <div class="row">
    <div class="column columnMarginR">
    <label for="estado">Macroregião</label>
    <input type="text" placeholder="macroregiao">
    </div>
    <div class="column">
    <label for="estado">Estado</label>
    <input type="text">
    </div>
    </div>
    </div>
    <div class="column">
    <label for="dataRef">Data de Referência: </label>
    <div class="row">
    <div class="column columnMarginR">
    <label for="ano">Ano</label>
    <input type="text">
    </div>
    <div class="column marginBottom">
    <label for="mes">Mês</label>
    <input type="text">
    </div>
    </div>
    <label for="tipoInstalacao">Tipo de instalação: </label>
    <div class="tipoInstSub marginBottom">
    <input type="text">
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
    <input type="text" placeholder="kV">
    </div>
    <div class="arranjo column">
    <label for="arranjo">Arranjo: </label>
    <input type="text" placeholder="kV">
    </div>
    </div>
    <div class="column"></div>
    </div>
    <h3>Módulo de Manobra</h3>
    <section class="row">
    <div class="column">
    <div class="row">
    <div class="sincDisjuntor column columnMarginR">
    <label for="nome">Sincronização Disjuntor: </label>
    <input type="text">
    </div>
    <div class="tipoAplicacao column marginBottom">
    <label for="regiao">Tipo Aplicação: </label>
    <input type="text">
    </div>
    </div>
    <div class="moduloManobraQuantidade column">
    <label for="regiao">Quantidade: </label>
    <input type="text">
    </div>
    </div>
    <div class="column" style="width: 35%">
    <div class="moduloManobraTipo column marginBottom">
    <label for="nome">Tipo: </label>
    <input type="text">
    </div>
    <label for="addModuloDeManobra">Adicionar Módulo de Manobra: </label>
    icone de add
    <font-awesome-icon icon="add" :font-size="20" color="green" />
    </div>
    </section>
    <div class="tableModuloManobra">
        <TabelaComponent :items="tableModuloManobraItens" :colunas="tableModuloManobraColunas" />
    </div>
    <hr>
    <h3>Módulo de Equipamento</h3>
    <section class="row">
    <div class="row">
    <div class="tipoEquipamento column columnMarginR">
    <label for="nome">Tipo de Equipamento: </label>
    <input type="text">
    </div>
    <div class="moduloEquipamentoQuantidade column">
    <label for="regiao">Quantidade: </label>
    <input type="text">
    </div>
    </div>
    <div class="column">
    <label for="addModuloDeManobra">Adicionar Módulo de Equipamento: </label>
    icone de add
    <font-awesome-icon icon="add" :font-size="20" color="green" />
    </div>
    </section>
    <div class="tableModuloEquipamento">
    <TabelaComponent :items="tableModuloEquipamentoItens" :colunas="tableModuloEquipamentoColunas" />
    </div>
    <hr>
    <section class="salva-patio">
        <label for="addPatio">Cancelar: </label>
        icone de arrowback
        <font-awesome-icon icon="arrow-left" :font-size="20" color="green" />
        <label for="addPatio">Adicionar Pátio: </label>
    icone de add
    <font-awesome-icon icon="add" :font-size="20" color="green" />
    </section>
    <div class="tablePatio">
        <TabelaComponent :items="tablePatioItens" :colunas="tablePatioColunas" />
    </div>
    </section>
    <hr>
    <section class="salva-subestacao">
        <label for="addSubestacao">Cancelar: </label>
        icone de arrowback
        <font-awesome-icon icon="arrow-left" :font-size="20" color="green" />
        <label for="addSubestacao">Adicionar Subestação: </label>
        icone de add
        <font-awesome-icon icon="add" :font-size="20" color="green" />
    </section>
    <div class="tableSubestacao">
        <TabelaComponent :items="tableSubestacaoItens" :colunas="tableSubestacaoColunas" />
    </div>
    </section>
    <div></div>
    
    </div>
    <div></div>
    </section>
    <section class="gerar-excel">
    <label for="gerarExcel"></label>
    <font-awesome-icon icon="file-excel" :font-size="45" color="white" />
    </section>
    
    </template>
    
    
    

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faAdd, faArrowLeft, faPlus, faFileExcel } from '@fortawesome/free-solid-svg-icons'
import TabelaComponent from "./TabelaComponent.vue"
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' 

library.add(faAdd, faArrowLeft, faPlus, faFileExcel )
export default {
name: "OrcamentosComponent",
components: {
FontAwesomeIcon, 
TabelaComponent, 
},
data() {
return {
showDropdown: false, 
tableModuloManobraItens: [
    { tipo: "", quantidade: "", acao: "" }, 
    { tipo: "", quantidade: "", acao: "" }, 
], 
tableModuloManobraColunas: [
    { key: 'tipo', label: 'Tipo' },
    { key: 'quantidade', label: 'Quantidadese' },
    { key: 'acao', label: 'Ação' },
], 
tableModuloEquipamentoItens: [
        { elemento: "", quantidade: "", acao: "" }, 
        { elemento: "", quantidade: "", acao: "" }, 
      ],
tableModuloEquipamentoColunas: [
    { key: 'elemento', label: 'Elemento' },
    { key: 'quantidade', label: 'Quantidade' },
    { key: 'acao', label: 'Ação' },
], 
tablePatioItens: [
        { patio: "", tensaoPrimaria: "", arranjo: "", 
        qtdModuloManobra: "", qtdModuloEquipamento: "", acao: "" }, 
        { patio: "", tensaoPrimaria: "", arranjo: "", 
        qtdModuloManobra: "", qtdModuloEquipamento: "", acao: "" }, 
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
    { nomeSubestacao: "", dataCotacao: "", qtdModuloManobra: "", 
    qtdModuloEquipamento: "", acao: "" }, 
    { nomeSubestacao: "", dataCotacao: "", qtdModuloManobra: "", 
    qtdModuloEquipamento: "", acao: "" }, 
],
tableSubestacaoColunas: [
    { key: 'nomeSubestacao', label: 'Nome Subestação' },
    { key: 'dataCotacao', label: 'Data Cotação' },
    { key: 'qtdModuloManobra', label: 'Qtd. Módulos de Manobra' },
    { key: 'qtdModuloEquipamento', label: 'Qtd. Módulos de Equipamento' },
    { key: 'acao', label: 'Ação' },
], 
}
}
}
</script>

<style scoped>
h1, h2, h3 {
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
padding: 3%;
}

input {
height: 40px;
border: none;
margin-top: 30px;
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
