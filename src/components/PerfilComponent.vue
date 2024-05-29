<template>
    <section class="telaPerfil">
        <div class="perfil">
            <h1>Perfil</h1>
            <div class="secoes row">
                <section class="secaoUm">
                    <div class="column" style="align-items: center;">
                        <img src="" alt="">
                        <h2>João Silva Santos</h2>
                        <div class="chavePasse column">
                            <span>Chave Passe: </span>
                            <span class="passe">A000022MG-325</span>
                        </div>
                        <span class="instrucaoPasse">A Chave Passe é gerada automaticamente se você é usuário
                            comum.</span>
                    </div>
                </section>
                <section class="secaoDois">
                    <div class="email column marginBottom">
                        <label for="email">Email </label>
                        <div class="row" style="align-items: baseline;">
                            <input type="text" style="width: 100%; margin-right: 20px;" v-model="emailEdit"
                                :disabled="!isEditable">
                            <font-awesome-icon icon="edit" :font-size="28" color="green" @click="toggleEdit" />
                        </div>
                    </div>
                    <div class="cpf column marginBottom">
                        <label for="cpf">CPF </label>
                        <input type="text" style="width: 100%; margin-right: 20px;" v-model="cpfModel" disabled>
                    </div>
                    <div class="alterarSenha">
                        <div class="alterarSenha row" style="justify-content: flex-start">
                            <router-link to="/recuperarSenha" class="nav-link">Alterar senha</router-link>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </section>

</template>

<script>
import { library } from '@fortawesome/fontawesome-svg-core'
import { faEdit } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faEdit)
export default {
    name: "PerfilComponent",
    components: {
        FontAwesomeIcon
    },
    data() {
        return {
            emailEdit: "Joao.da-silva-santos@sedig.br",
            isEditable: false,
            cpfModel: "xxx.632.xxx - xx"
        };
    },
    methods: {
        toggleEdit() {
            this.isEditable = !this.isEditable;
        }
    }
}
</script>


<style scoped>
h1 {
    padding: 20px;
    color: black;
}

.telaPerfil {
    display: flex;
    align-items: center;
    flex-direction: column;
    color: #0D9488;
}

.perfil {
    width: 91%;
}
.secoes {
    height: 75vh;
}

.secaoUm {
    width: 30%;
    background-color: #e7e7e7;
    color: #000;
}

img {
    width: 200px;
    height: 200px;
    border-radius: 100%;
    background-color: #000;
    margin-top: 40px;
}

.chavePasse {
    background-color: #e0e0e0;
    width: 70%;
    padding: 3%;
}

.chavePasse .passe {
    font-size: 32px;
    color: #9c9c9c;
}

.instrucaoPasse {
    width: 70%;
    padding: 7%;
}

.secaoDois {
    background-color: #f5f5f5;
    width: 100%;
    margin-left: 10px;
    padding: 3%;
}

.email,
.cpf {
    width: 50%;
}
.alterarSenha {
    font-size: 15px;
    text-decoration: none;
}
.nav-link {
    color: #109dee;
    text-decoration: none;
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
    font-size: 25px;
    background-color: #FFF;
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

.salva-secaoDois {
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
}

.marginBottom {
    margin-bottom: 40px;
}
</style>
