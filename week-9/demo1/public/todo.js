'use strict';

var todolist = {};
var data_provider_url = 'http://localhost:3000/todos/';
var input = document.querySelector('.input');
var todo_body = document.getElementById('todolist_body');
var saveButton = document.querySelector('.saveButton');

input.addEventListener('click', function() {
  addToList();
})

saveButton.addEventListener('click', function() {
	itemSave();
})

var refresh = function () {
  createRequest('GET', data_provider_url, {}, refreshTodoList);
}

function handleLoad(response) {
	refresh();
}

function refreshTodoList(response) {
	var todolist = JSON.parse(response);
	var html = '';
	if (todolist) {
		for (var key in todolist) {
			var tr_element = document.createElement('tr');
			var td_element = document.createElement('td');
			td_element.innerHTML = todolist[key].id;
			tr_element.appendChild(td_element);

			var td_element = document.createElement('td');
			td_element.innerHTML = todolist[key].text;
			tr_element.appendChild(td_element);

			var checkbox_element = document.createElement('input');
			checkbox_element.type='checkbox';
			checkbox_element.value='1';
			checkbox_element.checked = todolist[key].completed;
			
			(function (id, text) {
				checkbox_element.addEventListener('click',
					function() {
						updateCompleted(id, text, this.checked);
					}
				);
			})(todolist[key].id, todolist[key].text);
			
			var td_element = document.createElement('td');
			td_element.appendChild(checkbox_element);
			tr_element.appendChild(td_element);

			var td_element = document.createElement('td');
			var element = document.createElement('input');
			element.type = 'button';
			element.value = 'Edit';
			
			(function (id, text, completed) {
				element.addEventListener('click',
					function() {
						editItem(id, text, completed);
					}
				);
			})(todolist[key].id, todolist[key].text, todolist[key].completed);

			td_element.appendChild(element);

			var element = document.createElement('input');
			element.type = 'button';
			element.value = 'Delete';
			(function (id) {
				element.addEventListener('click',
					function() {
						deleteFromList(id);
					}
				);
			})(todolist[key].id);
			td_element.appendChild(element);
			tr_element.appendChild(td_element);


			todo_body.appendChild(tr_element);
		}
	}
}

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


refresh();