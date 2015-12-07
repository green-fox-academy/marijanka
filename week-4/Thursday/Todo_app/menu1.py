from termcolor import colored
import sys
import todo


def menu_table():
	print('')
	print('')
	print('---------------------------------------------------------------------------------')
	print('|                                         					|')
	print('|       1  Add task to todo list           					|')
	print('|       2  Check complated task	        					|')
	print('|       3  Delete database      						|')
	print('|       4  List all incompleted tasks from todo list      			|')
	print('|       5  List all completed tasks from todo list        			|')
	print('|       6  List all completed and incompleted tasks from todo list              |')
	print('|	7  List all completed, incompleted and removed tasks from todo list	|')
	print('|       8  Remove list element from todo list (revocable)           		|')
	print('|       9  Remove list element from todo list and database (not revocable)      |')
	print('|       10 Search              							|')
	print('|	11 Uncheck already checked task						|')
	print('|       12 Exit              	 	   					|')
	print('|                                          					|')
	print('---------------------------------------------------------------------------------')
	print('')
	print('')


def menu_input():
	menu_table()
	sbody_input = input('Choose a number from menu: ')

	if int(sbody_input) == 1:
		todo.add_todo()
	elif int(sbody_input) == 2:
		todo.completed_todo()
	elif int(sbody_input) == 3:
		todo.delete_database()
	elif int(sbody_input) == 4:
		todo.list_todo()
	elif int(sbody_input) == 5:
		todo.list_todo_only_ch()
	elif int(sbody_input) == 6:
		todo.list_todo_ch()
	elif int(sbody_input) == 7:
		todo.list_todo_all()
	elif int(sbody_input) == 8:
		todo.remove_todo()
	elif int(sbody_input) == 9:
		todo.remove_todo_ultimate()
	elif int(sbody_input) == 10:
		todo.search_todo()
	elif int(sbody_input) == 11:
		todo.uncompleted_todo()
	elif int(sbody_input) == 12:
		exit()
	else:
		print('This is not correct number!')
		other_input = input('Choose a number from menu: ')

while True:
	menu_input()
