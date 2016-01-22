'use strict';

var data_provider_url = 'http://localhost:3000/todos/';

function createRequest(method, url, data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method , url);
  todoRequest.setRequestHeader('Content-Type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function () {
    if (todoRequest.readyState === 4 && callback !== null) {
      callback(todoRequest.response)
    }
  }
}
