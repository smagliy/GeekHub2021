#http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
# цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
#Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
#пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)
from bs4 import BeautifulSoup
import requests
import csv
import sqlite3
import json

db = sqlite3.connect('Pagination.db')
cur = db.cursor()

def link_number():
    list_all_links = ['http://quotes.toscrape.com']
    page_cons = 'http://quotes.toscrape.com'
    page = page_cons
    while True:
        try:
            page_response = requests.get(page)
            site = BeautifulSoup(page_response.text, 'lxml')
            start = site.select_one('.pager .next a').get('href')
            page = page_cons + start
            list_all_links.append(page)
        except Exception:
            break
    return list_all_links


def page_list(page, number_page):
    page_response = requests.get(page)
    site = BeautifulSoup(page_response.text, 'lxml')
    element_list = site.select('.quote ')
    list_elements = []
    id = 0
    for i in element_list:
        id += 1
        element_content = {
            'author': i.select_one('span small.author').get_text(),
            'text_author': i.select_one('span.text').get_text().replace("“", '').replace("”", ''),
            'tags': [elem.get_text() for elem in i.select('div.tags a.tag')],
            'number_page': number_page,
            }
        list_elements.append(element_content)
    return list_elements


list_all = list()
number = 0
for link in link_number():
    number += 1
    list_elem_one = page_list(link, number)
    list_all.append(list_elem_one)


def append_csv():
    fields = ['Author', 'Text', 'Tags', 'Number page']
    with open('pagination.csv', 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for site in list_all:
            for elem in site:
                writer.writerow({'Author': elem['author'], 'Text': elem['text_author'], 'Tags': elem['tags'], 'Number page': elem['number_page']})


def append_database():
    cur.execute("CREATE TABLE IF NOT EXISTS authors (author TEXT, texts_author TEXT, tags STRING, number_page INT)")
    db.commit()
    for site in list_all:
        for elem in site:
            cur.execute("INSERT INTO authors (author, texts_author, tags, number_page) VALUES (?, ?, ?, ?)", (elem['author'], elem['text_author'], json.dumps(elem['tags']), elem['number_page']))
            db.commit()


append_database()
