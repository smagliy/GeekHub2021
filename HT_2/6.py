# Написати скрипт, який об'єднає три словника в самий перший.
# Оновлюється тільки перший словник. Дані можна "захардкодити".
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
for d in (dict_1, dict_2, dict_3): dict_1.update(d)
print(dict_1)