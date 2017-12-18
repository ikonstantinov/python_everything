import sqlite3
import os


# c1 = cursor.execute("SELECT * FROM student")
# print(c1.fetchall())
# cursor.execute("INSERT INTO student (name, subj, mark) VALUES (?, ?, ? )", ('Bob', 'Math', 5))
# db.commit()



class Controller:

    def __init__(self, path='/Users/ivan_konstantinov/DjangoProjects/firstdjango/db.sqlite3'):
        self.path = path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()

with Controller() as c:
    c1 = c.execute("SELECT * FROM student")
    for i in c1.fetchall():
        print('Name: {} , Subj: {} , Mark: {} '.format(i[1], i[2], i[3],))

