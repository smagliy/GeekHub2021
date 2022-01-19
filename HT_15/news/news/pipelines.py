import sqlite3


class NewsPipeline:
    def __init__(self):
        self.con = sqlite3.connect('date.db')
        self.cur = self.con.cursor()

    def crete_table(self):
        self.cur.execute(f"""CREATE TABLE date_post (name_post TEXT, texts TEXT, tags TEXT, link TEXT)""")

    def process_item(self, item, spider):
        self.store_db(item)
        print(f'Pipelines')
        return item

    def store_db(self, item):
        self.cur.execute(f"""INSERT INTO date_post VALUES (?, ?, ?, ?)""", (item['name_post'], item['texts'], item['tags'], item['link']))
        self.con.commit()
