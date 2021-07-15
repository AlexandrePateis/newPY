strig = 'abcde'
lista = [1,2,3,4,5]
i=0
dici ={strig[i]:lista[i]*2 for i in range(0, len(strig))}
print(dici)