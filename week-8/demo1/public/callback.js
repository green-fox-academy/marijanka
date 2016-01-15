'use strict';

function createRequest(method, url, data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method , url);
  todoRequest.setRequestHeader('Content-Type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function () {
    if (todoRequest.readyState === 4) {
      callback(todoRequest.response)
    }
  }
}
