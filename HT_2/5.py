# Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями
# (дублікати значень - видалити). Словник для роботи захардкодити свій.
dict_1 = {'name': 'Kate',
          'surname': 'Petrova',
          'age': 25,
          'experience': 25}
result = {}
for key, value in dict_1.items():
    if value not in result.values():
        result[key] = value
print(result)
