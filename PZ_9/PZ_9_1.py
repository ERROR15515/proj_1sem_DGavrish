# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко,творог, сыр, сахар.
# Определить:
# 1. в каких магазинах нельзя приобрести сыр.
# 2. в каких магазинах можно приобрести одновременно молоко и сахар.
# 3. в каких магазинах можно приобрести соль


magnit = {'молоко', 'соль', 'сахар'}    # ввод переменных
five = {'мясо', 'молоко', 'сыр'}
cross = {'молоко', 'творог', 'сыр', 'сахар'}

if 'сыр' in magnit:
    pass
else:
    print('1) Магнит')
if 'сыр' in five:
    pass
else:
    print('1) Пятерочка')
if 'сыр' in cross:
    pass
else:
    print('1) Перекресток')


if 'молоко' and 'сахар' in magnit & five:
    print('2) Магнит, Пятерочка')
elif 'молоко' and 'сахар' in magnit & cross:
    print('2) Магнит, Перекресток')
elif 'молоко' and 'сахар' in cross & five:
    print('2) Перекресток, Пятерочка')

if 'соль' in magnit:
    print('3) Магнит')
if 'соль' in five:
    print('3) Пятерочка')
elif 'соль' in cross:
    print('3) Перекресток')
