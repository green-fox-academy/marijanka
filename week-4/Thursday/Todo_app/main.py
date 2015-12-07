from sys import *
import os
import todo

def readme():
    os.system('cls')
    open_file = open('README.md')
    open_text = open_file.read()
    open_file.close()
    print(open_text)

if len(argv) != 1 and len(argv) < 4:
    if (argv[1] == 'add'):
        if len(argv) == 3:
            todo.add_todo(argv[2])
        else:
            todo.add_todo()
    elif (argv[1] == 'ls' or argv[1] == 'st'):
        if len(argv) == 3 and argv[2] == '-la':
            todo.list_removed_todo()
        else:
            todo.list_todo()
    elif (argv[1] == 'rm'):
        todo.remove_todo()
    elif (argv[1] == 'ch'):
        todo.completed_todo()
    elif (argv[1] == 'uch'):
        todo.uncompleted_todo()
    elif (argv[1] == '--help'):
        readme()
    elif (argv[1]) == '--version':
        print('TODO for Developers version 0.1')
    else:
        print('Invalid syntax')
else:
    readme()
