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

// Rota para excluir um filme pelo ID (DELETE)
router.delete('/filmes/:id', (req, res) => {
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
  
// Rota para excluir um ator pelo ID (DELETE)
router.delete('/atores/:id', (req, res) => {
const atorId = req.params.id;

const query = 'DELETE FROM actor WHERE actor_id = ?';

db.query(query, [atorId], (err, results) => {
    if (err) {
    res.status(500).json({ error: 'Erro ao excluir ator do banco de dados' });
    } else {
    res.json({ success: true, message: 'Ator excluído com sucesso' });
    }
});
});

// Rota para excluir uma categoria pelo ID (DELETE)
router.delete('/categorias/:id', (req, res) => {
const categoriaId = req.params.id;

const query = 'DELETE FROM category WHERE category_id = ?';

db.query(query, [categoriaId], (err, results) => {
    if (err) {
    res.status(500).json({ error: 'Erro ao excluir categoria do banco de dados' });
    } else {
    res.json({ success: true, message: 'Categoria excluída com sucesso' });
    }
});
});

module.exports = router;
