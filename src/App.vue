<template>
  <Header v-if="isLogin" @logout="isLogin = !isLogin" />
  <router-view @logout="isLogin = !isLogin" />
</template>

<script>
import Header from './components/headers/HeaderComponent.vue'

export default {
  data() {
    return {
      isLogin: true,
    };
  },
  name: 'App',
  components: {
    Header,
  }
}
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
