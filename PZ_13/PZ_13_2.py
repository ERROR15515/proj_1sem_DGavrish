# Составить генератор (yield), который преобразует
# все буквенные символы в заглавные

def str_to_lower(crs: str):
    for ch in crs:
        yield ch.upper()


user_str = input(str())
print(''.join(str_to_lower(user_str)))
