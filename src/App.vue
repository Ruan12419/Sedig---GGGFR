<template>
  <div id="app">
    <Header v-if="isAuthenticated" @logout="logout" />
    <router-view @logout="logout" />
  </div>
</template>

<script>
import Header from './components/headers/HeaderComponent.vue';
import { mapState, mapActions } from 'vuex';

export default {
  name: 'App',
  components: {
    Header,
  },
  computed: {
    ...mapState(['isAuthenticated']),
  },
  methods: {
    ...mapActions(['checkAuth', 'logout']),
  },
  created() {
    this.checkAuth();
  },
};
</script>

<style>
body {
  margin: 0px;
  padding: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
