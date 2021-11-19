# Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Max: ', my_dict[key_max])
print('Min: ', my_dict[key_min])