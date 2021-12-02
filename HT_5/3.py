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
    try:
        if 3 < len(name) < 50:
            if len(password) >= 8:
                if any(map(str.isdigit, password)):
                    return "OK"
                else:
                    raise Exception("Password doesn't have one or more digit")
            else:
                raise Exception("Password doesn't have 8 and more symbols")
        else:
            raise Exception("Password doesn't have 8 and more symbols")
    except Exception as err:
       return err


def verification(dict_users):
    for elem in dict_users:
        for key, value in elem.items():
            print(f'Name: {key}')
            print(f'Password: {value}')
            if validation(key, value):
                status = validation(key, value)
            print(f'Status: {status}')


dict_use = [{'kate': 'kate1234',
            'anna': 'anna',
            'alex': 'alex123zxdcf'}]
verification(dict_use)