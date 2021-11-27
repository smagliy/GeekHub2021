# Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
def square(a):
    perimeter = a * 4
    square_a = a**2
    diagonal_of_a_square = a * pow(2, 0.5)
    return perimeter, square_a, diagonal_of_a_square


side_of_a_square = float(input('Please, write a square side value: '))
print(square(side_of_a_square))