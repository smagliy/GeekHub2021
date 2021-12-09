# Програма-банкомат.
#    Створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#Введіть дію:
#           1. Продивитись баланс
#          2. Поповнити баланс
#          3. Вихід
#     - далі - фантазія і креатив :)
import csv
import json


def start():
    dict_menu = {1: "Sell and your balance",
                 2: "Replenish the balance",
                 3: "Add new user",
                 4: "Withdraw money from account",
                 5: "Exit"}
    for i in range(5):
        print('''
                1 - "Sell and your balance",
                2 - "Replenish the balance",
                3 - "Add new user",
                4 - "Withdraw money from account",
                5 - "Exit"
            ''')
        res = int(input('Write your command: '))
        if res == 1 or res == 2 or res == 4:
            name_1 = input('Write your name: ')
            password_1 = input('Write your password ')
            authorization(name_1, password_1)
            transaction(name_1, dict_menu[res])
            if res == 1:
                balance(name_1)
            elif res == 2:
                sum_on1 = int(input('How much you want to deposit in your account '))
                balance(name_1, sum_on1)
            else:
                sum_off1 = int(input('How much you want to withdraw from your account'))
                balance(name_1, sum_on=0, sum_off=sum_off1)
        elif res == 3:
            user_new()
        else:
            print('Thank you for your answer. Have a good day!')
            break


def user_new():
    name = input('Write your name: ')
    password = input('Write your password ')
    fields = ['Name', 'Password']
    with open('users.csv', 'a') as new_user:
        writer = csv.DictWriter(new_user, fieldnames=fields)
        writer.writerow({'Name': name, 'Password': password})
    file_name = f'{name}_balance.txt'
    with open(file_name, 'w') as new_file:
        new_file.write("0")
    file_name1 = f'{name}_transaction.json'
    with open(file_name1, 'w') as new_file:
        json.dump({"Name": f"{name}", "Operation": []}, new_file)
    print('Congratulations!! New user append')


def authorization(name, password):
    with open('users.csv', 'rt') as user:
        user_read = csv.DictReader(user, delimiter=',')
        for row in user_read:
            if name == row['Name']:
                if password == row['Password']:
                    return
                else:
                    raise Exception('Password and name wrong')


def transaction(name, operation):
    file = f'{name}_transaction.json'
    new_operation = {"operation": operation}
    with open(file) as operation:
        data = json.load(operation)
        data["Operation"].append(new_operation)

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def balance(name, sum_on=0, sum_off=0):
    file = f'{name}_balance.txt'
    with open(file, 'r+') as file:
        print(f'You have {file.read()} in your account!')
        if sum_off > 0 and sum_on > 0:
            for row in file:
                if int(row) > sum_off:
                    a = int(row) + sum_on - sum_off
                    print(f'You have {a} in your account after operation!')
                else:
                    raise Exception('The value you want to remove is too great or the value is`nt positive number')
            file.seek(0)
            file.write(str(a))


start()
