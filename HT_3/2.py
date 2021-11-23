# Користувачем вводиться початковий і кінцевий рік. Створити цикл,
# який виведе всі високосні роки в цьому проміжку (границі включно).
year_start = int(input('Year: '))
year_end = int(input('Year: '))
for i in range(year_start, year_end):
    if i % 400 == 0:
        print(i)
    elif i % 4 == 0 and i % 100 != 0:
        print(i)
