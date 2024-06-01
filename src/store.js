import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
  },
  mutations: {
    SET_AUTHENTICATED(state, value) {
      state.isAuthenticated = value;
    },
  },
  actions: {
    async checkAuth({ commit }) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/auth/status');
        commit('SET_AUTHENTICATED', response.data.isAuthenticated);
      } catch (error) {
        commit('SET_AUTHENTICATED', false);
      }
    },
    logout({ commit }) {
      axios.post('http://127.0.0.1:8000/logout').then(() => {
        commit('SET_AUTHENTICATED', false);
      });
    },
  },
});
