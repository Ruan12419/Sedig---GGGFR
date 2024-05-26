<template>
    <section class="row">
        <section class="header column" style="align-items: center; justify-content: center">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b3/Eletrobras.png">
        </section>
        <section class="login column">
            <div class="title">
                <span>Login</span>
            </div>
            <div class="loginBody column">
                <label for="email">Email</label>
                <input type="text" id="email">
                <label for="senha" class="inputtMarginTop">Senha</label>
                <input type="text" id="senha">
                <div class="esqueceuSenha row" style="justify-content: flex-end">
                    <span>Esqueceu a senha?</span>
                </div>
                <div class="botaoLogin">
                    <div class="column" style="align-items: center">
                        <div class="botao-estilo" @click="$emit('logout')">
                            <router-link to="/inicio" class="nav-link">Login</router-link>
                        </div>

                    </div>
                </div>
                <div class="naoPossuiCadastro column" style="align-items: center;">
                    <span>Não possui cadastro? Cadastre-se</span>
                </div>
            </div>
        </section>
    </section>
</template>

<script>

export default {
    name: "LoginComponent",
    components: {
    },
    data() {
        return {
            showDropdown: false
        }
    }
}
</script>

<style scoped>
.header {
    height: 100vh !important;
    width: 350px;
    background-color: #6BC9DB;
}

img {
    width: 80%;
    margin-bottom: 180px;
}

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