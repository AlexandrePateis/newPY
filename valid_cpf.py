aux = 10
soma = 0
result = 0
def think_size(x):                  #Função que calcula o tamanho do número, e retorna essa valor
    a = str(x)
    if len(a) > 1:
        if a[0] == '0':
            return len(a) - 1
        else:
            return len(a)
    return len(a)

while True:
    cpf = int(input('Enter you cpf: '))
    if think_size(cpf)<11 or think_size(cpf)>11:
        print('Invalid')
    else:
        break
cpf = str(cpf)
cpf_provisory = cpf[:-2]
new = list(cpf_provisory)
new_int = []
for value in new:
    new_int.append(int(value))
for value in new_int:
    result = value * aux
    #print(f'{value} * {aux} = {result}')
    soma = soma + result
    aux = aux -1
print(soma)

digit_01 = 11 -(soma % 11) 
if digit_01>9:
    digit_01 = 0
    new_int.append(0)
else:
    digit_01 = 11 -(soma % 11)       
    new_int.append(digit_01)
soma = 0
result = 0
aux = 11
for value in new_int:
    result = value * aux
    #print(f'{value} * {aux} = {result}')
    soma = soma + result
    aux = aux -1
digit_02 = 11 - (soma % 11)
if digit_02>9:
    new_int.append(0)
else:
    new_int.append(digit_02)  
new_int_final=[]
for value in new_int:
    new_int_final.append(str(value))
cpf = int(cpf)
new_int_final = ''.join(new_int_final)
#print(new_int_final)
new_int_final = int(new_int_final)
print(cpf)
print(new_int_final)
if cpf == new_int_final:
    print('CPF VALID !!!!')
else:
    print('CPF INVALID !!')    