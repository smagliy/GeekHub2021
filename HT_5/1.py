# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
#    необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#    Логіка наступна:
#        якщо введено коректну пару ім'я/пароль - вертається <True>;
#        якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція
#        вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
    pass


def register(username, password, silent=False):
    list_user = [('kate', 'kate123'),
                 ('anna', 'anna123'),
                 ('alex', 'alex123'),
                 ('jack', 'jack123'),
                 ('ivan', 'ivan123')]
    try:
        if (username, password) is list_user:
            return True
        elif (username, password) is not list_user and silent is True:
            return False
    except LoginException:
        return 'LoginException'


print(register('kate', 'kate123', silent=False))
print(register('k', 'kate23', silent=True))
print(register('kate', 'kate', silent=False))
