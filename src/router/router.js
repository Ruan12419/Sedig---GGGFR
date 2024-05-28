import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomeComponent.vue'
import Orcamentos from '../components/OrcamentosComponent.vue'
import Insumos from '../components/InsumosComponent.vue'
import Login from '../components/LoginComponent.vue'
import Cadastro from '../components/CadastroComponent.vue'
import RecuperarSenha from '../components/RecuperarSenhaComponent.vue'
import RecuperarSenha2 from '../components/RecuperarSenhaComponent2.vue'

const routes = [
  { path: '/inicio', component: Home },
  { path: '/insumos', component: Insumos }, 
  { path: '/orcamentos', component: Orcamentos}, 
  { path: '/login', component: Login},
  { path: '/cadastro', component: Cadastro},
  { path: '/recuperarSenha', component: RecuperarSenha},
  { path: '/recuperarSenha2', component: RecuperarSenha2}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
