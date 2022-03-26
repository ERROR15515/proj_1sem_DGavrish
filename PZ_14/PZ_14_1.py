# В исходном текстовом файле (Dostoevsky.txt) найти все произведения
# писателя. Посчитать количество полученых элементов.

import re

filet = open('Dostoevsky.txt', 'r', encoding='UTF-8')
a = str(filet.read())

p = re.compile(r'[«]+[A-Я]+[а-я]+[а-я]')
q = p.findall(a)
if "«Время" in q:
    q.remove("«Время")
if "«Эпоха" in q:
    q.remove("«Эпоха")
print(len(set(q)))

