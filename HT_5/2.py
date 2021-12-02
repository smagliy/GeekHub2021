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
                    print('User is registered')
                    return dict_users
                else:
                    raise Exception("Password doesn't have one or more digit")
            else:
                raise Exception("Password doesn't have 8 and more symbols")
        else:
            raise Exception("Password doesn't have 8 and more symbols")
    except Exception as err:
        return err



print(validation('cvbnjk,', 'xcfghjkl,m1'))
print(validation('kate1234', 'katezxcvbnm'))
print(validation('as', 'asdfghjkl1'))


