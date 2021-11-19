# Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями
# (дублікати значень - видалити). Словник для роботи захардкодити свій.
dict_1 = {'name': 'Kate',
          'surname': 'Petrova',
          'age': 25,
          'experience': 25}
temp = []
for key, value in list(dict_1.items()):
    if value not in temp:
        temp.append(value)
    else:
        dict_1.pop(key, value)
print(dict_1)
