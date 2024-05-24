<template>
    <section class="cadastrar-orcamentos">
        <div class="cadastro">
            <h1>Cadastrar Orçamentos</h1>
            <section class="subestacao">
                <section class="dados-subestacao">
                    <div class="left">
                        <div class="nomeSubestacao">
                            <label for="nome">Nome Subestação: </label>
                            <input type="text">
                        </div>
                        <label for="regiao">Região</label>
                        <div class="regiao">
                            <div class="column">
                                <label for="estado">Macroregião</label>
                                <input type="text" placeholder="macroregiao">
                            </div>
                            <div class="column">
                                <label for="estado">Estado</label>
                                <input type="text">
                            </div>
                        </div>
                    </div>
                    <div class="right">
                        <label for="dataRef">Data de Referência: </label>
                        <div class="dataReferencia">
                            <div class="column">
                            <label for="ano">Ano</label>
                            <input type="text">
                            </div>
                            <div class="column">
                            <label for="mes">Mês</label>
                            <input type="text">
                            </div>
                        </div>
                        <label for="tipoInstalacao">Tipo de instalação: </label>
                        <div class="tipoInstSub">
                            <input type="text">
                        </div>
                    </div>
                </section>
                <hr>
                <section class="dados-patio">
                    <h2>Pátio</h2>
                    <div class="left">
                        <div class="tensaoPrimaria">
                            <label for="tensaoPrimaria">Tensão Primária: </label>
                            <input type="text" placeholder="kV">
                        </div>
                        <div class="arranjo">
                            <label for="arranjo">Arranjo: </label>
                            <input type="text" placeholder="kV">
                        </div>
                    </div>
                    <h3>Módulo de Manobra</h3>
                    <section class="modulo-manobra">
                        <div class="left">
                            <div class="sincTipo">
                                <div class="sincDisjuntor">
                                    <label for="nome">Sincronização Disjuntor: </label>
                                    <input type="text">
                                </div>
                                <div class="tipoAplicacao">
                                    <label for="regiao">Tipo Aplicação: </label>
                                    <input type="text">
                                </div>
                            </div>
                            <div class="moduloManobraQuantidade">
                                <label for="regiao">Quantidade: </label>
                                <input type="text">
                            </div>
                        </div>
                        <div class="right">
                            <div class="moduloManobraTipo">
                                <label for="nome">Tipo: </label>
                                <input type="text">
                            </div>
                            <label for="addModuloDeManobra">Adicionar Módulo de Manobra: </label>
                            icone de add
                            <font-awesome-icon icon="add" :font-size="20" color="green" />
                        </div>
                        
                    </section>
                    <div class="tableModuloManobra">
                        <div class="title-table">
                        <table>
                            <thead>
                            <th>Tipo</th>
                            <th>Quantidade</th>
                            <th>Ação</th>
                            </thead>

                            <tbody>
                            <tr class="imp">
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            <tr class="par">
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
                    </div>
                    <hr>
                    <h3>Módulo de Equipamento</h3>
                    <section class="modulo-equipamento">
                        <div class="up">
                            <div class="left">
                            <div class="tipoEquipamento">
                                <label for="nome">Tipo de Equipamento: </label>
                                <input type="text">
                            </div>
                            <div class="moduloEquipamentoQuantidade">
                                <label for="regiao">Quantidade: </label>
                                <input type="text">
                            </div>
                            </div>
                            <div class="right">
                            <label for="addModuloDeManobra">Adicionar Módulo de Equipamento: </label>
                            icone de add
                            <font-awesome-icon icon="add" :font-size="20" color="green" />
                            </div>
                        </div>
                    </section>
                    <div class="tableModuloEquipamento">
                        <div class="title-table">
                        <table>
                            <thead>
                            <th>Tipo</th>
                            <th>Quantidade</th>
                            <th>Ação</th>
                            </thead>

                            <tbody>
                            <tr class="imp">
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            <tr class="par">
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
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
                        <div class="title-table">
                        <table>
                            <thead>
                            <th>Pátio</th>
                            <th>Tensão Primária</th>
                            <th>Arranjo</th>
                            <th>Qtd. Módulos de Manobra</th>
                            <th>Qtd. Módulos de Equipamento</th>
                            <th>Ação</th>
                            </thead>

                            <tbody>
                            <tr class="imp">
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            <tr class="par">
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
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
                    <div class="tablePatio">
                        <div class="title-table">
                        <table>
                            <thead>
                            <th>Nome Subestação</th>
                            <th>Data Cotação</th>
                            <th>Qtd. Módulos de Manobra</th>
                            <th>Qtd. Módulos de Equipamento</th>
                            </thead>

                            <tbody>
                            <tr class="imp">
                                <td></td>
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            <tr class="par">
                                <td></td>
                                <td></td>
                                <td></td>
                                <td>
                                <!-- <font-awesome-icon icon="edit" :font-size="20" color="green"/>
                                <font-awesome-icon icon="trash-alt" :font-size="20" color="red" />
                                -->
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        </div>
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
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' 

library.add(faAdd, faArrowLeft, faPlus, faFileExcel )
export default {
    name: "OrcamentosComponent",
    components: {
        FontAwesomeIcon
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

.cadastrar-orcamentos {
    display: flex;
    align-items: center;
    flex-direction: column;
    color: #0D9488;
}
h1, h2, h3 {
    color: black;
}


.cadastro {
    width: 91%;
}

.subestacao {
    background-color: #f5f5f4;
    padding: 3%;
}

.dados-subestacao {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

input {
    height: 40px;
    border: none;
    margin-top: 30px;
}
.nomeSubestacao {
    display: flex;
    flex-direction: column;
}
.dados-subestacao .left {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.dados-subestacao .left .regiao {
    display: flex;
    flex-direction: row;
}

.dados-subestacao .right {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.dados-subestacao .right .dataReferencia {
    display: flex;
    flex-direction: row;
}

.dados-patio .left {
    display: flex;
    flex-direction: row;
}

.dados-patio .left .tensaoPrimaria, .arranjo {
    display: flex;
    flex-direction: column;
}

.dados-patio .modulo-manobra {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.dados-patio .modulo-manobra .left {
    display: flex;
    flex-direction: column;
}
.dados-patio .modulo-manobra .left .sincTipo {
    display: flex;
}
.dados-patio .modulo-manobra .left .sincDisjuntor, .tipoAplicacao, .moduloManobraQuantidade, .right .moduloManobraTipo {
    display: flex;
    flex-direction: column;
}

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
  padding: 1.4% 7%;
  text-align: center;
  color: #000;
}
.font-awesome-icon {
  font-size: 200px !important;
  color: red !important;
}

.dados-patio .modulo-equipamento .up {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.dados-patio .modulo-equipamento .up .tipoEquipamento, .moduloEquipamentoQuantidade {
    display: flex;
    flex-direction: column;
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
</style>