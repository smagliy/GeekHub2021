#Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто, функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки -
# пересуваємо елементи з початку списку в його кінець).
def list_reversed(lst, n):
    if n > 0:
        for i in range(n):
            lst.append(lst.pop(0))
    elif n < 0:
        for i in range(n):
            lst.insert(0, lst.pop())
    return lst


list_2 = [4, 5, 6, 7, 8, 9, 0]
step = int(input('Write a step: '))
print(list_reversed(list_2, step))