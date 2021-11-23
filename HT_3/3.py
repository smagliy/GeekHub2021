# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
def season(number_month):
    if 1 <= number_month <= 3:
        print('Winter has come')
    elif 4 <= number_month <= 6:
        print('Spring has come')
    elif 7 <= number_month <= 9:
        print('Summer has come')
    else:
        print('Autumn has come')


month = int(input('Write a number of month: '))
result = season(month)
print(result)