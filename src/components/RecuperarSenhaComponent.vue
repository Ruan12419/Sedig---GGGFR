<template>
    <section class="row">
        <section class="header column" style="align-items: center; justify-content: center">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b3/Eletrobras.png">
        </section>
        <section class="login column">
            <div class="title">
                <span class="to-recover">Recuperar Senha</span>
            </div>
            <div class="loginBody column">    
                            <h5 class="title-h5">Esqueceu sua senha? Não se preocupe, estamos aqui para te ajudar.</h5>
                            <p class="paragraph">Por favor, insira o seu endereço de email abaixo. <br> Enviaremos um link para o seu email que permitirá <br> que você redefina sua senha.</p>
                            <div>
                        <input type="text" id="email" class="input-email">
                    </div>
                            <div class="botaoLogin">
                                <div class="column" style="align-items: center">
                        <div class="botao-estilo" @click="$emit('enviar')">
                            <router-link to="/recuperarSenha2" class="nav-link">Enviar</router-link>
                        </div>

                    </div>
                    
                </div>
                <div class="title-h6">
                    <h6>Se você não receber o email em alguns minutos, verifique sua pasta de spam ou tente novamente.</h6>
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
    width: 563px;
    padding: 2% 0%;
    font-size: 22px;
}

span {
    padding: 20px;
}

.loginBody {
    height: 330px;
    width: 530px;
    background-color: #f5f5f5;
    padding: 3%;
}

input {
    height: 40px;
    border: none;
    margin-top: 30px;
}

.botao-estilo {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 70px;
    height: 40px;
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

.to-recover {
    font-weight: bold;
}

.title-h5 {
    font-size: 1em;
    margin-right: auto;
}

.paragraph {
    font-weight: 600;
    margin-top: -5px;
}

.input-email {
    width: 55vh;
    height: 35px;
    margin-bottom: 30px;
}
</style>