import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class Schedule:
    def __init__(self, iD, kelas, teacher, day, date, time, note):
        self.id = iD
        self._kelas = kelas
        self._teacher = teacher
        self._day = day
        self._date = date
        self._time = time
        self._note = note

    def getiD(self):
        return self.id

    def getKelas(self):
        return self._kelas

    def setKelas(self, value):
        self._kelas = value

    def getGuru(self):
        return self._teacher

    def setGuru(self, value):
        self._teacher = value

    def getHari(self):
        return self._day

    def setHari(self, value):
        self._day = value

    def getTanggal(self):
        return self._date

    def setTanggal(self, value):
        self._date = value

    def getWaktu(self):
        return self._time
        
    def setWaktu(self, value):
        self._time = value

    def getNote(self):
        return self._note

    def setNote(self, note):
        self._note = note
