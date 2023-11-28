// Antes de rodar, verifique se o seu ambiente está preparado
// Inicializar o projeto (já foi feito): npm init -y
// Instalar as dependências: npm install express mysql
// Adicione as variáveis de ambiente

// Inicie o servidor: node app.js
// Equanto o servidor estiver no ar: http://localhost:3000/filmes

// Se aparecer o erro "ER_NOT_SUPPORTED_AUTH_MODE", tente: ALTER USER 'seu_usuario'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'sua_senha'; 

const express = require('express');
const mysql = require('mysql');
const fs = require('fs'); // Ler o arquivo json com as credenciais

const app = express();
const port = 3000;

// Configurar a conexão com o banco de dados
const filename = 'credential.json';
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

// Rotas para obter dados das tabelas (GET)
// Rota para obter dados da tabela film
app.get('/filmes', (req, res) => {
  db.query('SELECT * FROM film', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Rota para obter dados da tabela actor
app.get('/atores', (req, res) => {
  db.query('SELECT * FROM actor', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Rota para obter dados da tabela category
app.get('/categorias', (req, res) => {
  db.query('SELECT * FROM category', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Rotas para adicionar novas instâncias nas tabelas
// Rota para adicionar um novo filme (POST)
app.post('/filmes', (req, res) => {
  const { title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features } = req.body;

  const query = `
    INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `;

  const values = [title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features];

  db.query(query, values, (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Erro ao adicionar filme ao banco de dados' });
    } else {
      res.json({ success: true, message: 'Filme adicionado com sucesso' });
    }
  });
});

// Rota para excluir um filme pelo ID (DELETE)
app.delete('/filmes/:id', (req, res) => {
  const filmeId = req.params.id;

  const query = 'DELETE FROM film WHERE film_id = ?';

  db.query(query, [filmeId], (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Erro ao excluir filme do banco de dados' });
    } else {
      res.json({ success: true, message: 'Filme excluído com sucesso' });
    }
  });
});

// Iniciar o servidor
app.listen(port, () => {
  console.log(`Servidor web iniciado em http://localhost:${port}`);
});
