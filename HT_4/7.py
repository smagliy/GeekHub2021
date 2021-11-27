# Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому
def function_list(list_1):
    dict_list = {}
    for i in list_1:
        if i in dict_list:
            dict_list[i] += 1
        else:
            dict_list[i] = 1
    return dict_list


list_1 = map(str, input('write a list without commas: ').split())
print(function_list(list_1))