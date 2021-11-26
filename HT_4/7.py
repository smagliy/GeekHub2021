# Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому
def function_list(list):
    dict_list = {}
    for i in list:
        if i in dict_list:
            dict_list[i] += 1
        else:
            dict_list[i] = 1
    for item in sorted(dict_list):
        print(item, dict_list[item])
    return


list_1 = list(input('Write a list: '))
print(function_list(list_1))