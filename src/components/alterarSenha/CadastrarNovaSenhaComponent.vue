<template>
    <section class="row">
        <HeaderLateralComponent />
        <section class="login column">
            <div class="title">
                <span class="to-recover">{{ title }}</span>
            </div>
            <div class="loginBody column">
                <div class="mudarSenha column" v-if="mudarSenha">
                    <div class="column">
                        <label for="senha" class="senha">Nova Senha </label>
                        <input type="password" id="senha" class="input-senha">

                        <label for="confirmarSenha" class="confirmar-senha" style="margin-top: 40px;">Confirmar Nova
                            Senha </label>
                        <input type="password" id="confirmarSenha" class="input-senha">
                    </div>
                    <div class="column" style="align-items: center;">
                        <div class="botao-estilo" @click="alteraSenha">
                            <a class="nav-link">{{ buttonText }}</a>
                        </div>
                    </div>
                </div>
                <div class="botaoLogin column" v-else>
                    <div class="column" style="align-items: center;">
                        <h4>{{ message }}</h4>
                        <p>{{ instructions }}</p>
                    </div>
                    <div class="column" style="align-items: center;">
                        <div class="botao-estilo" @click="login">
                            <router-link to="/login" class="nav-link">Login</router-link>
                        </div>
                    </div>
                </div>
                <div class="title-h6">
                    <h6>{{ footerMessage }}</h6>
                </div>
            </div>
        </section>
    </section>
</template>

<script>
import HeaderLateralComponent from "../headers/HeaderLateralComponent.vue";

export default {
    name: "CadastrarNovaSenhaComponent",
    components: {
        HeaderLateralComponent,
    },
    data() {
        return {
            mudarSenha: true,
            title: "Recuperar Senha",
            buttonText: "Alterar Senha",
            footerMessage: "Se você não solicitou essa alteração de senha, entre em contato com nosso suporte imediatamente."
        };
    },
    methods: {
        alteraSenha() {
            this.mudarSenha = false;
            this.title = "Senha recuperada com sucesso";
            this.message = "Sua senha foi alterada com sucesso!";
            this.instructions = "Agora você pode fazer login com sua nova senha. Lembre-se de manter sua senha segura e não compartilhá-la com ninguém.";
            this.footerMessage = "Se você não solicitou essa alteração de senha, entre em contato com nosso suporte imediatamente.";
        },
        tryAgain() {
            this.showInput = true;
        },
        login() {
        }
    }
};
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
    width: 563px;
    padding: 2% 0%;
    font-size: 22px;
}

span {
    padding: 20px;
}

.loginBody {
    height: fit-content;
    width: 530px;
    background-color: #f5f5f5;
    padding: 3%;
}

label {
    font-size: 18px;
    color: #0D9488;
    margin-top: 15px;
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
    margin-top: 30px;
    width: 100px;
    height: 40px;
    background-color: #46b341;
    padding: 1px 20px;
    border-radius: 15px;
}

.tentarNovamente {
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

.tentarNovamente span {
    padding: 0;
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

.input-email,
.input-senha {
    width: 100%;
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

input {
    height: 40px;
    border: none;
    margin-top: 30px;
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

.line-2 {
    text-align: center;
}

.line-3 {
    align-items: center;
}

a {
    text-decoration: none;
}
</style>