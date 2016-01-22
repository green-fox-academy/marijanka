'use strict';

var express = require("express");
var bodyParser = require("body-parser");
var mysql = require("./mysql.js");

var app = express();

app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

app.get("/todos", function (req, res) {
  mysql.getItems(function(items) {
    res.status(200).json(items);
  });
});

app.post("/todos", function (req, res) {
  var items = req.body.text;
  mysql.addItem(items, function(newItem) {
    res.status(200).json(newItem);
  });
});

app.get("/todos/:id", function (req, res) {
  findItem(req, res, function (item) { res.json(item); });
});

app.put("/todos/:id", function (req, res) {
  mysql.updateItem(req.params.id, req.body, function (upItem) {
    res.status(200).json(upItem);
  });
});

app.delete("/todos/:id", function (req, res) {
  mysql.removeItem(req.params.id, function(item) {
    res.status(200).json(item);
  });
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
})

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));
  next();
}
