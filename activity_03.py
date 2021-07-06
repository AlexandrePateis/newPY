def check_negative_or_passive(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0        
num = int(input('Type a number: '))
print(check_negative_or_passive(num))        