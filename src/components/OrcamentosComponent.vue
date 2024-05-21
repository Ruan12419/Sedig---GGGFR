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
                        <div class="regiao">
                            <label for="regiao">Região</label>
                            <input type="text" placeholder="macroregiao">
                            <label for="estado">Estado</label>
                            <input type="text">
                        </div>
                    </div>
                    <div class="right">
                        <div class="dataReferencia">
                            <label for="dataRef">Data de Referência: </label>
                            <label for="ano">Ano</label>
                            <input type="text">
                            <label for="mes">Mês</label>
                            <input type="text">
                        </div>
                        <div class="tipoInstSub">
                            <label for="tipoInstalacao">Tipo de instalação: </label>
                            <input type="text">
                        </div>
                    </div>
                </section>
                <hr>
                <section class="dados-patio">
                    <h2>Pátio</h2>
                    <div class="left">
                        <div class="nomeSubestacao">
                            <label for="nome">Tensão Primária: </label>
                            <input type="text" placeholder="kV">
                        </div>
                        <div class="regiao">
                            <label for="regiao">Arranjo: </label>
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
                    <hr>
                    <section>Outro Módulo</section>
                </section>
            </section>
            <div></div>

        </div>
        <div></div>
    </section>
</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faAdd } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' 

library.add(faAdd)
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
    background-color: #DDD;
    padding: 3%;
}

.dados-subestacao {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
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
</style>