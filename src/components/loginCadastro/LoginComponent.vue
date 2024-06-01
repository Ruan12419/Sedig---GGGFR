<template>
    <section class="row">
        <HeaderLateralComponent />
        <section class="login column">
            <div class="title">
                <span>Login</span>
            </div>
            <div class="loginBody column">
                <label for="email">Email</label>
                <input type="text" id="email" v-model="email">
                <label for="senha" class="inputtMarginTop">Senha</label>
                <input type="password" id="senha" v-model="senha">
                <div class="esqueceuSenha row" style="justify-content: flex-end">
                    <router-link to="/recuperarSenha" class="nav-link-2">Esqueceu a senha?</router-link>
                </div>
                <div class="botaoLogin">
                    <div class="column" style="align-items: center">
                        <div class="botao-estilo" @click="login">
                            <span class="nav-link">Login</span>
                        </div>
                    </div>
                </div>
                <div class="naoPossuiCadastro column" style="align-items: center;">
                    <router-link to="/cadastro" class="nav-link-2">Não possui conta? Cadastre-se</router-link>
                </div>
            </div>
        </section>
    </section>
</template>

<script>
import axios from 'axios';
import HeaderLateralComponent from "../headers/HeaderLateralComponent.vue"

export default {
    name: "LoginComponent",
    components: {
        HeaderLateralComponent,
    },
    data() {
        return {
            showDropdown: false, 
            email: "", 
            senha: "", 
        }
    }, 
    methods: {
        login() {
            const dadosLogin = {
                email: this.email,
                senha: this.senha
            };

            axios.post('http://127.0.0.1:8000/login', dadosLogin)
                .then(response => {
                    if (response.status === 200) {
                        this.$store.commit('SET_AUTHENTICATED', true); 
                        this.$router.push('/inicio');
                    }
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
}
</script>

<style scoped>
.login {
    margin: auto;
    margin-top: 10%;
}

.title {
    background-color: #F5FABF;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    width: 600px;
    padding: 2% 0%;
    font-size: 22px;
}

span {
    padding: 20px;
}

.loginBody {
    height: 400px;
    background-color: #f5f5f5;
    padding: 7%;
}

label {
    font-size: 18px;
    color: #0D9488;
}

input {
    height: 40px;
    border: none;
    margin-top: 30px;
}

.inputtMarginTop {
    margin-top: 40px;
}

.esqueceuSenha,
.naoPossuiCadastro {
    color: #109dee;
    font-size: 15px;
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

.nav-link {
    text-decoration: none;
    color: white;
}

.nav-link-2 {
    text-decoration: none;
    margin-top: 35px;
    color: #109dee;

}

.column {
    display: flex;
    flex-direction: column;
}

.row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>