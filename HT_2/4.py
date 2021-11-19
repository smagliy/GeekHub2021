#  Написати скрипт, який об'єднає три словника в новий.
# Початкові словники не повинні змінитись. Дані можна "захардкодити".
dict_1 = {'name': 'Kate',
          'surname': 'Petrova'}
dict_2 = {'phone': '21346356',
          'adress': 'Shevchenko street, 23'}
dict_3 = {'age': 36,
          'sex': 'female'}
dict_res = dict_1 | dict_2 | dict_3
print(dict_res)


