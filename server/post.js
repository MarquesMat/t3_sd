const express = require('express');
const mysql = require('mysql');
const fs = require('fs'); // Ler o arquivo json com as credenciais

// Configurar a conexão com o banco de dados
const filename = 'credentials.json';
const credenciais = JSON.parse(fs.readFileSync(filename, 'utf8'));

const db = mysql.createConnection({
  host: 'localhost',
  user:  credenciais.user, // Usuário do MySql
  password: credenciais.password, // Senha do MySql
  database: 'sakila',
});

const router = express.Router();

// Rota para adicionar um novo filme
router.post('/filmes', (req, res) => {
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

// Rota para adicionar um novo ator
router.post('/atores', (req, res) => {
  const { first_name, last_name } = req.body;

  const query = `
    INSERT INTO actor (first_name, last_name)
    VALUES (?, ?)
  `;

  const values = [first_name, last_name];

  db.query(query, values, (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Erro ao adicionar ator ao banco de dados' });
    } else {
      res.json({ success: true, message: 'Ator adicionado com sucesso' });
    }
  });
});

// Rota para adicionar um novo ator
router.post('/categorias', (req, res) => {
  const { name } = req.body;

  const query = `
    INSERT INTO category (name)
    VALUES (?)
  `;

  const values = [name];

  db.query(query, values, (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Erro ao adicionar categoria ao banco de dados' });
    } else {
      res.json({ success: true, message: 'Categoria adicionada com sucesso' });
    }
  });
});

module.exports = router;
