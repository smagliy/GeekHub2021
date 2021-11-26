# Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне,
# збільшити його на 100, якщо дорівнює 0, не змінювати.
def positive_numbers(n):
    if n > 0:
        res = n**2
    elif n < 0:
        res = n + 100
    else:
        res = n
    return res


number = int(input('Write a number: '))
print(positive_numbers(number))