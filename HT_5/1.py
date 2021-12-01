# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
#    необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#    Логіка наступна:
#        якщо введено коректну пару ім'я/пароль - вертається <True>;
#        якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція
#        вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
    pass


def list_users():
    list_user = [('kate', 'kate123'),
                 ('anna', 'anna123'),
                 ('alex', 'alex123'),
                 ('jack', 'jack123'),
                 ('ivan', 'ivan123')]
    return list_user


def register(username, password, silent=False):
    try:
        if (username, password) is list_users():
            return True
        elif silent is True:
            return False
    except LoginException:
        print('LoginException')
        raise LoginException


print(register('anna', 'anna123'))
print(register('k', 'kate23', silent=True))
print(register('jack', '2552e'))
