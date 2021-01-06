import sqlite3
from abc import ABC, abstractmethod
import os
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

#class untuk user atau pengguna, merupakan class induk dalam inheritence dengan peranakan / turunan student dan teacher
class User(ABC):
    #inisialisasi class object
    def __init__(self, nama, gender, alamat, phone, iD):
        self._nama = nama
        self._gender = gender
        self._alamat = alamat
        self._phone = phone
        self.id = iD

    #mengambil atribut nama
    def getNama(self):
        return self._nama
    
    #mengubah atau memberi atribut nama
    def setNama(self, nama):
        self._nama = nama

    #mengambil atribut gender
    def getGender(self):
        return self._gender

    #mengubah atau memberi atribut gender
    def setGender(self,gender):
        self._gender = gender

    #mengambil atribut alamat
    def getAlamat(self):
        return self._alamat

    #mengubah atau memberi atribut alamat
    def setAlamat(self, alamat):
        self._alamat = alamat

    #mengambil atribut nomor telpon
    def getPhone(self):
        return self._phone

    #mengubah atau memberi atribut nomor telpon
    def setPhone(self, phone):
        self._phone = phone

    #metode abstrak yang tidak bisa diubah dan diturunkan ke peranakan/subclassnya
    @abstractmethod
    def dataDiri(self):
        pass
    
    #metode abstrak yang tidak bisa diubah dan diturunkan ke peranakan/subclassnya
    @abstractmethod
    def lihatJadwal(self):
        pass
    
    #memebersihkan console window
    def clear(self):
        os.system('cls')
