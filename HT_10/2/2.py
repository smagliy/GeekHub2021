# Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
#    - Перелік валют краще принтануть.
#    - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
#    - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
#    - Також перевірте, чи введена правильна валюта.
#    Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
#    курсу обраної валюти (Нацбанк) від введеної дати до поточної.
import datetime
import json
import requests


def currency_on_date(currency, date_before):
    print("""
        Exchange Rate: USD, EUR, RUR, CHF, GBP, PLZ, SEK, XAU, CAD
        """)
    d = datetime.datetime.strptime(date_before, '%d.%m.%Y')
    delta = datetime.timedelta(days=1)
    res = datetime.datetime.now() - d
    print(res.days)
    print(f'Currency: {currency}')
    for i in range(res.days):
        new_d = datetime.datetime.strftime(d, '%d.%m.%Y')
        response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={new_d}')
        d += delta
        with open('nb.json', 'w') as f:
            f.write(response.text)
        with open('nb.json', 'rb') as read:
            data = json.load(read)
            for elem in data['exchangeRate']:
                for key in elem:
                    if elem[key] == currency:
                        print(f"""
                        Date: {new_d}
                        NBU:  {elem['saleRateNB']}
                        """)


date = input('Enter a date (i.e. 01.12.2014): ')
curr = input('Write currency: ')
currency_on_date(curr, date)