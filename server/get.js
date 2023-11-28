const express = require('express');
const mysql = require('mysql');
const fs = require('fs'); // Ler o arquivo json com as credenciais

// Configurar a conexão com o banco de dados
const filename = 'credential.json';
const credenciais = JSON.parse(fs.readFileSync(filename, 'utf8'));

const db = mysql.createConnection({
  host: 'localhost',
  user:  credenciais.user, // Usuário do MySql
  password: credenciais.password, // Senha do MySql
  database: 'sakila',
});

const router = express.Router();

// Rota para obter dados da tabela film
router.get('/filmes', (req, res) => {
  db.query('SELECT * FROM film', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Rota para obter dados da tabela actor
router.get('/atores', (req, res) => {
  db.query('SELECT * FROM actor', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

// Rota para obter dados da tabela category
router.get('/categorias', (req, res) => {
  db.query('SELECT * FROM category', (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      res.json(results);
    }
  });
});

module.exports = router;
