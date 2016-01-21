'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host : 'localhost',
  user : 'testuser',
  password : 'test',
  database : 'todo'
});

connection.connect();


function addUser(attributes) {
  connection.query('INSERT INTO tasks SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  })
}

function getUser() {
  connection.query('SELECT * FROM tasks', function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

function getUserById(attributes) {
  connection.query('SELECT * FROM tasks WHERE task_id=?', attributes,
    function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

function removeUser(attributes) {
  connection.query('DELETE FROM tasks WHERE task_id=?', attributes,
    function(err, results) {
    if (err) throw err;
    console.log(results);
  });
}

module.exports = {
  add: addUser,
  get: getUser,
  getById: getUserById,
  delete: removeUser
};
