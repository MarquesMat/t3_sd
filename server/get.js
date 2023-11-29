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

// Rota para obter dados de uma categoria específica pelo category_id
router.get('/categorias/:category_id', (req, res) => {
  const categoryId = req.params.category_id;

  db.query('SELECT * FROM category WHERE category_id = ?', [categoryId], (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      if (results.length > 0) {
        res.json(results[0]);
      } else {
        res.status(404).json({ error: 'Categoria não encontrada' });
      }
    }
  });
});

// Rota para obter dados de um ator específico pelo actor_id
router.get('/atores/:actor_id', (req, res) => {
  const actorId = req.params.actor_id;

  db.query('SELECT * FROM actor WHERE actor_id = ?', [actorId], (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      if (results.length > 0) {
        res.json(results[0]);
      } else {
        res.status(404).json({ error: 'Ator não encontrado' });
      }
    }
  });
});

// Rota para obter dados de um filme específico pelo film_id
router.get('/filmes/:film_id', (req, res) => {
  const filmId = req.params.film_id;

  db.query('SELECT * FROM film WHERE film_id = ?', [filmId], (err, results) => {
    if (err) {
      res.status(500).send('Erro ao consultar o banco de dados');
    } else {
      if (results.length > 0) {
        res.json(results[0]);
      } else {
        res.status(404).json({ error: 'Filme não encontrado' });
      }
    }
  });
});


module.exports = router;
