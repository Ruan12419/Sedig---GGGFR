<template>
    <section class="row">
      <HeaderLateralComponent />
      <section class="cadastrarNovaSenha column">
        <div class="title">
          <span class="to-recover">{{ title }}</span>
        </div>
        <div class="CNSBody column">
          <h5 class="title-h5">{{ message }}</h5>
          <p class="paragraph" v-if="showInput">{{ instructions }}</p>
          <div v-if="showInput">
            <input type="text" id="email" class="input-email column">
          </div>
          <div class="botaoEnviarEmail" v-if="showInput">
            <div class="column" style="align-items: center">
              <div class="botao-estilo" @click="sendEmail">
                <span class="nav-link">{{ buttonText }}</span>
              </div>
            </div>
          </div>
          <div class="botaoTentarNovamente" v-else>
            <div class="column">
              <div class="botao-estilo tentarNovamente" @click="tryAgain">
                <router-link to="/recuperarSenha" class="nav-link">Tentar novamente</router-link>
              </div>
              <div class="botao-estilo-2" @click="login">
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
import HeaderLateralComponent from "./HeaderLateralComponent.vue";

  export default {
    name: "RecuperarSenhaComponent",
    components: {
        HeaderLateralComponent, 
    },
    data() {
      return {
        showInput: true,
        title: "Recuperar Senha",
        message: "Esqueceu sua senha? Não se preocupe, estamos aqui para te ajudar.",
        instructions: "Por favor, insira o seu endereço de email abaixo. Enviaremos um link para o seu email que permitirá que você redefina sua senha.",
        buttonText: "Enviar",
        footerMessage: "Se você não receber o email em alguns minutos, verifique sua pasta de spam ou tente novamente."
      };
    },
    methods: {
      sendEmail() {
        this.showInput = false;
        this.title = "Recuperar Senha";
        this.message = "Obrigado! Se o endereço de email que você forneceu estiver associado a uma conta em nosso sistema, nós enviaremos um link de recuperação de senha para ele.";
        this.footerMessage = "Se você não receber o email em alguns minutos, verifique sua pasta de spam ou tente novamente.";
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

.CNSBody {
    height: fit-content;
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
    margin-top: 30px;
    width: 70px;
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

.paragraph {
    font-weight: 600;
    margin-top: -5px;
}

.input-email {
    width: 100%;
}
.cadastrarNovaSenha {
    margin: auto;
    margin-top: 10%;
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
</style>