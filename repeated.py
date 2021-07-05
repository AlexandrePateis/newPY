#Taking repeated values ​​from the list
vet = list()
cont = 0
for c in range(0, 5):
    num = int(input('Type a value: '))
    vet.append(num)
print(vet)

noot_repeated = list()
for i in vet:
    if i not in noot_repeated:
        noot_repeated.append(i)
    noot_repeated.sort()
print(noot_repeated)        