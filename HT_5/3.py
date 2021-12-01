# На основі попередньої функції створити наступний кусок кода:
#    а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)
#    - як валідні, так і ні;
#    б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#    перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#       Name: vasya
#       Password: wasd
#       Status: password must have at least one digit
#       -----
#       Name: vasya
#       Password: vasyapupkin2000
#       Status: OK
def validation(name, password):
    dict_users = [{name: password} if 3 < len(name) < 50 and len(password) >= 8 and any(map(str.isdigit, password)) else print('Password and name wrong!')]
    if name == password:
        print('Comment: password is`nt equal name')
    else:
        return dict_users


def verification(dict_users):
    for elem in dict_users:
        for key, value in elem.items():
            print(f'Name: {key}')
            print(f'Password: {value}')
            try:
                if validation(key, value):
                    print('Status: OK')
                else:
                    raise Exception
            except Exception:
                print('Status: password must have at least one digit')




dict_use = [{'kate': 'kate1234',
            'anna': 'anna',
            'alex': 'alex123zxdcf'}]
verification(dict_use)