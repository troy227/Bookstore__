import sqlite3
class Database:

    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        cur=self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text, author text,year integer,isbn integer)")
        self.conn.commit()
    def insert(self,title,author,year,isbn):
        cur=self.conn.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
    def view(self):
        cur=self.conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        return rows
    def search(self,title="",author="",year="",isbn=""):
        cur=self.conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        return rows
    def delete(self,id):
        cur=self.conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
    def __del__(self):
        self.conn.close()
