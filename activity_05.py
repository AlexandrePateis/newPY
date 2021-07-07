while True:
    h = int(input('Typo a hour: '))
    if h >23:
        print('Invalid time, try again.')
    else:
        break    
while True:
    m = int(input('Typo a minutes: '))
    if m>59:
        print('Invalid minute, try again.')
    else:
        break    
while True:
    s = int(input('Typo a seconds: '))
    if s >59:
        print('Invalid second, try again.')
    else:
        break    

def convert_to_seconds(hour, minute, second):
    tot = 0
    h = hour * 3600
    tot = tot + h
    m = minute *60
    tot = tot + m
    s = second
    tot = tot + s
    return tot

total_in_second = convert_to_seconds(h, m, s)
print(f'Total in second is: {total_in_second}')