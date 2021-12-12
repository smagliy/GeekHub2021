#Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити"
#   деяку кількість банкнот (вибирається номінал і кількість).
#   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість
#   банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота,
#   а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн.,
#   а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо),
#   а потрібно було 100 + 20 + 20 + 20 ).
# Особливості реалізації:
#   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#    - переглянути наявні купюри;
#     - змінити кількість купюр;
#   - видача грошей для користувачів відбувається в межах наявних купюр;
#   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію,
#   банкомати все, що в нього входить, відкладає в окрему касету.
#2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і
# напишіть весь код наново (завдання на самоконтроль). До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
import json
import csv

dict_m = {1: "Check your balance",
                 2: "Replenish the balance",
                 3: "Withdraw money from account",
                 4: "Exit"}


def start():
    print('1 - Sign in,  2 - Add a new user, 3 - admin')
    command = int(input('Write your command: '))
    if command == 1:
        menu(dict_m)
    elif command == 2:
        user_new()
        menu(dict_m)
    else:
        security_guard()


def menu(dict_menu):
    name1 = input('Write your name: ')
    password1 = input('Write your password: ')
    authorization(name1, password1)
    for i in range(5):
        print('''
                                              1 - "Check your balance",
                                              2 - "Replenish the balance",
                                              3 - "Withdraw money from account",
                                              4 - "Exit"
                                          ''')
        res = int(input('Write your command: '))
        transaction(name1, dict_menu[res])
        if res == 1:
            check_balance(name1)
        elif res == 2:
            add_sum = int(input('Write amount: '))
            add_and_get_balance(name1, add_sum)
        elif res == 3:
            get_sum = int(input('Write amount: '))
            add_and_get_balance(name1, sum_on=0, sum_off=get_sum)
        else:
            print('Thank you for your answer. Have a good day!')
            break


def security_guard():
    name = input('Write your name: ')
    password = input('Write your password: ')
    if name == 'admin' and password == 'admin':
        while True:
            print(' 1 - Screen how many bills are left, 2 - Change the number of bills, 3 - Exit')
            res = int(input('Write your command: '))
            with open('atm.json') as security:
                data = json.load(security)
                if res == 2:
                    component_1000hr = input('How many bills do you want to put in the 1000 hryvnias compartment? Put: ')
                    data["1000hr"] += int(component_1000hr)
                    component_500hr = input('How many bills do you want to put in the 500 hryvnias compartment? Put: ')
                    data["500hr"] += int(component_500hr)
                    component_200hr = input('How many bills do you want to put in the 200 hryvnias compartment? Put: ')
                    data["200hr"] += int(component_200hr)
                    component_100hr = input('How many bills do you want to put in the 100 hryvnias compartment? Put: ')
                    data["100hr"] += int(component_100hr)
                    component_50hr = input('How many bills do you want to put in the 50 hryvnias compartment? Put: ')
                    data["50hr"] += int(component_50hr)
                    component_20hr = input('How many bills do you want to put in the 20 hryvnias compartment? Put: ')
                    data["20hr"] += int(component_20hr)
                    print(data)

                    with open("atm.json", 'w') as outfile:
                        json.dump(data, outfile)
                elif res == 1:
                    print(data)
                else:
                    break


def authorization(name, password):
    with open('users.csv', 'rt') as user:
        user_read = csv.DictReader(user, delimiter=',')
        for row in user_read:
            if name == row['Name']:
                if password == row['Password']:
                    return
                else:
                    raise Exception('Password wrong')
            else:
                raise Exception('Name wrong')

def transaction(name, operation):
    file = f'{name}_transaction.json'
    new_operation = {"operation": operation}
    with open(file) as operation:
        data = json.load(operation)
        data["Operation"].append(new_operation)

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def user_new():
    name = input('Write your name: ')
    password = input('Write your password: ')
    fields = ['Name', 'Password']
    with open("users.csv", "a") as new:
        writer = csv.DictWriter(new, fieldnames=fields)
        writer.writerow({'Name': name, 'Password': password})
    file_name = f'{name}_balance.txt'
    with open(file_name, 'w') as new_file:
        new_file.write("0")
    file_name1 = f'{name}_transaction.json'
    with open(file_name1, 'w') as new_file:
        json.dump({"Name": f"{name}", "Operation": []}, new_file)
    print('Congratulations!! New user append')


def check_balance(name):
    file = f'{name}_balance.txt'
    with open(file) as check:
        for row in check:
            print(f'You have {row} hr in your account!')


def add_and_get_balance(name, sum_on=0, sum_off=0):
    file = f'{name}_balance.txt'
    with open(file, 'r+') as file:
        if sum_on > 0:
            for row in file:
                final_balance = int(row) + sum_on
                print(f'You have {final_balance} in account after operation!')
                file.seek(0)
                file.write(str(final_balance))
                break
            else:
                raise Exception("Money isn't negative number!")
        elif sum_off > 0:
            for row in file:
                if int(row) > sum_off:
                    atm(sum_off)
                    final_balance_1 = int(row) - sum_off
                    print(f'You have {final_balance_1} in account after operation!')
                    file.seek(0)
                    file.write(str(final_balance_1))
                    break
                else:
                    print("The money isn't a negative number or you wrote a larger amount than you have!")
                    break


def atm(need_money):
    with open("atm.json", "r+") as file:
        data = json.load(file)
        a = 0
        while True:
            if need_money >= 1000 and data['1000hr'] > 0:
                data['1000hr'] -= 1
                print('1000 hr')
                a = a + 1000
                need_money = need_money - 1000
                continue
            elif need_money >= 500 < 1000 and data['500hr'] > 0:
                data['500hr'] -= 1
                print('500hr')
                a = a + 500
                need_money = need_money - 500
                continue
            elif need_money >= 200 < 500 and data['200hr'] > 0:
                data['200hr'] -= 1
                print('200 hr')
                a = a + 200
                need_money = need_money - 200
                continue
            elif need_money >= 100 < 200 and data['100hr'] > 0:
                data['100hr'] -= 1
                print('100 hr')
                a = a + 100
                need_money = need_money - 100
                continue
            elif need_money >= 50 < 100 and data['50hr'] > 0:
                data['50hr'] -= 1
                print('50 hr')
                a = a + 50
                need_money = need_money - 50
                continue
            elif need_money >= 20 < 50 and data['20hr'] > 0:
                data['20hr'] -= 1
                print('20 hr')
                a = a + 20
                need_money = need_money - 20
                continue
            elif need_money == 0:
                print(data)
                break
            else:
                print(f'Try another amount! You can have {a}hr')
                break

    with open("atm.json", 'w') as outfile:
        json.dump(data, outfile)


start()