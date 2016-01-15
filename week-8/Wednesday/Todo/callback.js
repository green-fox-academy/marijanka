'use strict';

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var urlDel = "https://mysterious-dusk-8248.herokuapp.com/todos/14"
var todoContainer = document.querySelector('.todo-container');

var todoCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function (todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  });
}

var refresh = function () {
  createRequest('GET', url, {}, todoCallback);
}

refresh();

var newTodo = JSON.stringify({text: 'Bologság!!!'});

var createTodoCallback = function (response) {
  refresh();
}

createRequest('POST', url, newTodo, createTodoCallback);
