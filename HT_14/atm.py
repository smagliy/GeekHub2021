import sqlite3
import requests
import json

db = sqlite3.connect('DataBase.db')
cur = db.cursor()


class Autorization(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def log_into(self):
        if self.name == 'admin' and self.password == 'admin':
            print(f'Hello superuser {self.name}')
            return 'Admin'
        elif cur.execute("SELECT * FROM users WHERE name=? AND password=?", (self.name, self.password)).fetchone():
            print(f'Hello {self.name}')
            return True
        else:
            print('Login or password wrong!')
            return False

    def add_new_user(self):
        cur.execute("INSERT INTO users (name, password, balance) VALUES (?, ?, ?)", (self.name, self.password, 0))
        db.commit()
        cur.execute("INSERT INTO transactions (name, operation) VALUES (?, ?)", (self.name, ''))
        db.commit()
        print(f'Welcome {self.name}')
        return True


class MethoudsForUsers(Autorization):
    def __init__(self, name, password):
        super(MethoudsForUsers, self).__init__(name, password)

    def transactions(self, operation):
        operations = cur.execute("SELECT operation FROM transactions WHERE name=?", (self.name,)).fetchone()[0]
        operations = operations + ' ' + operation
        cur.execute(f"UPDATE transactions SET operation=? WHERE name=?", (operations, self.name))
        db.commit()

    def get_balance(self):
        self.transactions('Check your balance')
        return cur.execute("SELECT balance FROM users WHERE name=?", (self.name,)).fetchone()[0]

    def currency(self):
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

    def put_some_money(self, sum_of_money):
        if sum_of_money > 0:
            cur.execute("UPDATE users SET balance=balance+? WHERE name=?", (int(sum_of_money), self.name))
            db.commit()
            self.transactions('Replenish the balance')
        else:
            print("Money can’t be negative")

    def take_some_money(self, sum_of_money):
        if sum_of_money > 0:
            if self.get_balance() >= sum_of_money:
                while Bank().atm(sum_of_money):
                    cur.execute("UPDATE users SET balance=balance-? WHERE name=?", (int(sum_of_money), self.name))
                    db.commit()
                    self.transactions('Withdraw money from account')
                    break
            else:
                print('The sum is more how you have on your balance!')
        else:
            print("Money can’t be negative")


class Bank(object):
    def atm(self, money_needed):
        res = cur.execute("SELECT * FROM nominals").fetchall()
        db.commit()
        nom = [int(i[0]) for i in res if i[1] != 0]
        flag = True
        while flag:
            flag = False
            if money_needed // 1000 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("1000",)).fetchone()[0] != 0 and \
                    (money_needed - 1000 == 0 or [i for i in nom if (money_needed - 1000) // i > 0]):
                print('1000hr')
                money_needed -= 1000
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "1000"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            if money_needed // 500 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("500",)).fetchone()[0] != 0 and \
                    (money_needed - 500 == 0 or [i for i in nom if (money_needed - 500) // i > 0]):
                print('500hr')
                money_needed -= 500
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "500"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            if money_needed // 200 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("200",)).fetchone()[0] != 0 and \
                    (money_needed - 200 == 0 or [i for i in nom if (money_needed - 200) // i > 0]):
                print('200hr')
                money_needed -= 200
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "200"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            if money_needed // 100 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("100",)).fetchone()[0] != 0 and \
                    (money_needed - 100 == 0 or [i for i in nom if (money_needed - 100) // i > 0]):
                print('100hr')
                money_needed -= 100
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "100"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            if money_needed // 50 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("50",)).fetchone()[0] != 0 and \
                    (money_needed - 50 == 0 or [i for i in nom if (money_needed - 50) // i > 0]):
                print('50hr')
                money_needed -= 50
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "50"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            if money_needed // 20 > 0 and \
                    cur.execute("SELECT number FROM nominals WHERE nominal=?", ("20",)).fetchone()[0] > 0 and \
                    (money_needed - 20 == 0 or [i for i in nom if (money_needed - 20) // i > 0]):
                print('20hr')
                money_needed -= 20
                cur.execute("UPDATE nominals SET number=number-? WHERE nominal=?", (1, "20"))
                if money_needed == 0:
                    db.commit()
                    break
                else:
                    flag = True
            else:
                print('It is impossible to withdraw such a sum from an ATM!')
                return False
        return True

    def security_guard(self):
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
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_1000hr, "1000"))
                db.commit()
                add_500hr = int(input('How much you want to put in 500hr: '))
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_500hr, "500"))
                db.commit()
                add_200hr = int(input('How much you want to put in 200hr: '))
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_200hr, "200"))
                db.commit()
                add_100hr = int(input('How much you want to put in 100hr: '))
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_100hr, "100"))
                db.commit()
                add_50hr = int(input('How much you want to put in 50hr: '))
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_50hr, "50"))
                db.commit()
                add_20hr = int(input('How much you want to put in 20hr: '))
                cur.execute("UPDATE nominals SET number=number+? WHERE nominal=?", (add_20hr, "20"))
                db.commit()
            else:
                break

class Menu(object):
    def start(self):
        print("""
                1 - Sing in,
                2 - Add new user
                """)
        command = int(input('Write your command: '))
        login = input('Write your login: ')
        password = input('Write your password: ')
        user1 = MethoudsForUsers(login, password)
        if command == 1:
            log = user1.log_into()
            if log == 'Admin':
                Bank().security_guard()
            elif log == True:
                self.menu(user1)
            else:
                print('Some problem with autorization')
        elif command == 2:
            user1.add_new_user()
            self.menu(user1)

    def menu(self, user):
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
                print(f'You have {user.get_balance()} hr in your account')
            elif command == 2:
                amount_on = int(input('Write the amount you want to add: '))
                user.put_some_money(amount_on)
            elif command == 3:
                amount_off = int(input('Write the amount you want withdraw: '))
                user.take_some_money(amount_off)
            elif command == 4:
                user.currency()
            else:
                print('Thank you for your answer. Have a good day!')
                break


Menu().start()