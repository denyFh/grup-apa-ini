import sqlite3
from abc import ABC, abstractmethod
import os
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class User(ABC):
    def __init__(self, nama, gender, alamat, phone, iD):
        self._nama = nama
        self._gender = gender
        self._alamat = alamat
        self._phone = phone
        self.id = iD

    def getNama(self):
        return self._nama
    
    def setNama(self, nama):
        self._nama = nama

    def getGender(self):
        return self._gender

    def setGender(self,gender):
        self._gender = gender

    def getAlamat(self):
        return self._alamat

    def setAlamat(self, alamat):
        self._alamat = alamat

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    @abstractmethod
    def dataDiri(self):
        pass
    
    @abstractmethod
    def lihatJadwal(self):
        pass
    
    def clear(self):
        os.system('cls')
