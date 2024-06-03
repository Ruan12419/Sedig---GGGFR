import { createRouter, createWebHistory } from 'vue-router'
import store from '../store';
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
  { path: '/', redirect: '/inicio' },
  { path: '/inicio', component: Home },
  { path: '/insumos', component: Insumos, beforeEnter: (to, from, next) => {
    if (store.getters.isAdmin) {
      next(); 
    } else {
      next('/inicio'); 
    }
  } }, 
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

router.beforeEach(async (to, from, next) => {
  await store.dispatch('checkAuth');

  const isAuthenticated = store.getters.isAuthenticated;

  const authRequiredRoutes = ['/inicio', '/perfil', '/orcamentos', '/insumos'];
  const publicOnlyRoutes = ['/login', '/cadastro'];

  const authRequired = authRequiredRoutes.includes(to.path);
  const isPublicOnlyRoute = publicOnlyRoutes.includes(to.path);

  if (isAuthenticated && isPublicOnlyRoute) {
    return next('/inicio');
  }

  if (authRequired && !isAuthenticated) {
    return next('/login');
  }

  next();
});


export default router;
