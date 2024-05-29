import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomeComponent.vue'
import Orcamentos from '../components/OrcamentosComponent.vue'
import Insumos from '../components/InsumosComponent.vue'
import Login from '../components/loginCadastro/LoginComponent.vue'
import Cadastro from '../components/loginCadastro/CadastroComponent.vue'
import RecuperarSenha from '../components/alterarSenha/RecuperarSenhaComponent.vue'
import CadastrarNovaSenha from '../components/alterarSenha/CadastrarNovaSenhaComponent.vue'
import ConfirmarEmail from '../components/loginCadastro/ConfirmarEmailComponent.vue'
import Perfil from '../components/PerfilComponent.vue'

const routes = [
  { path: '/inicio', component: Home },
  { path: '/insumos', component: Insumos }, 
  { path: '/orcamentos', component: Orcamentos }, 
  { path: '/login', component: Login },
  { path: '/cadastro', component: Cadastro },
  { path: '/recuperarSenha', component: RecuperarSenha },
  { path: '/cadastrarNovaSenha', component: CadastrarNovaSenha }, 
  { path: '/confirmarEmail', component: ConfirmarEmail }, 
  { path: '/perfil', component: Perfil }, 
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;
