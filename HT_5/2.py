# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
def validation(name, password):
    dict_users = [{name: password} if 3 < len(name) < 50 and len(password) >= 8 and any(map(str.isdigit, password)) else print('Password and name wrong!')]
    if name == password:
        print('password is`nt equal name')
    else:
        return dict_users


name_user = str(input('Please, write your name: '))
password_user = str(input('Please, write your password: '))
print(validation(name_user, password_user))