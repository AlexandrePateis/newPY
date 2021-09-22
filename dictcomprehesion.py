while True:
    num = int(input('Qual número deseja ver a tabuada ?'))
    for c in range(1, 11):
        print(f'{num}x{c} = {num * c}')
    op = int(input('Desja consultar niovamente ? 1-siim - 2 nao'))
    if op == 2:
        break    