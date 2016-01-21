'use strict';

function createRequest(method, "/load", data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method , url);
  todoRequest.setRequestHeader('Content-Type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function () {
    console.log('allapot: ', todoRequest.readyState);
    if (todoRequest.readyState === 4 && callback !== null) {
      callback(todoRequest.response)
    }
  }
}
