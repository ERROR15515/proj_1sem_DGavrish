# В матрице элементы последней строки заменить на 0.

import random


print('Введите количество строк и столбцов от 1 до 10.')
a, b = int(input('Столбцы: ')), int(input('Строки: '))
mat = [[random.randint(1, 10) for x in range(a)] for y in range(b)]

for i in range(a):
    mat[b-1][i] = 0

for i in mat:
    print(i)
