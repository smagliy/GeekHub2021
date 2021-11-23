# Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe8pj345" -> просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
string = str(input('Write a string: '))


def function_string(string_f):
    if len(string_f) < 30:
        s = 0
        new_string = ''
        for i in string_f:
            if i.isdigit():
                s += int(i)
            else:
                new_string += i
        print(f'Sum numbers: {s}')
        print(f'The letters in string: {new_string}')
    elif len(string_f) > 50:
        print(f'The string is bigger than 50, it is {len(string_f)}')
    elif 30 <= len(string_f) <= 50:
        print(f'length {len(string_f)}')
        a_1 = []
        a_2 = []
        for i in string_f:
            if i.isdigit():
                a_1.append(i)
            else:
                a_2.append(i)
        print(f'Numbers in the string: {len(a_1)}')
        print(f'Letters in the string: {len(a_2)}')


function_string(string)