<template>
  <Header />
  <router-view />
</template>

<script>
import Header from './components/HeaderComponent.vue'

export default {
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
