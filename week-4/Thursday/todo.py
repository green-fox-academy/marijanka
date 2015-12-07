from sys import *
import os

filename = 'test.txt'

def open_file():
    input_file = open(filename)
    input_text = input_file.read()
    input_file.close()
    return input_text

def write_file(todo_items):
    output_file = open(filename, 'w')
    output_file.write('\n'.join(todo_items))
    output_file.close()

def add_todo(new_task = ''):
    if new_task == '':
        new_task = input('Write a new task: ')
        return add_todo(new_task)
    todo_items = open_file().split('\n')
    todo_items.append(new_task)
    write_file(todo_items)

def list_todo():
    output = list_helper()
    for i in range(len(output)):
        if output[i][-1] == 'X':
            print(i+1, '. [x] ',output[i][0:len(output[i])-1], sep='')
        else:
            print(i+1, '. [ ] ',output[i], sep='')

def list_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '' and item[len(item)-1] != '*':
            output.append(item)
    return output

def remove_helper():
    todo_items = open_file().split('\n')
    output = []
    for item in todo_items:
        if item != '':
            output.append(item)
    return output

def remove_todo(task_id = ''):
    if task_id == '':
        list_todo()
        print('')
        task_id = input('Choose lists number: ')
        return remove_todo(task_id)
    items = list_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i] + '*')
    write_file(output)

def list_removed_todo():
     todo_items = open_file().split('\n')
     output = []
     print('Removed elements:')
     for item in todo_items:
         if item != '' and item[len(item)-1] == '*':
             if item != '' and item[len(item)-2] == 'X':
                 output.append(item[:len(item)-2])
             else:
                 output.append(item[:len(item)-1])
     for i in range(len(output)):
         print(output[i][0:len(item)-1])



def completed_todo(task_id = ''):
    if task_id == '':
        list_todo()
        print('')
        task_id = input('Choose lists number: ')
        return completed_todo(task_id)
    items = list_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i] + " X")
    write_file(output)

def uncompleted_todo(task_id = ''):
    if task_id == '':
        list_todo()
        print('')
        task_id = input('Choose lists number: ')
        return uncompleted_todo(task_id)
    items = list_helper()
    output = []
    task_id = int(task_id)
    for i in range(len(items)):
        if i != (task_id - 1):
            output.append(items[i])
        else:
            output.append(items[i][:len(items[i])-2])
    write_file(output)
