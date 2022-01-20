import sqlite3


class NewsPipeline:
    def __init__(self):
        self.con = sqlite3.connect('date.db')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS date (name_post TEXT, texts TEXT, tags TEXT, link TEXT, date TEXT)")
        self.con.commit()
        self.cur.execute(f"""INSERT INTO date VALUES (?, ?, ?, ?, ?)""", (item['name_post'], item['texts'], item['tags'], item['link'], item['date']))
        self.con.commit()
