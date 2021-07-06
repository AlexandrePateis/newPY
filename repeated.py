#Taking repeated values ​​from the list
vet = list()
cont = 0
for c in range(0, 5):
    num = int(input('Type a value: '))
    vet.append(num)
print(vet)

def noot_repeated(lista):
    nova = list()
    for i in lista:
        if i not in nova:
            nova.append(i)
    nova.sort()
    return nova    

vet = noot_repeated(vet)
print(vet)    