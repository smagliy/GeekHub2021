# сі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати
#    документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def range_1(start, stop=0, step=1):
    if stop == 0 and step == 1:
        while 0 < abs(start - stop):
            yield stop
            stop += step
    else:
        while 0 < abs(stop - start):
            yield start
            start += step


list_range = []
for i in range_1(0):
    list_range.append(i)
print(list_range)

list_range_1 = []
for i in range_1(2, 10):
    list_range_1.append(i)
print(list_range_1)

list_rang = []
for i in range_1(20, 10, -2):
    list_rang.append(i)
print(list_rang)


