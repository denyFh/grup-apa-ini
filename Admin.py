import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()
class Admin:
    def __init__(self, username, password, iD):
        self.__username = username
        self.__password = password
        self.id = iD

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
    def setUsername(self, value):
        self.__username = value
    def setPassword(self, value):
        self.__password = value    
    def detail(self):
        password = len(Admin.getPassword(self))*"*"
        return (f"""=============================================
                 DATA DIRI                   
=============================================
Username = {Admin.getUsername(self)}
Password = {password}
""")