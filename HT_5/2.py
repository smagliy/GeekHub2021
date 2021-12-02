# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
def validation(name, password):
    try:
        if 3 < len(name) < 50:
            if len(password) >= 8:
                if any(map(str.isdigit, password)):
                    dict_users = [{name: password}]
                    print(dict_users)
                else:
                    print("Password doesn't have one or more digit")
                    raise Exception
            else:
                print("Password doesn't have 8 and more symbols")
                raise Exception
        else:
            print('Name must have more than 3 characters and less than 50 characters')
            raise Exception
    except Exception:
        print("Login excepted")


print(validation('cvbnjk,', 'xcfghjkl,m1'))
print(validation('kate1234', 'katezxcvbnm'))
print(validation('as', 'asdfghjkl1'))


