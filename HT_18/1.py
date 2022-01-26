# Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
# Документація на АПІ:
# https://github.com/HackerNews/API
# Скрипт повинен отримувати із командного рядка одну із наступних категорій:
# askstories, showstories, newstories, jobstories
# Якщо жодної категорії не указано - використовувати newstories.
# Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
# Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів мають різний набір полів.
# Код повинен притримуватися стандарту pep8.
# Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
import requests
import csv
import fire
import sys

class API(object):
    def __init__(self):
        self.request = requests
        self.list_name = ['askstories', 'showstories', 'jobstories', 'newstories']
        self.dict_elem = {'askstories': ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type'],
                          'showstories': ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type', 'url'],
                          'jobstories': ['by', 'id', 'score', 'text', 'time', 'title', 'type', 'url'],
                          'newstories': ['by', 'descendants', 'id', 'kids', 'score', 'time', 'title', 'type', 'url', 'text']}
        # self.newstories()

    def askstories(self):
        response = self.request.get(f'https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty')
        text = response.json()
        header = self.dict_elem['askstories']
        with open(f'askstories.csv', 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for id in text:
                response_id = self.request.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
                json = response_id.json()
                if json != None:
                    writer.writerow(json)

    def showstories(self):
        response = self.request.get(f'https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty')
        text = response.json()
        header = self.dict_elem['showstories']
        with open(f'showstories.csv', 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for id in text:
                response_id = self.request.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
                json = response_id.json()
                if json != None:
                    writer.writerow(json)

    def jobstories(self):
        response = self.request.get(f'https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty')
        text = response.json()
        header = self.dict_elem['jobstories']
        with open(f'jobstories.csv', 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for id in text:
                response_id = self.request.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
                json = response_id.json()
                if json != None:
                    writer.writerow(json)

    def newstories(self):
        response = self.request.get(f'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
        text = response.json()
        header = self.dict_elem['newstories']
        with open(f'newstories.csv', 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for id in text:
                response_id = self.request.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
                json = response_id.json()
                if json != None:
                    writer.writerow(json)


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'askstories':
            API().askstories()
        elif sys.argv[1] == 'showstories':
            API().showstories()
        elif sys.argv[1] == 'newstories':
            API().newstories()
        elif sys.argv[1] == 'jobstories':
            API().jobstories()
        else:
            print('some problem...')
    except Exception:
        API().newstories()


