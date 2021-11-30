# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#    - щось своє :)
#    Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
import re


def validation(name, password):
    list_users = [name if 3 < len(name) < 50 else print('Name wrong!')]
    list_passwords = [password if len(password) >= 8 and any(map(str.isdigit, password)) else print('Password wrong!')]
    return list_users, list_passwords


name_user = str(input('Please, write your name: '))
password_user = str(input('Please, write your password: '))
print(validation(name_user, password_user))