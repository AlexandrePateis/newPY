import os
worklist = []
del_worklist = []

print('''
Options:
1 - Add task.
2 - Remove task.
3 - Back task.
4 - Show task
5 - Get out
''')

def show_task(lis):
    if not lis:
        print('Nothing to show')
    for i in lis:
        print(i)    

def clear_screen():
    clear = os.system('clear')
    return clear

   
while True:
    op = int(input('Enter you option: '))
    if op > 5 or op < 1:
        print('Option invalid. ')
        continue   
    if op == 1:
        task = str(input('Enter your task.'))
        worklist.append(task)
        clear_screen()
        print(worklist)
    elif op == 2:
        if not worklist:
            print('Not remove.')
        else:    
            del_worklist.append(worklist[-1])
            worklist.pop()
            clear_screen()
            print(worklist)
    elif op == 3:
        if not worklist or del_worklist == []:
            print('Not back.')
        else:    
            worklist.append(del_worklist[-1])
            del_worklist.pop()
            clear_screen()
            print(worklist)
    elif op == 4:
        show_task(worklist)
    else:
        break    
           

