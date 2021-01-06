import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()
#class kelas
class Classes:
    #inisialisasi class object, berisi atribut kelas
    def __init__(self, classname):
        self._classname = classname
    
    #mengambil atribut nama kelas
    def getClassName(self):
        return self._classname