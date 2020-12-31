import sqlite3
from User import User
from Student import Student
from Teacher import Teacher
from Admin import Admin
from Schedule import Schedule
from Classes import Classes
import os

DbName = 'db_leslesan.db'


class Display:
    def __init__(self, guestID=None):
        self.conn = sqlite3.connect(DbName)
        self.cursor = self.conn.cursor()
        self.guestID = guestID

    def clear(self):
        os.system('cls')

    @property
    def setguestID(self):
        pass

    @setguestID.setter
    def setguestID(self, value):
        self.guestID = value

    def Login(self):
        self.clear()
        global admin
        global siswa
        global guru
        global objek
        print("""=============================================
|||||||||| WELCOME TO TADIKA MESRA ||||||||||
=============================================
(ketik (-exit) untuk keluar dari program)
""")
        self.setguestID = input("Masukkan ID : ")
        if self.guestID.isdigit():
            self.guestID = int(self.guestID)

        data = []
        query = self.cursor.execute(
            "SELECT * FROM tab_admins WHERE password=?", (self.guestID,))
        for row in query:
            data.append(row)
        if len(data) > 0:
            admin = Admin(data[0][1], data[0][2], data[0][0])
            self.menuAdmin()
        else:
            if self.guestID == "-exit":
                self.exit()
            elif len(str(self.guestID)) == 8:
                query = self.cursor.execute(
                    "SELECT * FROM tab_students WHERE student_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    siswa = Student(
                        data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][0])
                    objek = User(data[0][1], data[0][3],
                                 data[0][4], data[0][5], data[0][0])
                    self.menuSiswa()
                else:
                    print("\nID tidak terdaftar, hubungi administrator")
                    input("(Press Enter to Continue...)\n")
                    self.Login()
            elif len(str(self.guestID)) == 5:
                query = self.cursor.execute(
                    "SELECT * FROM tab_teachers WHERE teacher_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    guru = Teacher(data[0][1], data[0][2], data[0]
                                   [3], data[0][4], data[0][5], data[0][0])
                    objek = User(data[0][1], data[0][3],
                                 data[0][4], data[0][5], data[0][0])
                    self.menuGuru()
                else:
                    print("\nID tidak terdaftar, hubungi administrator")
                    input("(Press Enter to Continue...)\n")
                    self.Login()
            else:
                print("\nID tidak terdaftar, hubungi administrator")
                input("(Press Enter to Continue...)\n")
                self.Login()

    def role(self, x):
        if type(x) == str:
            return "Admin"
        elif type(x) == int:
            if len(str(x)) == 8:
                return "Siswa"
            elif len(str(x)) == 5:
                return "Guru"

    def menuSiswa(self):
        self.clear()
        print(f"""Hello {siswa.getNama()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Lihat Data Diri
[2] Lihat Data Pengajar
[3] Lihat Jadwal
[4] Lihat Daftar Teman
=============================================""")
        self.cekMenu = "0"
        while self.cekMenu != "-1":
            self.cekMenu = input(
                "(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
            if self.cekMenu == "1":
                siswa.dataDiri()
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "2":
                objek.dataDiri()
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "3":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Semua Jadwal
[b] Lihat Jadwal Pribadi
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    objek.lihatJadwal()
                elif a == "b":
                    siswa.lihatJadwal()
                else:
                    print("\n============ Menu Tidak Tersedia ============\n")
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "4":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Daftar Teman Sekelas
[b] Lihat Daftar Semua Teman
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    siswa.lihatTeman()
                elif a == "b":
                    objek.lihatTeman()
                else:
                    print("\n============ Menu Tidak Tersedia ============\n")
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "-menu":
                self.menuSiswa()
            elif self.cekMenu == "-exit":
                self.exit()
            else:
                input(
                    "============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def menuGuru(self):
        self.clear()
        print(f"""Hello {guru.getNama()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Lihat Data Diri
[2] Lihat Data Siswa
[3] Lihat Jadwal
[4] Lihat Guru
=============================================""")
        self.cekMenu = "0"
        while self.cekMenu != "-1":
            self.cekMenu = input(
                "(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
            if self.cekMenu == "1":
                guru.dataDiri()
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "2":
                objek.lihatTeman()
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "3":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Semua Jadwal
[b] Lihat Jadwal Pribadi
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    objek.lihatJadwal()
                elif a == "b":
                    guru.lihatJadwal()
                    guru.editCatatan()
                else:
                    print("\n============ Menu Tidak Tersedia ============\n")
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "4":
                objek.dataDiri(self)
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "-menu":
                self.menuGuru()
            elif self.cekMenu == "-exit":
                self.exit()
            else:
                input(
                    "============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def menuAdmin(self):
        self.clear()
        global kelas
        print(f"""Hello {admin.getUsername()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Data Diri
[2] Data Kelas
[3] Data Guru
[4] Jadwal
=============================================
(ketik (-exit) untuk keluar dari program)""")
        self.cekMenu = input("Masukkan Menu : ")
        while self.cekMenu != "-exit":
            if self.cekMenu == "1":
                self.clear()
                print(admin.detail())
                a = input("Edit data diri? (ketik 'y' jika iya) ")
                if a == "y":
                    self.clear()
                    print(admin.editDataDiri())
                else:
                    pass
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "2":
                self.clear()
                print(admin.mengelolaKelas())
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "3":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Guru
[b] Tambah Guru
[c] Hapus Guru
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    User.dataDiri(self)
                    input("(Press Enter to Continue...)\n")
                elif a == "b":
                    nama = input("Masukkan nama >> ")
                    mapel = input("Masukkan mata pelajaran >> ")
                    jk = input(
                        "Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
                    if jk == "l":
                        jk = "Laki-Laki"
                    elif jk == "p":
                        jk = "Perempuan"
                    else:
                        jk = "unset"
                    alamat = input("Masukkan alamat >> ")
                    nohp = input("Masukkan nomor hp >> ")
                    guru = Teacher(nama, jk, mapel, alamat,
                                   nohp, 1)  # <-thisone
                    tempo = self.cursor.execute(
                        "select * from tab_teachers where PHONE = ?", (guru.getPhone(),))
                    if tempo.fetchone() is None:
                        self.cursor.execute("insert into tab_teachers (NAMA, JENIS_KELAMIN, MAPEL, ALAMAT, PHONE) values (?,?,?,?,?)", (
                            guru.getNama(), guru.getGender(), guru.getMapel(), guru.getAlamat(), guru.getPhone()))
                        self.conn.commit()
                        print(">> Guru berhasil didaftarkan")
                    else:
                        print(">> Guru sudah terdaftar")
                elif a == "c":
                    User.dataDiri(self)
                    admin.hapusGuru()
                else:
                    print("Menu tidak tersedia")
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "4":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Jadwal
[b] Tambah Jadwal
[c] Hapus Jadwal
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    User.lihatJadwal(self)
                    input("(Press Enter to Continue...)\n")
                elif a == "b":
                    klaslist = []
                    gurulist = []
                    sql1 = self.cursor.execute(
                        "select class_id from tab_classes")
                    for i in sql1:
                        klaslist.append(i)
                    res1 = str(klaslist)[1:-1]
                    print(f"List kelas tersedia: {res1}")
                    sql2 = self.cursor.execute(
                        "select teacher_id from tab_teachers")
                    for i in sql2:
                        gurulist.append(i)
                    res2 = str(gurulist)[1:-1]
                    print(f"List guru tersedia: {res2}")
                    klasid = int(input("Masukkan id kelas >> "))
                    guruid = int(input("Masukkan id guru >> "))
                    hari = input("Masukkan hari >> ").upper()
                    tg = input("Masukkan tanggal (DD) >> ")
                    bln = input("Masukkan bulan (MM) >> ")
                    thn = input("Masukkan tahun (YYYY) >> ")
                    tanggal = "{}/{}/{}".format(tg, bln, thn)
                    waktumulai = input(
                        "Masukkan waktu mulai dengan format jam 24.00 >> ")
                    waktuakhir = input(
                        "Masukkan waktu selesai dengan format jam 24.00 >> ")
                    waktu = "{} s/d {}".format(waktumulai, waktuakhir)
                    jadwal = Schedule(1, klasid, guruid,
                                      hari, tanggal, waktu, 1)  # <-Thisone
                    tempor = self.cursor.execute(
                        "select * from tab_schedules where DATE = ? AND TIME = ?", (jadwal.getTanggal(), jadwal.getWaktu(),))
                    if tempor.fetchone() is None:
                        self.cursor.execute("insert into tab_schedules (class_id, teacher_id, DAY, DATE, TIME) values (?,?,?,?,?)", (
                            jadwal.getKelas(), jadwal.getGuru(), jadwal.getHari(), jadwal.getTanggal(), jadwal.getWaktu()))
                        self.conn.commit()
                        print(">> Jadwal berhasil ditambahkan")
                    else:
                        print(">> Jadwal crash, silahkan tambahkan ulang")
                elif a == "c":
                    User.lihatJadwal(self)
                    admin.hapusJadwal()
#                 else:
#                     print("\n============ Menu Tidak Tersedia ============\n")
#                 input("(Press Enter to Continue...)\n")
#             elif self.cekMenu == "4":
#                 User.dataDiri(self)
#                 input("(Press Enter to Continue...)\n")
                else:
                    print("Menu tidak tersedia")
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            else:
                input(
                    "============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")
        else:
            self.exit()

    def exit(self):
        print("""
============= SEE YOU NEXT TIME =============
""")
        self.conn.close()
        exit()


start = Display()
start.Login()
