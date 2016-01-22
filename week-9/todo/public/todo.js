'use strict';

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

refresh();