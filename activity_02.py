def date(months):
    meses = ('January', 'February', 'March'
    , 'April', 'May', 'June', 'July', 'August', 'September',
    'October November December')
    month_associate = meses[month - 1]
    return month_associate
while True:
    day = int(input('Enter your birth day: '))
    if day > 31 or day <0:
        print('Invalid day !!')   
    else:
        break
while True:
    month = int(input('Enter the month of your birth: '))
    if month >12 or month <=0:
        print('Invalid month !!')
    else:
        break
while True:
    year = int(input('Enter the year of your birth: '))
    if year > 2021 and month < 1910:
        print('Invalid year !!!')
    else:
        break
date(month)    
print(f'Your date of birth is:{date(month)}/{day}/{year}')    