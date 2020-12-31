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
        query = self.cursor.execute("SELECT * FROM tab_admins WHERE password=?", (self.guestID,))
        for row in query:
            data.append(row)
        if len(data) > 0:
            admin = Admin(data[0][1], data[0][2], data[0][0])
            self.menuAdmin()
        else:
            if self.guestID == "-exit":
                self.exit()
            elif len(str(self.guestID)) == 8:
                query = self.cursor.execute("SELECT * FROM tab_students WHERE student_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    # self.status = [self.role(self.guestID), data[0][1]]
                    siswa = Student(data[0][1], data[0][2], data[0][3],data[0][4], data[0][5], data[0][0])
                    objek = User(data[0][1], data[0][3], data[0][4], data[0][5], data[0][0])
                    # print(
                    #     "\n- Selamat datang, {} ({}) -".format(self.status[1], self.status[0]))
                    self.menuSiswa()
                else:
                    print("\nID tidak terdaftar, hubungi administrator")
                    input("(Press Enter to Continue...)\n")
                    self.Login()
            elif len(str(self.guestID)) == 5:
                query = self.cursor.execute("SELECT * FROM tab_teachers WHERE teacher_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    guru = Teacher(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][0])
                    objek = User(data[0][1], data[0][3], data[0][4], data[0][5], data[0][0])
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
                    a = input("Edit catatan? (ketik 'y' jika iya) ")
                    if a == "y":
                        jadwal = input("Masukkan ID Jadwal: ")
                        note = input("Masukkan catatan: ")
                        self.cursor.execute(
                            "UPDATE tab_schedules set NOTE = ? WHERE id = ?", (note, jadwal))
                        if jadwal in Teacher.daftarid:
                            self.conn.commit()
                        else:
                            print(
                                ">> Hubungi guru yang bertugas untuk memberikan catatan")
                    else:
                        continue
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
=============================================""")
        self.cekMenu = "0"
        while self.cekMenu != "-1":
            self.cekMenu = input(
                "(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
            if self.cekMenu == "1":
                print(admin.detail())
                a = input("Edit data diri? (ketik 'y' jika iya) ")
                if a == "y":
                    b = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Edit username
[b] Edit password
=============================================
Masukkan pilihan >> """)
                    if b == "a":
                        password = input("Masukkan password: ")
                        if password == self.guestID:
                            username = input("Masukkan username: ")
                            tempo = self.cursor.execute(
                                "select * from tab_admins where username = ?", (username,))
                            if tempo.fetchone() is None:
                                admin.setUsername(username)
                                self.cursor.execute("UPDATE tab_admins set USERNAME = ? WHERE password = ?", (
                                    admin.getUsername(), admin.getPassword()))
                                self.conn.commit()
                            else:
                                print(
                                    "Username sudah digunakan, silahkan gunakan username lain")
                        else:
                            print("Password salah, kembali ke menu utama")
                    elif b == "b":
                        password = input("Masukkan password lama: ")
                        if password == self.guestID:
                            newpassword = input("Masukkan password baru: ")
                            tempo = self.cursor.execute(
                                "select * from tab_admins where password = ?", (newpassword,))
                            if tempo.fetchone is None:
                                admin.setPassword(newpassword)
                                print(
                                    "Password berhasil diganti, silahkan login kembali untuk melanjutkan kegiatan")
                                self.cursor.execute(
                                    "UPDATE tab_admins set password = ? WHERE password = ?", (admin.getPassword(), password))
                                self.conn.commit()
                                self.exit()
                            else:
                                print(
                                    "Password sudah digunakan, silahkan gunakan password lain")
                        else:
                            print("Password salah,  kembali ke menu utama")
                    else:
                        print("Password salah,  kembali ke menu utama")
                else:
                    continue
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "2":
                a = input("""
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Kelas
[b] Tambahkan Kelas
[c] Tambahkan Siswa
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    kelas = []
                    query = self.cursor.execute("SELECT * FROM tab_classes")
                    for row in query:
                        print(f"""[{row[0]}] {row[1]}""")
                        kelas.append(row[1])
                    getdetail = input(
                        "Masukkan nama kelas untuk melihat detail >> ")
                    sql = self.cursor.execute(
                        "SELECT * FROM tab_classes WHERE NAMA = ?", (getdetail,))
                    for row in sql:
                        idkelas = row[0]
                    if getdetail in kelas:
                        query = self.cursor.execute(
                            "SELECT * FROM tab_students WHERE kelas = ?", (idkelas,))
                        for row in query:
                            print(f"""
ID: {row[0]}
Nama: {row[1]}
Jenis Kelamin: {row[3]}
Alamat: {row[4]}
No.HP: {row[5]}
""")
                    else:
                        print(">> Kelas tidak terdaftar")
                elif a == "b":
                    nama = input("Masukkan nama kelas >> ")
                    kelas = Classes(nama)
                    tempo = self.cursor.execute(
                        "select * from tab_classes where nama = ?", (kelas.getClassName(),))
                    if tempo.fetchone() is None:
                        self.cursor.execute(
                            "insert into tab_classes (nama) values (?)", (kelas.getClassName()))
                        self.conn.commit()
                        print(">> Kelas berhasil ditambahkan")
                    else:
                        print(">> Nama kelas sudah terdaftar")
                elif a == "c":
                    nama = input("Masukkan nama >> ")
                    getkelas = input("Masukkan nama kelas >> ")
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
                    sql = self.cursor.execute(
                        "SELECT * FROM tab_classes WHERE NAMA = ?", (getkelas,))
                    for row in sql:
                        idkelas = int(row[0])
                    siswa = Student(nama, idkelas, jk, alamat, nohp, 1)
                    tempo = self.cursor.execute(
                        "select * from tab_students where PHONE = ?", (siswa.getPhone(),))
                    if tempo.fetchone() is None:
                        self.cursor.execute("insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)", (
                            siswa.getNama(), siswa.getKelas(), siswa.getGender(), siswa.getAlamat(), siswa.getPhone()))
                        self.conn.commit()
                        print(">> Siswa berhasil didaftarkan")
                    else:
                        print(">> Siswa sudah terdaftar")
                else:
                    print("Menu tidak tersedia")
#                 Teacher.dataDiri(self)
#                 User.lihatTeman(self)
#                 input("(Press Enter to Continue...)\n")
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
                    # sql = self.cursor.execute("SELECT * FROM tab_classes WHERE NAMA = ?", (getkelas,))
                    # for row in sql:
                    #     idkelas = int(row[0])
                    guru = Teacher(nama, jk, mapel, alamat, nohp, 1)
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
                    d = input("ingin menghapus data? ketik 'y' jika iya ")
                    if d == "y":
                        inpId = input("Masukkan id guru yang ingin dihapus ")
                        temp = self.cursor.execute(
                            "select * from tab_teachers where teacher_id = ?", (inpId,))
                        if temp.fetchone() is None:
                            print(">> Guru tidak ada")
                        else:
                            self.cursor.execute(
                                "delete from tab_teachers where teacher_id = ?", (inpId,))
                            self.conn.commit()
                            print(">> Guru telah dihapus")
                    else:
                        continue
                else:
                    print("Menu tidak tersedia")
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
                                      hari, tanggal, waktu, 1)
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
                    e = input("Ingin menghapus jadwal? ketik 'y' jika iya ")
                    if e == "y":
                        f = input("Pada Hari apa jadwal tersebut? >> ").upper()
                        temp = self.cursor.execute(
                            "select * from tab_schedules where DAY = ?", (f,))
                        if temp.fetchone() is None:
                            print(">> Jadwal tidak ada")
                        else:
                            tempf = self.cursor.execute(
                                "select * from tab_schedules where DAY = ?", (f,))
                            for row in tempf:
                                print(f"""
            ID Jadwal : {row[0]}
            ID Kelas : {row[1]}
            ID Guru : {row[2]}
            Hari : {row[3]}
            Tanggal : {row[4]}
            Waktu : {row[5]}
            Catatan : {row[6]}
                                """)
                            jid = input(
                                "Masukkan ID Jadwal yang ingin dihapus >> ")
                            tempjid = self.cursor.execute(
                                "select * from tab_schedules where id = ?", (jid,))
                            if tempjid.fetchone() is None:
                                print(">> ID Jadwal tidak ditemukan")
                            else:
                                self.cursor.execute(
                                    "delete from tab_schedules where id = ?", (jid,))
                                self.conn.commit()
                                print(">> Jadwal telah dihapus")
                    else:
                        continue
#                 else:
#                     print("\n============ Menu Tidak Tersedia ============\n")
#                 input("(Press Enter to Continue...)\n")
#             elif self.cekMenu == "4":
#                 User.dataDiri(self)
#                 input("(Press Enter to Continue...)\n")
                else:
                    print("Menu tidak tersedia")
            elif self.cekMenu == "-menu":
                self.menuAdmin()
            elif self.cekMenu == "-exit":
                self.exit()
            else:
                input(
                    "============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def exit(self):
        print("""
============= SEE YOU NEXT TIME =============
""")
        self.conn.close()
        exit()


start = Display()
start.Login()
