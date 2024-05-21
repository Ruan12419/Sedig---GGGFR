<template>
    <header>
      <img src="https://upload.wikimedia.org/wikipedia/commons/b/b3/Eletrobras.png" srcset="">
      <nav>
        <ul>
          <li><router-link to="/inicio" class="nav-link">Início</router-link></li>
          <li>|</li>
          <li><router-link to="/orcamentos" class="nav-link">Orçamentos</router-link></li>
          <li>|</li>
          <li><router-link to="/insumos" class="nav-link">Insumos</router-link></li>
        </ul>
      </nav>
      <div class="img-perfil" @mouseover="showDropdown = true" @mouseleave="showDropdown = false">
      <div alt="foto-perfil" srcset="" style="background-color: #FFF; border-radius: 100%; width: 60px; height: 60px;"></div>
      <div v-if="showDropdown" class="dropdown">
        <button>Edit Profile</button>
        <button>Logout</button>
      </div>
    </div>
    </header>
  </template>
  
  <script>
  export default {
    name: "HeaderComponent",
    data() {
      return {
        showDropdown: false
      }
    }
  }
  </script>
  
  <style scoped>
  body {
    margin: 0;
    padding: 0;
    background-color: rgba(200,400,200, 1);
  }
  header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: baseline;
    padding: 1.5em;
    padding-bottom: 0;
    background-color: #6BC9DB;
  }
  img {
    width: 8em;
  }
  ul, li {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: space-around;
  }
  li {
    font-size: 18px;
    margin-right: 1.7em;
    margin-left: 1.7em;
    color: #FFF;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  li:hover {
    color: blue;
  }
  .nav-link {
    text-decoration: none;
    color: inherit;
  }
  .dropdown {
    position: absolute;
    background-color: #f9f9f9;
    max-width: 150px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    right: 1px;
  }
  .dropdown button {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    width: 100%;
  }
  .dropdown button:hover {
    background-color: #f1f1f1
  }

  @media screen and (max-width: 600px) {
    header {
      flex-direction: row;
      align-items: baseline;
    }
    img {
      width: 7em;
    }
    ul, li {
      margin-right: 0.15em;
      margin-left: 0.15em;
      font-size: small;
    }
    .dropdown {
      left: 1px;
    }
  }
  </style>
  