# Write a script to concatenate N strings
number = int(input('Number: '))
list = []
for a in range(number):
    b = input("string :")
    list.append(b)
    a += 1
print(''.join(list))
