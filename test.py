import sqlite3

db = sqlite3.connect('base.sqlite')

# Create Cursor
c = db.cursor()

c.execute("""CREATE TABLE mylibrary (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(128) NOT NULL,
    release_year DATE,
    author VARCHAR(128) NOT NULL,
    genre VARCHAR(64) NOT NULL,
    brief_retelling TEXT DEFAULT '',
    quotes TEXT DEFAULT '',
    review TEXT DEFAULT ''
 )""")

# Добавление данных
#c.execute("INSERT INTO library3 VALUES ('1', '451', '1953', 'RAY BRADBURY', 'novel', '', '', '')")

# Выборка данных
c.execute("SELECT * FROM mylibrary")
print(c.fetchall())

db.commit()

db.close()
