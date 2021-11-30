# сі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати
#    документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def range(start, stop, step):
    while start < stop:
        yield start
        start += step


list_range = []
for i in range(3, 10, 1):
    list_range.append(i)
print(list_range)
