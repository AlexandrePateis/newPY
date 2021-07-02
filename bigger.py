big = 0
lis = list()
for c in range(0, 5):
    num = int(input('Type a number: '))
    lis.append(num)
print(lis)
big=max(lis)
print (f'The largest number is the {big}')        