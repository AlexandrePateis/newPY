import os
from random import randint
list1 = list()
list2 = list()



while True:
    while True:
        my = int(input('Enter a number from 1 to 60: '))
        if my <=60:
            break
    if my not in list2:
        list2.append(my)
    my = 0
    if len(list2) == 6:
        break    

while True:
    comp = randint(1, 60)
    if comp not in list1:
        list1.append(comp)
    comp = 0
    if len(list1) == 6:
        break
os.system('clear')
list2.sort()
list1.sort()
print(f'This is your list {list2}')
print(f'This is the sorted list {list1}')       

new = [valor for valor in list1 if valor in list2]

print(new)
