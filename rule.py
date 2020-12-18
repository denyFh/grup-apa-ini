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
    @classmethod
    def dataDiri(self):
        if len(Display.guestID) == 5:
            query = c.execute('''\
                SELECT tab_teachers.teacher_id, tab_teacher.nama, tab_teacher.mapel, tab_teachers.jenis_kelamin
                WHERE tab_students.student_id = ?''', (Display.guestID,))
            for row in query:
                print(f"""
                    ID: {row[0]}
                    Nama: {row[1]}
                    Mata Pelajaran: {row[2]}
                    Jenis Kelamin: {row[3]}""")          
        elif len(Display.guestID) == 8:
                    query = c.execute('''\
            SELECT tab_students.student_id, tab_students.nama, tab_classes.nama, tab_students.jenis_kelamin
            FROM tab_students
            INNER JOIN tab_classes
            ON tab_students.kelas = tab_classes.class_id
            WHERE tab_students.student_id = ?''', (Display.guestID,))
        for row in query:
            print(f"""
                ID: {row[0]}
                Nama: {row[1]}
                Kelas: {row[2]}
                Jenis Kelamin: {row[3]}""")
    
    def lihatJadwal(self):
        query = c.execute("""
        SELECT tab_teachers.NAMA, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        """)

        for row in query:
            print(f"""
                Pengajar: {row[0]}
                Kelas: {row[1]}
                Waktu: {row[2]}, {row[3]}, {row[4]}
                Note: {row[5]}
            """)


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

    @classmethod
    def dataDiri(self):
        query = c.execute('''\
            SELECT tab_teachers.teacher_id, tab_teacher.nama, tab_teacher.mapel, tab_teacher.jenis_kelamin, tab_teacher.alamat, tab_teacher.phone
            WHERE tab_students.student_id = ?''', (Display.guestID,))
        for row in query:
            print(f"""
                ID: {row[0]}
                Nama: {row[1]}
                Mata Pelajaran: {row[2]}
                Jenis Kelamin: {row[3]}
                Alamat: {row[4]}
                Nomor telepon: {row[5]}""")


class Student(Person):

    def __init__(self, nama, gender, alamat, phone, kelas):
        super().__init__(nama, gender, alamat, phone)
        self._kelas = kelas

    def getKelas(self):
        return self._kelas

    def lihatJadwal(self):
        query0 = c.execute(
            """SELECT KELAS from tab_students
            WHERE student_id = ?""", (Display.guestID,))

        for row in query0:
            kelas = row[0]

        query = c.execute("""
        SELECT tab_teachers.NAMA, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        WHERE tab_classes.class_id = ?""", (kelas,))

        for row in query:
            print(f"""
                Pengajar: {row[0]}
                Kelas: {row[1]}
                Waktu: {row[2]}, {row[3]}, {row[4]}
                Note: {row[5]}
            """)

    @classmethod
    def dataDiri(self):
        query = c.execute('''\
            SELECT tab_students.student_id, tab_students.nama, tab_classes.nama, tab_students.jenis_kelamin, tab_students.alamat, tab_students.phone
            FROM tab_students
            INNER JOIN tab_classes
            ON tab_students.kelas = tab_classes.class_id
            WHERE tab_students.student_id = ?''', (Display.guestID,))
        for row in query:
            print(f"""
                ID: {row[0]}
                Nama: {row[1]}
                Kelas: {row[2]}
                Jenis Kelamin: {row[3]}
                Alamat: {row[4]}
                Nomor telepon: {row[5]}""")


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
                Silahkan pilih menu yang anda inginkan (1-4):
                1. Lihat Jadwal
                2. Lihat Data Diri
                3. Lihat Data Pengajar
                4. Lihat Jadwal Pribadi
                5. Logout
                ----------------------------------------------------""".format(self.status[0], self.status[1]))
        self.cekMenu = "0"
        while self.cekMenu != "5":
            self.cekMenu = input("\t\tMasukkan Menu : ")
            if self.cekMenu == '1':
                Person.lihatJadwal(self)
            elif self.cekMenu == '2':
                Student.dataDiri()
            # elif self.cekMenu == '3':
            #     Person().lihatdata()
            elif self.cekMenu == '4':
                Student.lihatJadwal(self)
            elif self.cekMenu == '5':
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
    #     print("coming soon")
    #     exit()

    def exit(self):
        print("""
            \t--------------------Terima Kasih-------------------""")
        conn.close()
        exit()


a = Display().Home()
