import sqlite3

db = sqlite3.connect('libr.db')

# Create Cursor
c = db.cursor()

# c.execute("""CREATE TABLE library (
#     ID INTEGER NOT NULL PRIMARY KEY,
#     title VARCHAR(128) NOT NULL,
#     release_year DATE,
#     author VARCHAR(128) NOT NULL,
#     genre VARCHAR(64) NOT NULL,
#     brief_retelling TEXT DEFAULT '',
#     quotes TEXT DEFAULT '',
#     review TEXT DEFAULT ''
# )""")

# Добавление данных
c.execute("INSERT INTO library VALUES ('', '451', '1953', 'RAY BRADBURY', 'novel', '', '', '')")

# Выборка данных
c.execute("SELECT * FROM library")
print(c.fetchall())

db.commit()

db.close()
