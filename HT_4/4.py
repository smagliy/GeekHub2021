# Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.
def prime_list(start, finish):
    lst = []
    for i in range(start, finish):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


start_d = int(input('Input a start diapason: '))
finish_d = int(input('Input a finish diapason: '))
print(prime_list(start_d, finish_d))