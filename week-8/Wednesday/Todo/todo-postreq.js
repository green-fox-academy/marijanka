'use strict';

function createPostRequest(url, data, callback) {
  var req = new XMLHttpRequest();
  req.open('POST', url);
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(data);
  req.onreadystatechange = function () {
    console.log('allapot: ', req.readyState);
    if (req.readyState === 4) {
      callback(req.response)
    }
  }
}

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoContainer = document.querySelector('.todo-container');

var todoCallback = function (response) {
  console.log(JSON.parse(response));
  var todoItem = JSON.parse(response);
  var newTodoItem = document.createElement('p');
  newTodoItem.innerText = todoItem.text;
  todoContainer.appendChild(newTodoItem);
}

var dataToSend = JSON.stringify({text: 'Cigi!!!'})
createPostRequest(url, dataToSend, todoCallback)
