<template>
  <h1>Orçamentos</h1>
  <section class="orcamentos-cadastrados">
    
    <table>
      <thead>
        <th>Nome da Subestação</th>
        <th>Data Cotação</th>
        <th>Qtd. Pátios</th>
        <th>Qtd. Módulos</th>
      </thead>
      
      <tbody>
        <tr>
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
        </tr>
        <tr>
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
        </tr>
        <tr>
          <td>Olinda</td>
          <td>2023</td>
          <td>3</td>
          <td>7</td>
        </tr>
      </tbody>
    </table>
  </section>
    <section class="orcamentos">
        <section class="add-subestacao">
          <span>Cadastro de Subestação</span>
          <hr>
            <label for="SE-nome">Nome da Subestação: *</label>
            <input type="text" id="SE-nome" width="120" required>
        </section>
    </section>
  </template>
  
  <script>
  export default {
    name: "HomeComponent",
    data() {
      return {
        showDropdown: false
      }
    }
  }
  </script>
  
  <style scoped>

    table thead {
      background-color: rgb(166, 204, 243);
    }
    .orcamentos {
        background-color: #EEE;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 10%;
        height: 100%;
    }

    .add-subestacao {
        /* background-color: #DDD;*/
    }
  </style>