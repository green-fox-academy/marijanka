from termcolor import colored
import sys
import todo

print(colored('\033[44m\033[1;35m' + '*******  ****'))



def menu_input():
	sbody_input = input('Choose from menu: ')

	try:
		menu_choose = False
		while menu_choose == False:
			if int(sbody_input) == 1:
				todo.list_todo()
				menu_choose = True
			elif int(sbody_input) == 2:
				todo.add_todo()
				menu_choose = True
			elif int(sbody_input) == 3:
				todo.completed_todo()
				menu_choose = True
			elif int(sbody_input) == 4:
				todo.uncompleted_todo()
				menu_choose = True
			elif int(sbody_input) == 5:
				todo.remove_todo()
				menu_choose = True
			elif int(sbody_input) == 6:
				todo.list_removed_todo()
				menu_choose = True
			elif int(sbody_input) == 7:
				exit()
			else:
				print('This is not correct number!')
				other_input = input('Choose other number: ')
			if menu_right == True:
				main()

	except ValueError:
		print('Please only enter numbers! ')
		menu_input()

def menu_table():
	print('')
	print('')
	print(colored('-------------------------------------------')
	print(colored('|                                         |')
	print(colored('|       1 List tasks from todo list       |')
	print(colored('|       2 Add task to todo list           |')
	print(colored('|       3 Check task                      |')
	print(colored('|       4 Unchecked task                  |')
	print(colored('|       5 Remove task                     |')
	print(colored('|       6 List removed tasks              |')
	print(colored('|       7 Exit              	 	  |')
	print(colored('|                                         |')
	print(colored('-------------------------------------------')
	print('')
	print('')

def main():
	menu_table()
	menu_input()
