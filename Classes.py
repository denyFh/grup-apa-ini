import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()
class Classes:
    def __init__(self, classname):
        self._classname = classname

    def getClassName(self):
        return self._classname