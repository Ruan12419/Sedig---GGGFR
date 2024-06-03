<template>
    <section class="telaPerfil">
        <div class="perfil">
            <h1>Perfil</h1>
            <div class="secoes row">
                <section class="secaoUm">
                    <div class="column" style="align-items: center;">
                        <img v-if="isAdmin" src="../assets/PerfilADM.png" alt="">
                        <img v-else src="../assets/PerfilUsuario.png" alt="">
                        <h2>{{ usuario.nome }}</h2>
                        <div class="chavePasse column">
                            <span>Chave Passe: </span>
                            <span class="passe">{{ usuario.chavePasse }}</span>
                        </div>
                        <span class="instrucaoPasse">A Chave Passe é gerada automaticamente se você é usuário
                            comum.</span>
                    </div>
                </section>
                <section class="secaoDois">
                    <div class="email column marginBottom">
                        <label for="email">Email </label>
                        <div class="row" style="align-items: baseline;">
                            <input type="text" style="width: 100%; margin-right: 20px;" v-model="usuario.email" disabled>
                        </div>
                    </div>
                    <div class="cpf column marginBottom">
                        <label for="cpf">CPF </label>
                        <input type="text" style="width: 100%; margin-right: 20px;" v-model="usuario.cpf" disabled>
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
import http from '@/http';
import { mapGetters } from 'vuex';


export default {
    name: "PerfilComponent",
    components: {
    },
    data() {
        return {
            usuario: {
                email: "",
                cpf: "",
                chavePasse: "",
                nome: ""
            },
            isEditable: false
        };
    },
    computed: {
    ...mapGetters(['isAdmin']),
  },
    methods: {
        fetchUserData() {
            http.get('/usuario')
                .then(response => {
                    this.usuario = response.data;
                })
                .catch(error => {
                    console.error("Houve um erro ao buscar os dados do usuário:", error);
                });
        }
    },
    created() {
        this.fetchUserData();
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
