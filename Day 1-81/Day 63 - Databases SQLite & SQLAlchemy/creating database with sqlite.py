import sqlite3

db = sqlite3.connect('books-collection.db')
cursor = db.cursor()
# creating database with sqlite
try:
    cursor.execute("CREATE TABLE books "
                   "(id INTEGER PRIMARY KEY, "
                   "title varchar(250) NOT NULL UNIQUE, "
                   "author varchar(250) NOT NULL, "
                   "rating FLOAT NOT NULL)")
except sqlite3.OperationalError:
    pass
try:
    cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
    db.commit()
except (sqlite3.IntegrityError, sqlite3.OperationalError):
    pass
