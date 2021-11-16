# Write a script to check whether a specified value is contained in a group of values
list = [1, 5, 8, 3]
number = int(input('Integer number: '))
for i in list:
    if i == number:
        print(True)
        break
    else:
        print(False)
        break
