import sqlite3
db = sqlite3.connect('bank.db')
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance INT)")
db.commit()
cur.execute(f"INSERT INTO users VALUES ('user1', 'user1', 100)")
cur.execute(f"INSERT INTO users VALUES ('user2', 'user2', 100)")
cur.execute(f"INSERT INTO users VALUES ('admin', 'admin', 0)")
db.commit()

cur.execute("CREATE TABLE IF NOT EXISTS nominals (nominals TEXT, number INT)")
db.commit()
cur.execute(f"INSERT INTO nominals VALUES ('1000', 10)")
cur.execute(f"INSERT INTO nominals VALUES ('500', 10)")
cur.execute(f"INSERT INTO nominals VALUES ('200', 10)")
cur.execute(f"INSERT INTO nominals VALUES ('100', 10)")
cur.execute(f"INSERT INTO nominals VALUES ('50', 10)")
cur.execute(f"INSERT INTO nominals VALUES ('20', 10)")
db.commit()