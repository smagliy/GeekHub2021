# Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
# сума цифр кожного елемент якого буде дорівнювати 10.
#    Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]

def generator():
    generator_list = [item for item in range(100) if sum(map(int, str(item))) == 10]
    return generator_list


print(generator())