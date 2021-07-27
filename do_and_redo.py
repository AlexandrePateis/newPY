import os
worklist = []
del_worklist = []
print('Options: ')
print('1 - Add task. ')
print('2 - Remove task. ')
print('3 - Back task.')
print('4 - Show task')
print('5 - Get out')

def show_task(lis):
    if not lis:
        print('Nothing to show')
    for i in lis:
        print(i)
    return        


while True:
    while True:
        op = int(input('Enter you option: '))
        if op > 5 or op < 1:
            print('Option invalid. ')
        else:
            break    
    if op == 1:
        task = str(input('Enter your task.'))
        worklist.append(task)
        os.system('clear')
        print(worklist)
    elif op == 2:
        if worklist == []:
            print('Not remove.')
        else:    
            del_worklist.append(worklist[-1])
            worklist.pop()
            os.system('clear')
            print(worklist)
    elif op == 3:
        if worklist == []:
            print('Not back.')
        else:    
            if del_worklist[-1] not in worklist:
                worklist.append(del_worklist[-1])
                del_worklist.clear
            os.system('clear')
            print(worklist)
    elif op == 4:
        print(show_task(worklist))
    else:
        break    
           

