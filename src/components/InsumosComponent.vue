<template>
    <h1>Cadastro de Insumos</h1>
    <section class="orcamentos">
        <section class="add-subestacao">
            <input type="text" width="120">
            <span>Insumos</span>
        </section>
    </section>
  </template>
  
  <script>
  export default {
    name: "InsumosComponent",
    data() {
      return {
        showDropdown: false
      }
    }
  }
  </script>
  
  <style scoped>
    .orcamentos {
        background-color: #EEE;
    }

    .add-subestacao {
        background-color: #DDD;
    }
  </style>