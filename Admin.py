class Admin:
    def __init__(self, username, password, iD=None):
        self.__username = username
        self.__password = password
        self.id = iD

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password