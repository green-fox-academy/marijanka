'use strict';

var todolist = {};
var data_provider_url = 'http://localhost:3000';

window.onload = function() {
	requestList()
}

function requestList() {
	document.getElementById('todolist_body').innerHTML = '<tr><td>Loading...</td></tr>';
	createRequest('POST', data_provider_url, JSON.stringify({operation: 'list'}), handleLoad);
}

function handleLoad(response) {
	todolist = JSON.parse(response);
	refreshTodoList();
}

function refreshTodoList() {
	var html = '';
	todo_body = document.getElementById('todolist_body');
	todo_body.innerHTML = '';
	if (todolist) {
		for (key in todolist) {
			var tr_element = document.createElement('tr');

			var td_element = document.createElement('td');
			td_element.innerHTML = todolist[key].id;
			tr_element.appendChild(td_element);

			var td_element = document.createElement('td');
			td_element.innerHTML = todolist[key].subject;
			tr_element.appendChild(td_element);

			var checkbox_element = document.createElement('input');
			checkbox_element.type='checkbox';
			checkbox_element.value='1';
			checkbox_element.checked = todolist[key].completed;

			(function (id) {
				checkbox_element.addEventListener('click',
					function() {
						updateCompleted(id, this.checked);
					}
				);
			})(todolist[key].id);

			var td_element = document.createElement('td');
			td_element.appendChild(checkbox_element);
			tr_element.appendChild(td_element);

			var td_element = document.createElement('td');
			var element = document.createElement('input');
			element.type = 'button';
			element.value = 'Edit';
			(function (id) {
				element.addEventListener('click',
					function() {
						editItem(id);
					}
				);
			})(todolist[key].id);
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
	var data = {operation: 'add'};
	data.subject = document.getElementById('new_item').value;
	createRequest('POST', data_provider_url, JSON.stringify(data), handleLoad);
	document.getElementById('new_item').value = '';
}

function deleteFromList(id) {
	var data = {operation: 'delete'};
	data.id = id;
	createRequest('POST', data_provider_url, JSON.stringify(data), handleLoad);
}

function updateCompleted(id, completed) {
	var data = {operation: 'update_completed'};
	data.id = id;
	data.completed = completed;
	console.log(data);
	createRequest('POST', data_provider_url, JSON.stringify(data), handleLoad);
}

function editItem(id) {
	var item;
	for (key in todolist) {
		if (todolist[key].id == id) {
			item = todolist[key];
			break;
		}
	}
	document.getElementById('edit_id').innerHTML = item.id;
	document.getElementById('edit_subject').value = item.subject;
	document.getElementById('edit_completed').checked = item.completed;
	document.getElementById('editform').style.display = 'block';
}

function itemSave() {
	var data = {operation: 'item_save'};
	data.id = document.getElementById('edit_id').innerHTML;
	data.subject = document.getElementById('edit_subject').value;
	data.completed = document.getElementById('edit_completed').checked;
	createRequest('POST', data_provider_url, JSON.stringify(data), handleLoad);
	document.getElementById('editform').style.display = 'none';
}
