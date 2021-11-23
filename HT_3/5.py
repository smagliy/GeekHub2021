# Kористувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi
# змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
x = int(input('Write a number x: '))
y = int(input('Write a number y: '))

def equal(x1, y1):
    if x1 > y1:
        z = x1 - y1
        print(f'x is longer than y at {z}')
    elif x1 < y1:
        z = y1 - x1
        print(f'y is longer than x at {z}')
    elif x1 == y1:
        print('x equals y')
    return x1 - y1


print(equal(x, y))
