import os
while True:
    name = str(input('Type your name: ')).strip()
    len(name)
    if len(name) < 3:
        print('Name must have more than 3 characters.')
    else:
        break
while True:
    age = int(input('Type you age: '))
    if age > 150 or age < 0:
        print('Invalid age.')
    else:
        break
while True:
    wage = float(input('Type your wage: '))
    if wage < 0:
        print('Invalid wage')
    else:
        break
    
while True:
    sex = str(input('Type you sex [f/m]: ')).strip().lower()[0]
    if sex != 'm' and sex != 'f':
        print ('Invalid sex.')
    else:
        break        
if sex == 'm':
    sex = 'man'
else:
    sex = 'woman'
while True:
    marital_status = str(input('Type your marital status: ')).lower().strip()[0]
    if marital_status != 's' and marital_status != 'c' and marital_status != 'v' and marital_status != 'd':
        print('Invalid marital status.')
    else:
        break
if marital_status == 's':
    marital_status='not married'
elif marital_status == 'c':
    marital_status = 'merried'
elif marital_status == 'v':
    marital_status = 'windower'
else:
        marital_status = 'divorced'

os.system('clear')
print (f'Your name is {name}, you are {age} year old, your salary is {wage}, your sex is {sex}, and is {marital_status}')