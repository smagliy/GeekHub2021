# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя
# яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
def calculator(operation, x, y):
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            print(f'Sum x and y equal: {x+y}')
        elif operation == '-':
            print(f'Difference x and y equal: {x-y}')
        elif operation == '*':
            print(f'Multiplication x and y equal: {x*y}')
        elif operation == '/':
            print(f'Dividing x and y equal: {x/y}')
    else:
        print('Unfortunately, there is no such operation!')


number_1 = float(input('Write x='))
number_2 = float(input('Write y='))
operation_1 = input('Write operation (+, -, *, /): ')
calculator(operation_1, number_1, number_2)