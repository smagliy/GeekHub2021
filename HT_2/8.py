# Написати скрипт, який отримує від користувача позитивне ціле число і створює словник,
# з ключами від 0 до введеного числа, а значення для цих ключів - це квадрат ключа.
number = int(input('Positive number: '))
dict_1 = dict()
for x in range(1, number+1):
    dict_1[x] = x**2
print(dict_1)
