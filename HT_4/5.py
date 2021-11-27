# Написати функцію < fibonacci >, яка приймає один
# аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fibonacci(number):
    fib1 = fib2 = 1
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


num = int(input('Write a number: '))
print(fibonacci(num))