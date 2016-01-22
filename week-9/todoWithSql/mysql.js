'use strict';

var mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'testuser',
  password : 'test',
  database : 'todo'
});

connection.connect();

function addItem(attributes, callback) {
  	connection.query('INSERT INTO tasks SET text=?', attributes, function(err, result) {
    if (err) throw err;
    callback(result);
  })
}

function getItems(callback) {
  connection.query('SELECT id, text, completed FROM tasks', function(err, results) {
    if (err) throw err;
    callback(results);
  })
}

function removeItem(id, callback) {
  connection.query('DELETE FROM tasks WHERE id=?', id,
    function(err, results) {
    if (err) throw err;
    callback(results);
  })
}

function updateItem(id, attributes, callback) {
  var sql = 'UPDATE tasks SET ?? = ?, ?? = ? WHERE id=?';
  var inserts = ["text", attributes.text, "completed", String(attributes.completed), id]
  connection.query(mysql.format(sql, inserts), function (err, results) {
    if (err) throw err;
    callback(results);
  })
}


module.exports = {
  addItem: addItem,
  getItems: getItems,
  removeItem: removeItem,
  updateItem: updateItem
}
