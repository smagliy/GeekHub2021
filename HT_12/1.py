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
cur.execute("CREATE TABLE IF NOT EXISTS quote (author TEXT, texts_author TEXT, tags TEXT, page INT)")
cur.execute("CREATE TABLE IF NOT EXISTS authors (author TEXT, date_birth TEXT, location_birth TEXT, details TEXT)")
db.commit()


def link_text():
    page_cons = 'http://quotes.toscrape.com'
    page = page_cons
    list_all_links = list()
    while True:
        try:
            page_response = requests.get(page)
            site = BeautifulSoup(page_response.text, 'lxml')
            element_list = site.select('.quote ')
            list_elements_link = []
            for i in element_list:
                element_content = {
                    'author': i.select_one('span small.author').get_text(),
                    'text_author': i.select_one('span.text').get_text().replace("“", '').replace("”", ''),
                    'link_author': page_cons + i.select_one('a').get('href'),
                    'tags': [elem.get_text() for elem in i.select('div.tags a.tag')],
                    'page': page,
                }
                fields = ['Author', 'Text', 'Tags', 'Page']
                with open('quote_authors.csv', 'a', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=fields)
                    writer.writerow({'Author': element_content['author'], 'Text': element_content['text_author'], 'Tags': element_content['tags'],
                                     'Page': element_content['page']})
                cur.execute("INSERT INTO quote (author, texts_author, tags, page) VALUES (?, ?, ?, ?)",
                            (element_content['author'], element_content['text_author'], json.dumps(element_content['tags']), element_content['page']))
                db.commit()
                list_elements_link.append(element_content['link_author'])
            list_all_links.append(list_elements_link)
            start = site.select_one('.pager .next a').get('href')
            page = page_cons + start
        except Exception:
            break
    return list_all_links

link_text()

def link_authors():
    list_all_authors = list()
    list_href_authors = list()
    for el in link_text():
        for el_1 in el:
            href = el_1
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
            fields_2 = ['Author', 'Date birth', 'Location birth', 'Details']
            with open('authors_info.csv', 'a', encoding='utf-8') as file:
                write = csv.DictWriter(file, fieldnames=fields_2)
                write.writerow(
                    {'Author': element_author['author'], 'Date birth': element_author['date_birth'], 'Location birth': element_author['place_birth'],
                     'Details': element_author['details']})
            cur.execute("INSERT INTO authors (author, date_birth, location_birth, details) VALUES (?, ?, ?, ?)",
                        (element_author['author'], element_author['date_birth'], element_author['place_birth'], element_author['details']))
            db.commit()

link_authors()
