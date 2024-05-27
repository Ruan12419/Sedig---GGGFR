<template>
    <section class="row">
        <section class="header column" style="align-items: center; justify-content: center">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b3/Eletrobras.png">
        </section>
        <section class="register column">
            <div class="title">
                <span>Cadastro</span>
            </div>
            <div class="registerBody column">
                <label for="nomeCompleto">Nome Completo <span class="asterisk">*</span></label>
                <label for="nome-ex" class="label-place">Ex: João Silva Santos</label>
                <input type="text" id="nomeCompleto" class="input-nome">
                
                <div class="row">
                    <div class="column">
                        <label for="cpf">CPF <span class="asterisk">*</span></label>
                        <label for="cpf-ex" class="label-place">Ex: xxx.xxx.xxx-xx</label>
                        <input type="text" id="cpf" v-model="cpf" @input="formatarCPF" maxlength="14" class="input-cpf">
                    </div>
                    <div class="column-chavePasse">
                        <label for="chavePasse"> <span class="name-chavePasse">Chave Passe</span></label>
                        <input type="text" id="chavePasse" class="input-chavePasse" maxlength="14">
                    </div>
                </div>
                
                <div class="row">
                    <div class="column">
                        <label for="email">Email <span class="asterisk">*</span></label>
                        <input type="text" id="email" class="input-email">
                    </div>
                    <div class="column-estado">
                        <label for="estado"><span class="name-estado">Estado *</span></label>
                        <br>
                        <label for="uf" class="label-place-3">UF</label>
                        <select id="estado" class="input-uf">
                            <option disabled selected></option>
                            <option value="AC">AC</option>
                            <option value="AL">AL</option>
                            <option value="AP">AP</option>
                            <option value="AM">AM</option>
                            <option value="BA">BA</option>
                            <option value="CE">CE</option>
                            <option value="DF">DF</option>
                            <option value="ES">ES</option>
                            <option value="GO">GO</option>
                            <option value="MA">MA</option>
                            <option value="MT">MT</option>
                            <option value="MS">MS</option>
                            <option value="MG">MG</option>
                            <option value="PA">PA</option>
                            <option value="PB">PB</option>
                            <option value="PR">PR</option>
                            <option value="PE">PE</option>
                            <option value="PI">PI</option>
                            <option value="RJ">RJ</option>
                            <option value="RN">RN</option>
                            <option value="RS">RS</option>
                            <option value="RO">RO</option>
                            <option value="RR">RR</option>
                            <option value="SC">SC</option>
                            <option value="SP">SP</option>
                            <option value="SE">SE</option>
                            <option value="TO">TO</option>
                        </select>
                    </div>
                    <div class="column-estado">
                        <label for="cidade" class="label-place-2">Cidade</label>
                                <input type="text" id="cidade" class="input-cidade">
                            </div>
                        </div>
                        
                        <label for="senha" class="senha">Senha <span class="asterisk">*</span></label>
                        <input type="password" id="senha" class="input-senha">
                        
                        <label for="confirmarSenha" class="confirmar-senha">Confirmar Senha <span class="asterisk">*</span></label>
                <input type="password" id="confirmarSenha" class="input-confirmarSenha">
                
                <div class="botaoRegister">
                    <div class="column" style="align-items: center">
                        <div class="botao-estilo" @click="$emit('register')">
                            <router-link to="/inicio" class="nav-link">Cadastrar-se</router-link>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <router-link to="/login" class="nav-link-2">Já possui cadastro? Faça Login</router-link>
                </div>
            </div>
        </section>
    </section>
</template>

<script>
export default {
    name: "RegisterComponent",
    data() {
        return {
            cpf: ''
        };
    },
    methods: {
        formatarCPF() {
            let cpfLimpo = this.cpf.replace(/[^\d]/g, '');
            
            cpfLimpo = cpfLimpo.substring(0, 11);
            
            cpfLimpo = cpfLimpo.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
            
            this.cpf = cpfLimpo;
        }
    }
};
</script>

<style scoped>
.header {
    height: 115vh !important;
    width: 350px;
    background-color: #6BC9DB;
}

img {
    width: 80%;
    margin-bottom: 180px;
}

.register {
    margin: auto;
    margin-top: 3%;
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

.registerBody {
    height: 650px;
    background-color: #f5f5f5;
    padding: 4%;
}

label {
    font-size: 18px;
    color: #0D9488;
}

input, select {
    border: none;
}

.botao-estilo {
    width: 150px;
    height: 40px;
    background-color: #46b341;
    border-radius: 15px;
    margin-top: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-left: auto;
    color: white;
}

.nav-link {
    text-decoration: none;
    color: white;
}

.nav-link-2 {
    color: #109dee;
    font-size: 15px;
    text-decoration: none;
    margin-top: -30px;
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

.asterisk {
    color: red;
    margin-left: -20px;
}

.label-place {
    font-size: 15px;
    margin-top: 20px;
}

.label-place-2 {
    font-size: 10px;
    margin-top: 30px;
    margin-bottom: 50px;
}

.label-place-3 {
    font-size: 10px;
    margin-left: 46px;
    margin-top: -8px;
}

.input-nome {
    height: 35px;
    margin-top: 10px;
    margin-bottom: 30px;
}

.input-cpf {
    width: 280px;
    height: 30px;
    margin-top: 10px;
    margin-bottom: 30px;
}

.column-chavePasse {
    margin-right: 5px;
    display: flex;
    flex-direction: column;
}

.input-chavePasse {
    height: 30px;
    width: 200px;
    margin-left: 20px;
    margin-top: 47px;
    margin-bottom: 30px;
}

.input-email {
    width: 280px;
    height: 30px;
    margin-top: 30px;
    margin-bottom: 30px;
}

.column-estado {
    margin-right: 5px;
    display: flex;
    flex-direction: column;
}

.name-estado {
    margin-left: 25px
}

.input-uf {
    width: 50px;
    height: 32px;
    margin-left: 45px;
    margin-top: 10px;
    margin-bottom: 30px;  
}

.input-cidade {
    width: 100px;
    height: 30px;
    margin-top: -40px;
    margin-bottom: 30px;
}

.input-senha {
    height: 35px;
    margin-top: 10px;
    margin-bottom: 30px;
}

.input-confirmarSenha {
    height: 35px;
    margin-top: 10px;
    margin-bottom: 30px;
}
</style>