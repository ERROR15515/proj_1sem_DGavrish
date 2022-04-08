# В матрице элементы столбца N (N задать с клавиатуры)
# увеличить в два раза

import random


print('Введите количество строк и столбцов от 1 до 10.')
i, j = int(input('Столбцы: ')), int(input('Строки: '))
mat = [[random.randint(1, 10) for x in range(i)] for y in range(j)]

for i in mat:
    print(i)

n = int(input('Выберите столбец: '))

for i in range(j):
    mat[i][n-1] *= 2

for i in mat:
    print(i)
