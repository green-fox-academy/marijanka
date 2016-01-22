'use strict';

var todolist = {};
var input = document.querySelector('.input');
var todo_body = document.getElementById('todolist_body');
var saveButton = document.querySelector('.saveButton');

input.addEventListener('click', function() {
  addToList();
})

saveButton.addEventListener('click', function() {
	itemSave();
})

function addToList() {
	var data = document.getElementById('new_item').value;
	data = JSON.stringify({text: data});
	todo_body.innerHTML = '';
	createRequest('POST', data_provider_url, data, handleLoad);
	document.getElementById('new_item').value = '';
}

function deleteFromList(id) {
	var url = data_provider_url + id;
	todo_body.innerHTML = '';
	createRequest('DELETE', url, null, handleLoad);
}

function updateCompleted(id, text, completed) {
	var url = data_provider_url + id;
	var data = JSON.stringify({completed: true, text: text});
	todo_body.innerHTML = '';
	createRequest('PUT', url, data, handleLoad);
}

function editItem(id, text, completed) {
	document.getElementById('edit_completed').checked = Number(completed);
	document.getElementById('edit_subject').value = text;
	document.getElementById('edit_id').innerHTML = id;
	document.getElementById('editform').style.display = 'block';
}

function itemSave() {
	var id = document.getElementById('edit_id').innerHTML
	var url = data_provider_url + id;
	var text = document.getElementById('edit_subject').value;
	var completed = Boolean(document.getElementById('edit_completed').checked);
	var data = JSON.stringify({id: id, text: text, completed:completed});
	todo_body.innerHTML = '';
	createRequest('PUT', url, data, handleLoad);
	document.getElementById('editform').style.display = 'none';
}
