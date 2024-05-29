import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomeComponent.vue'
import Orcamentos from '../components/OrcamentosComponent.vue'
import Insumos from '../components/InsumosComponent.vue'
import Login from '../components/LoginComponent.vue'
import Cadastro from '../components/CadastroComponent.vue'
import RecuperarSenha from '../components/RecuperarSenhaComponent.vue'

const routes = [
  { path: '/inicio', component: Home },
  { path: '/insumos', component: Insumos }, 
  { path: '/orcamentos', component: Orcamentos}, 
  { path: '/login', component: Login},
  { path: '/cadastro', component: Cadastro},
  { path: '/recuperarSenha', component: RecuperarSenha},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;
