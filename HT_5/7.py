# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає
# генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із
# послідовності - ітерація починається знову.
def generation(list_generated):
    while True:
        for i in list_generated:
            yield i


list_numbers = [1, 2, 3, 5]
for number in generation(list_numbers):
    print(number)