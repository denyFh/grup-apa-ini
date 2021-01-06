import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

#class jadwal les
class Schedule:
    #inisialisasi class object, berisi atribut jadwal
    def __init__(self, iD, kelas, teacher, day, date, time, note):
        self.id = iD
        self._kelas = kelas
        self._teacher = teacher
        self._day = day
        self._date = date
        self._time = time
        self._note = note

    #mengambil atribut id
    def getiD(self):
        return self.id

    #mengambil atribut kelas
    def getKelas(self):
        return self._kelas

    #merubah atau menambahkan atribut kelas
    def setKelas(self, value):
        self._kelas = value

    #mengambil atribut guru
    def getGuru(self):
        return self._teacher

    #merubah atau menambahkan atribut guru
    def setGuru(self, value):
        self._teacher = value

    #mengambil atribut hari
    def getHari(self):
        return self._day

    #merubah atau menambahkan atribut hari
    def setHari(self, value):
        self._day = value

    #mengambil atribut tanggal
    def getTanggal(self):
        return self._date

    #merubah atau menambahkan atribut tanggal
    def setTanggal(self, value):
        self._date = value

    #mengambil atribut waktu
    def getWaktu(self):
        return self._time
    
    #merubah atau menambahkan atribut waktu
    def setWaktu(self, value):
        self._time = value

    #mengambil atribut note
    def getNote(self):
        return self._note

    #merubah atau menambahkan atribut note
    def setNote(self, note):
        self._note = note
