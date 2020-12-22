import sqlite3
DbName = 'db_leslesan.db'


class Connect:
    def __init__(self):
        self.db = sqlite3.connect(DbName)
        self.c = self.db.cursor()