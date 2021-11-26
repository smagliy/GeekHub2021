# Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте, и False - якщо ні.
def is_prime(n):
    for i in range(2, n):
        if not n % i:
            return True
    return False


number_input = int(input('Please, write number from 0 to 1000: '))
print(is_prime(number_input))