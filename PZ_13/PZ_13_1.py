# В последовательности на n целых элементов найти количество пар,
# для которых произведение элементов делится на 3 (элементы пары в
# последовательности являются соседними).

from random import randint

el = int(input('Введите количество элементов: '))
lst = [randint(0, 100) for i in range(el)]
print(lst)
a = 0
b = 0

for i in range(el-1):
    if (lst[i] * lst[i+1]) % 3 == 0:
        a += 1

print(a)