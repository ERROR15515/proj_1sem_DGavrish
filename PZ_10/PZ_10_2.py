# Из предложенного текстового файла (text18-8.txt)
# вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить текст в стихотворной
# форме предварительно удалив букву «с» из текста.

b = str()
n = 0
s = []
f1 = open('text18-8.txt', 'r', encoding='UTF-8')
a = f1.read()
p = ['!', ';', ':', '?', ',', '.', '-', '_', ' ', '…']
for si in a:
    si = si.replace('\n', ' ').replace(' ', '')
    for i in p:
        if i in si:
            si = si.replace(i, '')
    n += len(si)
for i in a:
    s.append(i)
p = ['с', 'С']
for si in a:
    for i in p:
        if i in si:
            si = si.replace(i, '')
    b += si
print(a)

print('Количество буквенных символов в документе: ', n)
f1.close()

f2 = open('text18-8-1.txt', 'w', encoding='UTF-8')
f2.write(str(b))
f1.close()
