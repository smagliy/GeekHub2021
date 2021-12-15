import sqlite3
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
        cur.execute(f"INSERT INTO users VALUES (f'{login}', f'{password}', 0)")
        print(f'Welcome {login}')


def get_balance(login):
    return cur.execute("SELECT balance FROM users WHERE username=?", (login,)).fetchone()[0]


def menu(login_1):
    while True:
        print("""
            1 - Check your balance,
            2 - Replenish the balance
            3 - Withdraw money from account
            4 - Exit
        """)
        command = int(input('Write your command: '))
        if command == 1:
            print(f'You have {get_balance(login_1)} hr in your account')
        elif command == 2:
            amount_on = int(input('Write the amount you want to add: '))
            if amount_on > 0:
                cur.execute("UPDATE users SET balance=balance+? WHERE username=?", (amount_on, login_1))
                db.commit()
        elif command == 3:
            amount_off = int(input('Write the amount you want withdraw: '))
            if amount_off > 0:
                if get_balance(login_1) - amount_off < 0:
                    raise Exception('')
                else:
                    while atm(amount_off):
                        cur.execute("UPDATE users SET balance=balance-? WHERE username=?", (amount_off, login_1))
                        db.commit()
                        break
        else:
            print('Thank you for your answer. Have a good day!')
            break


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
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_1000hr, "1000hr"))
            db.commit()
            add_500hr = int(input('How much you want to put in 500hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_500hr, "500hr"))
            db.commit()
            add_200hr = int(input('How much you want to put in 200hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_200hr, "200hr"))
            db.commit()
            add_100hr = int(input('How much you want to put in 100hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_100hr, "100hr"))
            db.commit()
            add_50hr = int(input('How much you want to put in 50hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_50hr, "50hr"))
            db.commit()
            add_20hr = int(input('How much you want to put in 20hr: '))
            cur.execute("UPDATE nominals SET number=number+? WHERE nominals=?", (add_20hr, "20hr"))
            db.commit()
        else:
            break


def atm(money_needed):
    res = cur.execute("SELECT * FROM nominals").fetchall()
    db.commit()
    nom = [int(i[0]) for i in res if i[1] != 0]
    flag = True
    while flag:
        flag = False
        if money_needed // 1000 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("1000",)).fetchone()[0] != 0 and \
                (money_needed - 1000 == 0 or [i for i in nom if (money_needed - 1000) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "1000"))
            db.commit()
            print('1000hr')
            money_needed -= 1000
            if money_needed == 0:
                break
            else:
                flag = True
        if money_needed // 500 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("500",)).fetchone()[0] != 0 and \
                (money_needed - 500 == 0 or [i for i in nom if (money_needed - 500) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "500"))
            db.commit()
            print('500hr')
            money_needed -= 500
            if money_needed == 0:
                break
            else:
                flag = True
        if money_needed // 200 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("200",)).fetchone()[0] != 0 and \
                (money_needed - 200 == 0 or [i for i in nom if (money_needed - 200) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "200"))
            db.commit()
            print('200hr')
            money_needed -= 200
            if money_needed == 0:
                break
            else:
                flag = True
        if money_needed // 100 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("100",)).fetchone()[0] != 0 and \
                (money_needed - 100 == 0 or [i for i in nom if (money_needed - 100) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "100"))
            db.commit()
            print('100hr')
            money_needed -= 100
            if money_needed == 0:
                break
            else:
                flag = True
        if money_needed // 50 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("50",)).fetchone()[0] != 0 and \
                (money_needed - 50 == 0 or [i for i in nom if (money_needed - 50) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "50"))
            db.commit()
            print('50hr')
            money_needed -= 50
            if money_needed == 0:
                break
            else:
                flag = True
        if money_needed // 20 > 0 and cur.execute("SELECT number FROM nominals WHERE nominals=?", ("20",)).fetchone()[0] != 0 and \
                (money_needed - 20 == 0 or [i for i in nom if (money_needed - 20) // i > 0]):
            cur.execute("UPDATE nominals SET number=number-? WHERE nominals=?", (1, "20"))
            db.commit()
            print('20hr')
            money_needed -= 20
            if money_needed == 0:
                break
            else:
                flag = True
        else:
            print('It is impossible to withdraw such a sum from an ATM!')
            return False


start()