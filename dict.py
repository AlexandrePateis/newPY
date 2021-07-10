import os
print()
qnt_correct = 0
questions = {
    'Question 1':{
        'question': 'Does Mairo speak fluent English?', 
        'Answer': {'a': 'Not', 'b': 'Yes', 'c': 'Rather not answer'},
        'correct_answer': 'b'
    },
    'Question 2':{
        'question': 'How much is 2 x2 ?', 
        'Answer': {'a': '4', 'b': '9', 'c': 'Rather not answer'},
        'correct_answer': 'a'
    },
}

for pk, pv in questions.items(): #Interando: pk = numero da pergunta, pv = pergunta
    print(f'{pk}: {pv["question"]}')  
    for rk, rv in pv['Answer'].items(): #Interando: rk = chave da respota, rv = resposta, pv[Asnwer] = Intera sobre o dicionario de opção de respotas
        print(f'[{rk}]: {rv}')
    your_answer = input('Your answer: ').strip().lower()[0]
    if your_answer == pv['correct_answer']:
        print('CORRECT !!!!!')
        qnt_correct +=1
    print()       
print(f'You got {qnt_correct} questions right !! ')    