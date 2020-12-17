import sqlite3
import main as mn

databaseName = 'db_leslesan.db'
conn = sqlite3.connect(databaseName)


class Person:
    def __init__(self, nama, gender, alamat, phone):
        self._nama = nama
        self._gender = gender
        self._alamat = alamat
        self._phone = phone

    def getNama(self):
        return self._nama

    def getGender(self):
        return self._gender

    def getAlamat(self):
        return self._alamat

    def getPhone(self):
        return self._phone

    def setAlamat(self, alamat):
        self._alamat = alamat

    def setPhone(self, phone):
        self._phone = phone

    def lihatdata(self):
        guestID = ''
        cekMenu = ''
        if len(guestID) == 8 and cekMenu == "3":
            print("List Nama Teacher")
        elif len(guestID) == 8 and cekMenu == "2":
            print("List Nama Student")

        if len(guestID) == 5 and cekMenu == "3":
            print("List Nama Teacher")
        elif len(guestID) == 5 and cekMenu == "2":
            print("List Nama Student")

    # def lihatJadwalFree(self):


class Teacher(Person):
    def __init__(self, nama, gender, alamat, phone, mapel):
        super().__init__(nama, gender, alamat, phone)
        self._mapel = mapel

    def getMapel(self):
        return self._mapel

    def lihatJadwal(self):
        print("""
        -----------Jadwal Mengajar----------
        |    Kelas    |    Jam Mengajar    |
        |{}           |{}                  |
        """.format(Schedule.getKelas, Schedule.getWaktu))


class Student(Person):
    check = mn.Display.guestID

    def __init__(self, nama, gender, alamat, phone, kelas):
        super().__init__(nama, gender, alamat, phone)
        self._kelas = kelas

    def getKelas(self):
        return self._kelas

    def lihatJadwal(self):
        print("""
        ----------------------Jadwal Pelajaran---------------------
        |   Pengajar   |    Kelas    |            Waktu           |
        |{}            |{}           |{}, {}, {}                  |
        """.format(self.getNama, Schedule.getKelas, Schedule.getHari, Schedule.getTanggal, Schedule.getWaktu))


class Classes:
    def __init__(self, classname):
        self._classname = classname

    def getClassName(self):
        return self._classname


class Admin:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password


class Schedule:
    def __init__(self, iD, kelas, teacher, day, time, date, note):
        self._iD = iD
        self._kelas = kelas
        self._teacher = teacher
        self._day = day
        self._time = time
        self._date = date
        self._note = note

    def getiD(self):
        return self._iD

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
