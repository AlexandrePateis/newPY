import os
cont = 1
cart =[]
for c in range(3):
    product = str(input(f'Enter the product {cont}: ')).strip().title()
    price = float(input(f'Enter the price dthe product {cont}: '))
    cart.append((product, price))
    cont +=1
    os.system('clear')
print(cart)
total =[]
for p in cart:
    total.append(p[1])
print(total)
print(f'R${sum(total):.2f}')
