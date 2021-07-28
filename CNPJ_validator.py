first_digit = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
second_digit = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
while True:
    number_cnpj = str(input('Enter your CNPJ: '))
    cnpj_str = str(number_cnpj)
    provisional_list = [i for i in cnpj_str]
    # print(len(provisional_list))
    if len(provisional_list) == 14:
        break
    else:
        print('Invalid CNPJ.')

cnpj_int = [int(i) for i in provisional_list]
cnpj_int_minus_two = [i for i in cnpj_int[0:12]]

# print(cnpj_int)
# print(cnpj_int_minus_two)

first_digit_definit = [x * y for x, y in zip(cnpj_int_minus_two, first_digit)]
# print(first_digit_definit)
sum_tot = sum(first_digit_definit)
first_digit_num = 11 - (sum_tot % 11)
if first_digit_num > 9:
    cnpj_int_minus_two.append(0)
else:
    cnpj_int_minus_two.append(first_digit_num)
# print(f'{cnpj_int_minus_two}')
sum_tot = 0
second_digit_definit = [x * y for x, y in zip(cnpj_int_minus_two, second_digit)]

sum_tot = sum(second_digit_definit)
second_digit_num = 11 - (sum_tot % 11)
if second_digit_num > 9:
    cnpj_int_minus_two.append(0)
else:
    cnpj_int_minus_two.append(second_digit_num)

if cnpj_int == cnpj_int_minus_two:
    print('CNPJ VALID !!')
    complete1 = [str(i) for i in cnpj_int]
    complete2 = [str(i) for i in cnpj_int_minus_two]
    for i in complete1:
        print(i, end='')
    print()
    for i in complete2:
        print(i, end='')
else:
    print('CNPJ INVALID !!')
    complete1 = [str(i) for i in cnpj_int]
    complete2 = [str(i) for i in cnpj_int_minus_two]
    for i in complete1:
        print(i, end='')
    print()
    for i in complete2:
        print(i, end='')
