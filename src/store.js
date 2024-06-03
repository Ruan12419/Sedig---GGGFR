import { createStore } from 'vuex';
import http from '@/http';

export default createStore({
  state: {
    isAuthenticated: false,
    isAdmin: false, 
  },
  mutations: {
    SET_AUTHENTICATED(state, value) {
      state.isAuthenticated = value;
    },
    SET_ADMIN(state, value) { 
      state.isAdmin = value;
    },
  },
  actions: {
    async checkAuth({ commit }) {
      try {
        const response = await http.get('/api/auth/status');
        commit('SET_AUTHENTICATED', response.data.isAuthenticated);
        commit('SET_ADMIN', ((response.data.is_superuser) && response.data.is_staff)); 
      } catch (error) {
        commit('SET_AUTHENTICATED', false);
        commit('SET_ADMIN', false); 
      }
    },
    logout({ commit }) {
      http.post('/logout').then(() => {
        commit('SET_AUTHENTICATED', false);
        commit('SET_ADMIN', false); 
        localStorage.removeItem('sessionid');
      }).catch(error => {
        console.error('Erro ao tentar fazer logout:', error);
      });
    },
  },
  getters: {
    isAdmin: state => state.isAdmin, 
    isAuthenticated: state => state.isAuthenticated, 
  },
});
