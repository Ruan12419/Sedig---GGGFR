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
                                <select id="macroregiao">
                                    <!-- -->
                                </select>
                            </div>
                            <div class="column">
                                <label for="estado">Estado</label>
                                <select id="estado">
                                    <!-- -->
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="column">
                        <label for="dataRef">Data de Referência: </label>
                        <div class="row">
                            <div class="column columnMarginR">
                                <label for="ano">Ano</label>
                                <select id="ano">
                                    <!-- -->
                                </select>
                            </div>
                            <div class="column marginBottom">
                                <label for="mes">Mês</label>
                                <select id="mes">
                                    <!-- -->
                                </select>
                            </div>
                        </div>
                        <label for="tipoInstalacao">Tipo de instalação: </label>
                        <div class="tipoInstSub marginBottom">
                            <select id="tipoInstalacao">
                                <!-- -->
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
                                <select id="tensaoPrimaria">
                                    <!-- -->
                                </select>
                            </div>
                            <div class="arranjo column">
                                <label for="arranjo">Arranjo: </label>
                                <select id="arranjo">
                                    <!-- -->
                                </select>
                            </div>
                        </div>
                        <div class="column"></div>
                    </div>
                    <h3 @click="showManobra = !showManobra">
                        Módulo de Manobra <button>{{ showManobra ? '^' : '>' }}</button>
                    </h3>
                    <section class="moduloManobra row" v-if="showManobra">
                        <div class="column">
                            <div class="row">
                                <div class="sincDisjuntor column columnMarginR">
                                    <label for="nome">Sincronização Disjuntor: </label>
                                    <select id="sincDisjuntor">
                                        <!-- -->
                                    </select>
                                </div>
                                <div class="tipoAplicacao column marginBottom">
                                    <label for="regiao">Tipo Aplicação: </label>
                                    <select id="tipoAplicacao">
                                        <!-- -->
                                    </select>
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
                                <select id="tipo" style="width: 100%;">
                                    <!-- -->
                                </select>
                            </div>
                            <div class="column" style="align-items: flex-end;">
                            <label for="addModuloDeManobra">Adicionar Módulo de Manobra: </label>
                            <div class="botao-estilo">
                            <font-awesome-icon icon="add" :font-size="20" color="white" />
                            </div>
                            </div>
                        </div>
                    </section>
                    <div class="tableModuloManobra" v-if="showManobra">
                        <TabelaComponent :items="tableModuloManobraItens" :colunas="tableModuloManobraColunas" />
                    </div>
                    <hr>
                    <h3 @click="showEquipamento = !showEquipamento">Módulo de Equipamento <button>{{ showEquipamento ?
                            '^' : '>' }}</button></h3>
                    <section class="moduloEquipamento row" v-if="showEquipamento">
                        <div class="row">
                            <div class="tipoEquipamento column columnMarginR">
                                <label for="nome">Tipo de Equipamento: </label>
                                <select id="tipoEquipamento" style="width: 500px;">
                                    <!-- -->
                                </select>
                            </div>
                            <div class="moduloEquipamentoQuantidade column">
                                <label for="regiao">Quantidade: </label>
                                <input type="text" style="width: 300px;">
                            </div>
                        </div>
                        <div class="column">
                        <div class="column" style="align-items: flex-end;">
                            <label for="addModuloDeManobra">Adicionar Módulo de Equipamento: </label>
                            <div class="botao-estilo">
                                <font-awesome-icon icon="add" :font-size="20" color="white" />
                            </div>
                            </div>
                        </div>
                    </section>
                    <div class="tableModuloEquipamento" v-if="showEquipamento">
                        <TabelaComponent :items="tableModuloEquipamentoItens"
                            :colunas="tableModuloEquipamentoColunas" />
                    </div>
                    <hr>
                    <section class="salva-patio row" style="justify-content: flex-end;">
                        <div class="column">
                            <label for="addPatio">Cancelar: </label>
                            <div class="botao-estilo botao-estilo-cancelar" @click="showAlert">
                                <font-awesome-icon icon="arrow-left" :font-size="20" color="white" />
                            </div>
                        </div>
                        <div class="column">
                            <label for="addPatio">Adicionar Pátio: </label>
                            <div class="botao-estilo">
                                <font-awesome-icon icon="add" :font-size="20" color="white" />
                            </div>
                        </div>
</section>

                    <div class="tablePatio">
                        <TabelaComponent :items="tablePatioItens" :colunas="tablePatioColunas" />
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
      alert('Certeza?');
    },
  },
    data() {
        return {
            showManobra: false,
            showEquipamento: false,
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
                {
                    patio: "", tensaoPrimaria: "", arranjo: "",
                    qtdModuloManobra: "", qtdModuloEquipamento: "", acao: ""
                },
                {
                    patio: "", tensaoPrimaria: "", arranjo: "",
                    qtdModuloManobra: "", qtdModuloEquipamento: "", acao: ""
                },
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
                {
                    nomeSubestacao: "", dataCotacao: "", qtdModuloManobra: "",
                    qtdModuloEquipamento: "", acao: ""
                },
                {
                    nomeSubestacao: "", dataCotacao: "", qtdModuloManobra: "",
                    qtdModuloEquipamento: "", acao: ""
                },
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
    padding: 3%;
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

button {
    background-color: #46b341;
    width: 40px;
    color: #FFF;
    font-size: 20px;
    border: none;
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
