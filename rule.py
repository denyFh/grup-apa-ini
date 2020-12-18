import sqlite3

databaseName = 'db_leslesan.db'
conn = sqlite3.connect(databaseName)
c = conn.cursor()


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

    # def lihatdata(self):
    #     guestID = ''
    #     cekMenu = ''
    #     if len(guestID) == 8 and cekMenu == "3":
    #         print("List Nama Teacher")
    #     elif len(guestID) == 8 and cekMenu == "2":
    #         print("List Nama Student")

    #     if len(guestID) == 5 and cekMenu == "3":
    #         print("List Nama Teacher")
    #     elif len(guestID) == 5 and cekMenu == "2":
    #         print("List Nama Student")


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

    def dataDiri(self):
        print("""
        Nama: {}
        Mata Pelajaran: {}
        Jenis Kelamin: {}
        Alamat: {}
        Nomor telepon: {}""")


class Student(Person):

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

    def dataDiri(self):
        data = []
        query = c.execute(
            "SELECT * FROM tab_students WHERE student_id=?", (Display.guestID,))
        query2 = c.execute(
            "SELECT nama tab_classes WHERE class_id=?", (query[2],))
        print("""
            ID: {query[0]}
            Nama: {query[1]}
            Kelas: {query2}
            Jenis Kelamin: {query[3]}
            Alamat: {query[4]}
            Nomor telepon: {query[5]}""")


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
    def __init__(self, iD, kelas, teacher, day, date, time, note):
        self._iD = iD
        self._kelas = kelas
        self._teacher = teacher
        self._day = day
        self._date = date
        self._time = time
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

class Display:
    guestID = None
    def __init__(self):
        pass

    def Home(self):
        
        check = []
        print("""
            
            \t------------------------HOME-----------------------
            \t------ketik (-quit) untuk membatalkan program------""")
        Display.guestID = input("\t\tMasukkan ID : ")
        query = c.execute(
            "SELECT * FROM tab_admins WHERE password=?", (Display.guestID,))
        for row in query:
            check.append(row)
            if len(check) > 0:
                Display.menuAdmin(self)
            else:
                check = []
                continue

        if Display.guestID == "-quit":
            Display.exit(self)
            exit()
        elif len(Display.guestID) == 8:
            query = c.execute(
                "SELECT * FROM tab_students WHERE student_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                Display.menuSiswa(self)
            else:
                print("\t\t-----ID tidak terdaftar, hubungi administrator-----")
                check = []
                Display.Home(self)
        elif len(Display.guestID) == 5:
            query = c.execute(
                "SELECT * FROM tab_teachers WHERE teacher_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                Display.menuGuru(self)
            else:
                print("\t\t-----ID tidak terdaftar, hubungi administrator-----")
                check = []
                Display.Home(self)
        else:
            print("\t\t-----ID tidak terdaftar, hubungi administrator-----")
            Display.Home(self)

    def menuSiswa(self):
        self.status = ["Siswa", Display.guestID]
        print("""
                -----------Selamat datang, {} {}-----------
                Silahkan pilih menu yang anda inginkan (1-3):
                1. Lihat Jadwal
                2. Lihat Data Diri
                3. Lihat Data Pengajar
                4. Logout
                ----------------------------------------------------""".format(self.status[0], self.status[1]))
        self.cekMenu = "0"
        while self.cekMenu != "4":
            self.cekMenu = input("\t\tMasukkan Menu : ")
            if self.cekMenu == '1':
                Student().lihatJadwal()
            elif self.cekMenu == '2':
                Student().dataDiri()
            # elif self.cekMenu == '3':
            #     Person().lihatdata()
            elif self.cekMenu == '4':
                Display.exit(self)
            else:
                print("Menu tidak tersedia")

    # def menuGuru(self):
    #     self.status = ["Guru", Display.guestID]
    #     print("""
    #             -----------Selamat datang, {} {}-----------
    #             Silahkan pilih menu yang anda inginkan (1-3):
    #             1. Lihat Jadwal
    #             2. Lihat Data Siswa
    #             3. Lihat Data Pengajar
    #             4. Logout
    #             ----------------------------------------------------""".format(self.status[0], self.status[1]))
    #     self.cekMenu = "0"
    #     while self.cekMenu != "4":
    #         self.cekMenu = input("\t\tMasukkan Menu : ")
    #         if self.cekMenu == '1':
    #             morphs.Teacher().lihatJadwal()
    #         elif self.cekMenu == '2':
    #             morphs.Person().lihatdata()
    #         elif self.cekMenu == '3':
    #             morphs.Person().lihatdata()
    #         elif self.cekMenu == '4':
    #             Display.exit(self)
    #         else:
    #             print("Menu tidak tersedia")

    # def menuAdmin(self):
    #     print("you are here")
    #     exit()

    def exit(self):
        print("""
            \t--------------------Terima Kasih-------------------""")
        conn.close()
        exit()


# a = Display().Home()
