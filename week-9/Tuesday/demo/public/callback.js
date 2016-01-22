'use strict';

var url = "http://localhost:3000/todos";
var addItemAndListButton = document.querySelector('.addItemAndlistButton');
var deleteButton = document.querySelector('.delete')
var input = document.querySelector('.textarea');
var deleteInput = document.querySelector('.deleteInput');
var todoContainer = document.querySelector('.todo-container');

var dateObj = new Date();
var month = dateObj.getUTCMonth() + 1; //months from 1-12
var day = dateObj.getUTCDate();
var year = dateObj.getUTCFullYear();
var hour = dateObj.getUTCHours();
var minute = dateObj.getUTCMinutes();


var currentDate = year + '. '+ month + '. ' + day + '. ' + hour + ': ' + minute;

addItemAndListButton.addEventListener('click', function() {
  addItem();
})

deleteButton.addEventListener('click', function() {
  deleteItem();
})

var newTodo;

var addItem = function () {
  var textInput = input.value;
  newTodo = JSON.stringify({text: textInput});
  todoContainer.innerHTML = '';
  createRequest('POST', url, newTodo, createTodoCallback);
}

var deleteItem = function () {
  var numberInput = deleteInput.value;
  var delUrl = url + '/' + numberInput;
  todoContainer.innerHTML = '';
  createRequest('DELETE', delUrl, null, null);
  refresh();
}


var todoCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function (todoItem) {
    var newTodoItem = document.createElement('p');
    var todoItemId = document.createElement('p');
    var createCheckbox = document.createElement('input');
    createCheckbox.type = 'checkbox';
    newTodoItem.innerText = currentDate + '    ' + todoItem.id + '.      ' + todoItem.text;
    todoContainer.appendChild(newTodoItem);
    todoContainer.appendChild(createCheckbox);
  });
}

var refresh = function () {
  createRequest('GET', url, {}, todoCallback);
}

var createTodoCallback = function (response) {
  refresh();
}


refresh();
