// Antes de rodar, verifique se o seu ambiente está preparado
// Inicializar o projeto (já foi feito): npm init -y
// Instalar as dependências: npm install express mysql
// Adicione as variáveis de ambiente

// Inicie o servidor: node app.js
// Equanto o servidor estiver no ar: http://localhost:3000/filmes

// Se aparecer o erro "ER_NOT_SUPPORTED_AUTH_MODE", tente: ALTER USER 'seu_usuario'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'sua_senha'; 

// Para a autenticação, é necessário instalar o basic-auth e o express: npm install basic-auth && npm install express

const express = require('express');
const mysql = require('mysql');
const fs = require('fs'); // Ler o arquivo json com as credenciais
const basicAuth = require('basic-auth');

const apiGet = require('./get.js');
const apiDelete = require('./delete.js');
const apiPost = require('./post.js');
const apiUpdate = require('./update.js');

const app = express();
const port = 3000;

const authenticate = (req, res, next) => {
  const user = basicAuth(req);
  // Verifica as credenciais
  if (!user || user.name !== 'usr' || user.pass !== 'pwd') {
    res.set('WWW-Authenticate', 'Basic realm=Authorization Required');
    return res.status(401).send('Unauthorized');
  }

  // Se as credenciais estiverem corretas, prossiga para a próxima rota
  next();
};

// Configurar a conexão com o banco de dados
const filename = 'credentials.json';
const credenciais = JSON.parse(fs.readFileSync(filename, 'utf8'));

const db = mysql.createConnection({
  host: 'localhost',
  user:  credenciais.user, // Usuário do MySql
  password: credenciais.password, // Senha do MySql
  database: 'sakila',
});

// Conectar ao banco de dados
db.connect((err) => {
  if (err) {
    console.error('Erro ao conectar ao banco de dados: ' + err.message);
  } else {
    console.log('Conectado ao banco de dados Sakila');
  }
});

//app.use(authenticate);

// Habilita solicitações de qualquer origem --> permite API em geral
// Middleware para habilitar o CORS
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

// Permite que outras solicitações de API sejam realizadas
// Middleware para processar o corpo das solicitações (body-parser)
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use('/', apiGet); // Rotas para obter dados das tabelas (GET)
app.use('/', apiPost); // Rotas para adicionar novas instâncias nas tabelas (POST)
app.use('/', apiDelete); // Rota para excluir um filme pelo ID (DELETE)
app.use('/', apiUpdate); // Rotas de atualização

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor web iniciado em http://localhost:${port}`);
});
