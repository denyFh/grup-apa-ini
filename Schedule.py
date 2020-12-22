from connector import Connect


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

    def getGuru(self):
        return self._teacher

    def getHari(self):
        return self._day

    def getTanggal(self):
        return self._date

    def getWaktu(self):
        return self._time

    def getNote(self):
        return self._note

    def setNote(self, note):
        self._note = note

