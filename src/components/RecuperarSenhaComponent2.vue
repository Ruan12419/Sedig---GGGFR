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
                <div class="info">
                    <h5 class="title-h5">Obrigado! se o endereço de email que você forneceu estiver associado a <span class="line-2">uma conta em nosso sistema, nós enviaremos um link de </span><br> <span class="line-3">recuperação de senha para ele.</span></h5>
                 </div>   
                
                            <div class="botaoLogin">
                                <div class="column">
                        <div class="botao-estilo" @click="$emit('tentar-novamente')">
                            <router-link to="/recuperarSenha-2" class="nav-link">Tentar novamente</router-link>
                        </div>
                        <div class="botao-estilo-2" @click="$emit('login')">
                            <router-link to="/recuperarSenha-2" class="nav-link">Login</router-link>
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
    height: 280px;
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
    margin-top: 70px;
    margin-left: 80px;
    width: 130px;
    height: 40px;
    background-color: rgb(181, 181, 181);
    padding: 1px 20px;
    border-radius: 15px;
}

.botao-estilo-2 {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin-left: auto;
    margin-right: 80px;
    margin-top: -42px;
    width: 130px;
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
    font-size: 0.9em;
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

.line-2 {
    text-align: center;
}

.line-3 {
    align-items: center;
}
</style>