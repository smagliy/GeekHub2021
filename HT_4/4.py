# Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.
def prime_list(start, finish):
    a = []
    for i in range(start, finish):
        for i_1 in range(2, i):
            if not i % i_1:
                a.append(i)
                break
    return a


start_d = int(input('Input a start diapason: '))
finish_d = int(input('Input a finish diapason: '))
print(prime_list(start_d, finish_d))