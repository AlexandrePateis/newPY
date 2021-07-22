'''product = [
    {'name':'p1', 'price': 50},
    {'name':'p2', 'price': 22},
    {'name':'p3', 'price': 33},
    {'name':'p4', 'price': 47},
    {'name':'p5', 'price': 2},
    {'name':'p6', 'price': 18},
    {'name':'p7', 'price': 36},
    {'name':'p8', 'price': 28},
    {'name':'p9', 'price': 19},
    {'name':'p10', 'price': 37}
]
for p in product:
    print(p)
    new = [p['price']*2 for p in product]
print()
#print(new)
i=0
for p in product:
    p['price'] = new[i]
    i+=1
for p in product:
    print(p)            
print()
def more_20(p):
    p['price'] = p['price'] * 4
    return p
new_price = list(map(more_20, product))
for r in new_price:
    print(r)

'''
#Nova a partir daqui


def check_if_number(num):
    try:
        num = int(num)
        return num
    except ValueError:
        try:
            num = float(num)
            return num
        except ValueError:
            pass        




while True:
    number = check_if_number(input('Enter a number: '))
    if number is None:
        print('Erro: isso não é um número.')
    else:
        print(number)    

