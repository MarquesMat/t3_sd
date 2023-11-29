// update.js

const express = require('express');
const mysql = require('mysql');
const fs = require('fs');

const router = express.Router();

const filename = 'credential.json';
const credenciais = JSON.parse(fs.readFileSync(filename, 'utf8'));

const db = mysql.createConnection({
  host: 'localhost',
  user: credenciais.user,
  password: credenciais.password,
  database: 'sakila',
});

// Rota para atualizar um filme pelo ID
router.put('/filmes/:id', (req, res) => {
  const id = req.params.id;
  const { title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features } = req.body;

  const query = `
    UPDATE film
    SET title=?, description=?, release_year=?, language_id=?, rental_duration=?, rental_rate=?, length=?, replacement_cost=?, rating=?, special_features=?
    WHERE film_id=?
  `;

  const values = [title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, id];

  db.query(query, values, (err, results) => {
    if (err) {
      res.status(500).json({ error: 'Erro ao atualizar filme no banco de dados' });
    } else {
      res.json({ success: true, message: 'Filme atualizado com sucesso' });
    }
  });
});

// Rota para atualizar dados de um filme específico pelo film_id
router.put('/filmes/:film_id', (req, res) => {
    const filmId = req.params.film_id;
    const updateField = req.body.field;  // Novo campo adicionado para especificar o campo a ser atualizado
    const updateValue = req.body.value;  // Valor a ser atribuído ao campo especificado
  
    if (!updateField || !updateValue) {
      return res.status(400).json({ error: 'Parâmetros inválidos. Forneça um campo e um valor para atualização.' });
    }
  
    const query = `UPDATE film SET ${updateField} = ? WHERE film_id = ?`;
  
    db.query(query, [updateValue, filmId], (err, results) => {
      if (err) {
        res.status(500).send('Erro ao atualizar o banco de dados');
      } else {
        if (results.affectedRows > 0) {
          res.json({ message: 'Filme atualizado com sucesso' });
        } else {
          res.status(404).json({ error: 'Filme não encontrado' });
        }
      }
    });
  });

// Adicione rotas adicionais para atualização de atores e categorias se necessário

module.exports = router;
