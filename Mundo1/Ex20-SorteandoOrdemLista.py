# 20 - Sortear a ordem de apresentação do trabalho
import random

pessoas = ['Tiago Miranda', 'Isabel', 'Yuri', 'Joice', 'Leandro', 
        'Marina', 'Alberto/Adalberto/Roberto/Gabriel', 'Felipe Miranda', 'Samuel', 'Felipe Dias', 
        'Matheus', 'Gabriel Pereira', 'Henrique', 'Micael','Yan', 'Tathiane', 'Mariana',
        'Gabi Maria']
i = 0
while i<19:
    i = i + 1
    print(f'{i} - {random.choice(pessoas)}')

'''
# Ou

from random import shuffle
pessoas = ['Tiago Miranda', 'Isabel', 'Yuri', 'Joice', 'Leandro', 
        'Marina', 'Alberto/Adalberto/Roberto/Gabriel', 'Felipe Miranda', 'Samuel', 'Felipe Dias', 
        'Matheus', 'Gabriel Pereira', 'Henrique', 'Micael','Yan', 'Tathiane', 'Mariana',
        'Gabi Maria']
shuffle(pessoas)
print(f'{pessoas}')

'''