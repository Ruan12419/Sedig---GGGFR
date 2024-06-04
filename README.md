# sedig

Este é um guia passo a passo para configurar e executar o projeto sedig, que é um aplicativo web full stack usando Vue.js e Django.

## Configuração do Projeto

### Pré-requisitos
- Python 3
- pip
- Node.js
- npm

### Configuração do Ambiente Virtual para Django

1. Instale o ambiente virtual (venv) se ainda não estiver instalado:
   ```bash
   pip install virtualenv
   ```
2. Crie um ambiente virtual na raiz do projeto Django (dentro da pasta /backend):
    ```bash
    virtualenv venv
    ```
 3. Ative o ambiente virtual:
   * No Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   * No Linux:
   ```bash
   source venv/bin/activate
   ```
4. Entre na pasta sedig (/backend/sedig ) e instale as dependências do Django com o pip:
   ```bash
   pip install -r requirements.txt
   ```

### Executando o Servidor Django
1. Realize as migrações do banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Inicie o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```

### Configuração do Frontend Vue.js
1. Mantenha o servidor Djando ativo e abra um novo terminal para prosseguir
   * No VS code utilize o atalho:
      ``
      ctrl + shift + '
      ``
2. Assegure de estar na pasta raiz do projeto

3. Instale as dependências do projeto Vue.js:
* Você deve estar no mesmo diretório dos arquivos ``package.json`` e executar:
   ```bash
   npm install
   ```
#### Compilação e Hot-Reloads para Desenvolvimento
   * Para iniciar o servidor de desenvolvimento do Vue.js:
   ```bash
   npm run serve
   ```

#### Compilação e Minificação para Produção
   * Para compilar e minificar os arquivos para produção:
   ```bash
   npm run build
   ```

#### Lint e Correções de Arquivos
   * Para executar o lint e corrigir arquivos:
   ```bash
   npm run lint
   ```

## Executando o Projeto Completo
   * Com ambos os servidores (Django e Vue.js) rodando, você pode acessar o aplicativo web no navegador pelo endereço fornecido pelo Vue.js (geralmente http://localhost:8080).


<hr/>

#### Grupo
   * Fernando Antônio
   * Gabriel Santana
   * Gabriel Felipe
   * Ruan Lima