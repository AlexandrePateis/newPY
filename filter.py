import os
import statistics
list_01 = []
list_02 = []
cont =0
while True:
    prod = str(input('Enter the product: ').strip().lower().title())
    price = float(input('Enter the price: R$'))
    list_02.append(prod)
    list_02.append(price)
    list_01.append(list_02)
    list_02 = []
    os.system('clear')
    cont +=1 
    #asnwer = str(input('Do you want to add any more products?')).strip().lower()[0]
    if cont == 3:
        break
       
print(list_01)

cont = 0
med = [cont + med[1] for med in list_01]        #Utilizando Comprehension
print(sum(med)/len(list_01))



'''cont = 0
for value in list_01:               #Forma correta com loop
    cont = cont + value[1]
media = cont / len(list_01)
print (f'{media:.2f}')  '''      