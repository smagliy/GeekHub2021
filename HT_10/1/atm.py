# Доповніть програму-банкомат наступним функціоналом:
#    - новий пункт меню, який буде виводити поточний курс валют (API Приватбанк)
import sqlite3
import requests
import json
db = sqlite3.connect('bank.db')
cur = db.cursor()


def start():
    print("""
        1 - Sing in,
        2 - Add new user
        """)
    command = int(input('Write your command: '))
    login = input('Write your login: ')
    password = input('Write your password: ')
    user_search = (login, password)
    if command == 1:
        if login == 'admin' and password == 'admin':
            print(f'Hello {login}...')
            security_guard()
        else:
            if cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user_search[0], user_search[1])).fetchone():
                print(f'Hello user {login}')
                db.commit()
                menu(login)
            else:
                raise Exception('Login or password wrong!')
    elif command == 2:
        cur.execute(f"INSERT INTO users (username, password, balance) VALUES (?, ?, 0)", (login, password))
        db.commit()
        file_name1 = f'{login}_transaction.json'
        with open(file_name1, 'w') as new_file:
            json.dump({"Name": f"{login}", "Operation": []}, new_file)
        print(f'Welcome {login}')


def get_balance(login):
    return cur.execute("SELECT balance FROM users WHERE username=?", (login,)).fetchone()[0]


def transaction(name, operation):
    file = f'{name}_transaction.json'
    new_operation = {"operation": operation}
    with open(file) as operation:
        data = json.load(operation)
        data["Operation"].append(new_operation)

    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def menu(login_1):
    dict_operation = {1: 'Check your balance', 2: 'Replenish the balance', 3: 'Withdraw money from account'}
    while True:
        print("""
            1 - Check your balance,
            2 - Replenish the balance
            3 - Withdraw money from account
            4 - Currency
            5 - Exit
        """)
        command = int(input('Write your command: '))
        if command == 1:
            transaction(login_1, dict_operation[command])
            print(f'You have {get_balance(login_1)} hr in your account')
        elif command == 2:
            amount_on = int(input('Write the amount you want to add: '))
            transaction(login_1, dict_operation[command])
            if amount_on > 0:
                cur.execute("UPDATE users SET balance=balance+? WHERE username=?", (amount_on, login_1))
                db.commit()
        elif command == 3:
            amount_off = int(input('Write the amount you want withdraw: '))
            if amount_off > 0:
                if get_balance(login_1) - amount_off < 0:
                    raise Exception('Some exception')
                else:
                    while atm(amount_off):
                        cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (amount_off, login_1))
                        db.commit()
                        transaction(login_1, dict_operation[command])
                        break
        elif command == 4:
            currency()
        else:
            print('Thank you for your answer. Have a good day!')
            break


def currency():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    with open('api.json', 'w') as f:
        f.write(response.text)
    with open('api.json', 'rb') as read:
        data = json.load(read)
        for i in data:
            curr = i['ccy']
            base_curr = i['base_ccy']
            buy = i['buy']
            sale = i['sale']
            print(f'{curr} sale: {sale} {base_curr}, buy: {buy} {base_curr}')


def security_guard():
    while True:
        print('''
         1 - Screen how many bills are left, 
         2 - Change the number of bills, 
         3 - Exit'
        ''')
        command = int(input('Write your command: '))
        if command == 1:
            res = cur.execute("SELECT * FROM nominals").fetchall()
            print(res)
        elif command == 2:
            add_1000hr = int(input('How much you want to put in 1000hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_1000hr, "1000"))
            db.commit()
            add_500hr = int(input('How much you want to put in 500hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_500hr, "500"))
            db.commit()
            add_200hr = int(input('How much you want to put in 200hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_200hr, "200"))
            db.commit()
            add_100hr = int(input('How much you want to put in 100hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_100hr, "100"))
            db.commit()
            add_50hr = int(input('How much you want to put in 50hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_50hr, "50"))
            db.commit()
            add_20hr = int(input('How much you want to put in 20hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_20hr, "20"))
            db.commit()
        else:
            break


def atm(money_needed):
    res = cur.execute("SELECT * FROM nominals").fetchall()
    db.commit()
    nom = [int(i[0]) for i in res if i[1] != 0]
    flag = True
    hr1000 = 0
    hr500 = 0
    hr200 = 0
    hr100 = 0
    hr50 = 0
    hr20 = 0
    while flag:
        flag = False
        if money_needed // 1000 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("1000",)).fetchone()[0] != 0 and \
                (money_needed - 1000 == 0 or [i for i in nom if (money_needed - 1000) // i > 0]):
            hr1000 += 1
            print('1000hr')
            money_needed -= 1000
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr1000, "1000"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        if money_needed // 500 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("500",)).fetchone()[0] != 0 and \
                (money_needed - 500 == 0 or [i for i in nom if (money_needed - 500) // i > 0]):
            hr500 += 1
            print('500hr')
            money_needed -= 500
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr500, "500"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        if money_needed // 200 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("200",)).fetchone()[0] != 0 and \
                (money_needed - 200 == 0 or [i for i in nom if (money_needed - 200) // i > 0]):
            hr200 += 1
            print('200hr')
            money_needed -= 200
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr200, "200"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        if money_needed // 100 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("100",)).fetchone()[0] != 0 and \
                (money_needed - 100 == 0 or [i for i in nom if (money_needed - 100) // i > 0]):
            hr100 += 1
            print('100hr')
            money_needed -= 100
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr100, "100"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        if money_needed // 50 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("50",)).fetchone()[0] != 0 and \
                (money_needed - 50 == 0 or [i for i in nom if (money_needed - 50) // i > 0]):
            hr50 += 1
            print('50hr')
            money_needed -= 50
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr50, "50"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        if money_needed // 20 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("20",)).fetchone()[0] != 0 and \
                (money_needed - 20 == 0 or [i for i in nom if (money_needed - 20) // i > 0]):
            hr20 += 1
            print('20hr')
            money_needed -= 20
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (hr20, "20"))
            if money_needed == 0:
                db.commit()
                break
            else:
                flag = True
        else:
            print('It is impossible to withdraw such a sum from an ATM!')
            return False
    return True


start()