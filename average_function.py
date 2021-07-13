while True:
    note1 = float(input('Enter your first note: '))
    if note1 >10:
        print('Invalid note.')
    else:
        break
while True:
    note2 = float(input('Enter your second note: '))
    if note2 >10:
        print('Invalid note.')
    else:
        break
while True:
    note3 = float(input('Enter your third note: '))
    if note3 >10:
        print('Invalid note.')
    else:
        break

word = str(input('Enter a word: ')).strip().lower()
while word != 'p' and word != 'a':
    word = str(input('Enter a word: ')).strip().lower()

def return_average(first_note, second_note, third_note, word):
    if word == 'a':
        average = (first_note + second_note + third_note)/3
        return average
    average = (first_note/5)+(second_note/3)+(third_note/2)
    return average
average_final = return_average(note1, note2, note3, word)

print(f'Your avarege is: {average_final:.2f}')        