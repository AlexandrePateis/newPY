import os
os.system('clear')
user=str(input('Enter the username: ')).lower().strip()
while True:
    passw=str(input('Enter the password: ')).lower().strip()
    os.system('clear')
    if passw != user:
        break
    else:
        print('The password cannot be the same as the username.')
print('Registered successfully')