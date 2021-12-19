# Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
#    Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
#    конвертацію введеної суми з однієї валюти в іншу.
import requests
import json


def converter_currency_on_uah(name_1, summa):
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    with open('api_privat.json', 'w') as f:
        f.write(response.text)
    with open('api_privat.json', 'rb') as read:
        data = json.load(read)
        for i in data:
            if i['ccy'] == name_1:
                print(f'Summa 1: {summa} {name_1}')
                summa_in_ua = summa * float(i['sale'])
                valut = i['base_ccy']
                print(f'Summa in {valut}: {summa_in_ua}')
                return summa_in_ua, valut
            elif name_1 == 'UAH':
                valut = 'UAH'
                summa_in_ua = summa
                return summa_in_ua, valut


def convereter_on():
    print("""USD, EUR, RUR, BTC""")
    list_curr = ['USD', 'EUR', 'RUR', 'BTC', 'UAH']
    name1 = input('Write your currency of your sum: ')
    name2 = input('Write currency to which you want to convert: ')
    currency = int(input('Write your sum: '))
    if name2 in list_curr and name1 in list_curr:
        list_res_fun = converter_currency_on_uah(name1, currency)
        if list_res_fun == [None]:
            raise Exception('Some exceptions')
        else:
            if name2 == list_res_fun[1]:
                converter_currency_on_uah(name1, currency)
                return
            else:
                with open('api_privat.json', 'rb') as read:
                    data = json.load(read)
                    for i in data:
                        if i['ccy'] == name2:
                            res = list_res_fun[0] / float(i['buy'])
                            print(f'Summa in {name2}: {res}')
                            break
    else:
        print('Currency isn`t correct!')


convereter_on()