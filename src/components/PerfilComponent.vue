<template>
    <section class="telaPerfil">
        <div class="perfil">
            <h1>Perfil</h1>
            <div class="secoes row">
                <section class="secaoUm">
                    <div class="column" style="align-items: center;">
                        <img src="../assets/PerfilADM.png" alt="">
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

input {
    height: 40px;
    border: none;
    margin-top: 30px;
    font-size: 25px;
    background-color: #FFF;
}

.column {
    display: flex;
    flex-direction: column;
}
.row {
    display: flex;
    flex-direction: row;
}

.marginBottom {
    margin-bottom: 40px;
}
</style>
