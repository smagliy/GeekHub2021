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


def link_text():
    page_cons = 'http://quotes.toscrape.com'
    page = page_cons
    list_all_text = list()
    while True:
        try:
            page_response = requests.get(page)
            site = BeautifulSoup(page_response.text, 'lxml')
            element_list = site.select('.quote ')
            list_elements_text = []
            for i in element_list:
                element_content = {
                    'author': i.select_one('span small.author').get_text(),
                    'text_author': i.select_one('span.text').get_text().replace("“", '').replace("”", ''),
                    'link_author': page_cons + i.select_one('a').get('href'),
                    'tags': [elem.get_text() for elem in i.select('div.tags a.tag')],
                    'page': page,
                }
                list_elements_text.append(element_content)
            list_all_text.append(list_elements_text)
            start = site.select_one('.pager .next a').get('href')
            page = page_cons + start
        except Exception:
            break
    return list_all_text


def link_authors():
    list_all_authors = list()
    list_href_authors = list()
    for el in link_text():
        for el_1 in el:
            href = el_1['link_author']
            list_href_authors.append(href)
    list_href_authors_new = list(set(list_href_authors))
    for link in list_href_authors_new:
        page_response = requests.get(link)
        site = BeautifulSoup(page_response.text, 'lxml')
        element_list = site.select('.author-details')
        list_elements_authors = list()
        for i in element_list:
            element_author = {
                'author': i.select_one('.author-title').get_text().replace("\n", ''),
                'date_birth': i.select_one('.author-born-date').get_text(),
                'place_birth': i.select_one('.author-born-location').get_text(),
                'details': i.select_one('.author-description').get_text().replace("\n", '')
            }
            list_elements_authors.append(element_author)
        list_all_authors.append(list_elements_authors)
    return list_all_authors


def append_csv():
    fields = ['Author', 'Text', 'Tags', 'Page']
    with open('quote_authors.csv', 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        #writer.writeheader()
        for site in link_text():
            for elem in site:
                writer.writerow({'Author': elem['author'], 'Text': elem['text_author'], 'Tags': elem['tags'], 'Page': elem['page']})
    fields_2 =['Author', 'Date birth', 'Location birth', 'Details']
    with open('authors_info.csv', 'a', encoding='utf-8') as file:
        write = csv.DictWriter(file, fieldnames=fields_2)
        #write.writeheader()
        for authors in link_authors():
            for elem in authors:
                write.writerow({'Author': elem['author'], 'Date birth': elem['date_birth'], 'Location birth': elem['place_birth'], 'Details': elem['details']})


append_csv()

def append_database():
    cur.execute("CREATE TABLE IF NOT EXISTS quote (author TEXT, texts_author TEXT, tags TEXT, page INT)")
    cur.execute("CREATE TABLE IF NOT EXISTS authors (author TEXT, date_birth TEXT, location_birth TEXT, details TEXT)")
    db.commit()
    for site in link_text():
        for elem in site:
            cur.execute("INSERT INTO quote (author, texts_author, tags, page) VALUES (?, ?, ?, ?)", (elem['author'], elem['text_author'], json.dumps(elem['tags']), elem['page']))
            db.commit()
    for link in link_authors():
        for elem in link:
            cur.execute("INSERT INTO authors (author, date_birth, location_birth, details) VALUES (?, ?, ?, ?)", (elem['author'], elem['date_birth'], elem['place_birth'], elem['details']))
            db.commit()


append_database()
