import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomeComponent.vue'
import Insumos from '../components/InsumosComponent.vue'

const routes = [
  { path: '/inicio', component: Home },
  { path: '/insumos', component: Insumos }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
