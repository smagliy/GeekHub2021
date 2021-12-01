# сі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати
#    документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def range_1(start, stop, step):
    while 0 < abs(stop-start):
        yield start
        start += step


list_range = []
for i in range_1(10, 4, -1):
    list_range.append(i)
print(list_range)
