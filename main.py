import sqlite3
from Person import Person
from Student import Student
from Teacher import Teacher
from Admin import Admin
from Schedule import Schedule
from Classes import Classes

DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

class Display:
    guestID = None

    def __init__(self):
        pass

    def Home(self):
        global admin
        global siswa
        global guru
        global objek
        check = []
        print("""
=============================================
|||||||||| WELCOME TO TADIKA MESRA ||||||||||
=============================================
(ketik (-exit) untuk keluar dari program)
""")
        Display.guestID = input("Masukkan ID : ")
        if Display.guestID.isdigit():
            Display.guestID = int(Display.guestID)

        query = cursor.execute(
            "SELECT * FROM tab_admins WHERE password=?", (Display.guestID,))
        for row in query:
            check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                admin = Admin(row[1], row[2], Display.guestID)
                print(
                    "\n- Selamat datang, {} ({}) -".format(self.status[1], self.status[0]))
                Display.menuAdmin(self)
            else:
                check = []
                continue

        if Display.guestID == "-exit":
            Display.exit(self)
            exit()
        elif len(str(Display.guestID)) == 8:
            query = cursor.execute(
                "SELECT * FROM tab_students WHERE student_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                siswa = Student(row[1], row[2], row[3], row[4], row[5], Display.guestID)
                objek = Person(row[1], row[3], row[4], row[5], Display.guestID)
                print(
                    "\n- Selamat datang, {} ({}) -".format(self.status[1], self.status[0]))
                Display.menuSiswa(self)
            else:
                print("\nID tidak terdaftar, hubungi administrator")
                input("(Press Enter to Continue...)\n")
                check = []
                Display.Home(self)
        elif len(str(Display.guestID)) == 5:
            query = cursor.execute(
                "SELECT * FROM tab_teachers WHERE teacher_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                guru = Teacher(row[1], row[2], row[3], row[4],row[5], Display.guestID)
                objek = Person(row[1], row[3], row[4], row[5], Display.guestID)
                print(
                    "\n- Selamat datang, {} ({}) -".format(self.status[1], self.status[0]))
                Display.menuGuru(self)
            else:
                check = []
                print("\nID tidak terdaftar, hubungi administrator")
                input("(Press Enter to Continue...)\n")
                Display.Home(self)
        else:
            print("\nID tidak terdaftar, hubungi administrator")
            input("(Press Enter to Continue...)\n")
            Display.Home(self)

    def role(self, x):
        if type(x) == str:
            return "Admin"
        elif type(x) == int:
            if len(str(x)) == 8:
                return "Siswa"
            elif len(str(x)) == 5:
                return "Guru"

    def menuSiswa(self):
        print("""
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
            self.cekMenu = input("(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
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
                Display.menuSiswa(self)
            elif self.cekMenu == "-exit":
                Display.exit(self)
            else:
                input("============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def menuGuru(self):
        print("""
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
            self.cekMenu = input("(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
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
                        cursor.execute("UPDATE tab_schedules set NOTE = ? WHERE id = ?", (note, jadwal))
                        if jadwal in Teacher.daftarid:
                            conn.commit()
                        else:
                            print(">> Hubungi guru yang bertugas untuk memberikan catatan")
                    else:
                        continue
                else:
                    print("\n============ Menu Tidak Tersedia ============\n")
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "4":
                objek.dataDiri(self)
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "-menu":
                Display.menuGuru(self)
            elif self.cekMenu == "-exit":
                Display.exit(self)
            else:
                input("============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def menuAdmin(self):
        global kelas
        print("""
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
            self.cekMenu = input("(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
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
                        if password == Display.guestID:
                            username = input("Masukkan username: ")
                            tempo = cursor.execute("select * from tab_admins where username = ?", (username,))
                            if tempo.fetchone() is None:
                                admin.setUsername(username)
                                cursor.execute("UPDATE tab_admins set USERNAME = ? WHERE password = ?", (admin.getUsername(), admin.getPassword()))
                                conn.commit()
                            else:
                                print("Username sudah digunakan, silahkan gunakan username lain")
                        else: 
                            print("Password salah, kembali ke menu utama")
                    elif b == "b":
                        password = input("Masukkan password lama: ")
                        if password == Display.guestID:
                            newpassword = input("Masukkan password baru: ")
                            tempo = cursor.execute("select * from tab_admins where password = ?", (newpassword,))
                            if tempo.fetchone is None:
                                admin.setPassword(newpassword)
                                print("Password berhasil diganti, silahkan login kembali untuk melanjutkan kegiatan")
                                cursor.execute("UPDATE tab_admins set password = ? WHERE password = ?", (admin.getPassword(), password))
                                conn.commit()   
                                Display.exit(self)   
                            else:
                                print("Password sudah digunakan, silahkan gunakan password lain")
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
                    query = cursor.execute("SELECT * FROM tab_classes")
                    for row in query:
                        print(f"""[{row[0]}] {row[1]}""")
                        kelas.append(row[1])
                    getdetail = input("Masukkan nama kelas untuk melihat detail >> ")
                    sql = cursor.execute("SELECT * FROM tab_classes WHERE NAMA = ?", (getdetail,))
                    for row in sql:
                        idkelas = row[0]
                    if getdetail in kelas:
                        query = cursor.execute("SELECT * FROM tab_students WHERE kelas = ?", (idkelas,))
                        for row in query:
                            print(f"""
ID: {row[0]}
Nama: {row[1]}
Jenis Kelamin: {row[3]}
Alamat: {row[4]}
No.HP: {row[5]}
""")
                    else:
                        print("Kelas tidak terdaftar")
                elif a == "b":
                    nama = input("Masukkan nama kelas >> ")
                    kelas = Classes(nama)
                    tempo = cursor.execute("select * from tab_classes where nama = ?", (kelas.getClassName(),))
                    if tempo.fetchone() is None:
                        cursor.execute("insert into tab_classes (nama) values (?)", (kelas.getClassName()))
                        conn.commit()
                        print("Kelas berhasil ditambahkan")
                    else:
                        print("Nama kelas sudah terdaftar")
                elif a == "c":
                    nama =  input("Masukkan nama >> ")
                    getkelas = input("Masukkan nama kelas >> ")
                    jk = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
                    if jk == "l":
                        jk = "Laki-Laki"
                    elif jk == "p":
                        jk = "Perempuan"
                    else: 
                        jk = "unset"
                    alamat = input("Masukkan alamat >> ")
                    nohp =  input("Masukkan nomor hp >> ")
                    sql = cursor.execute("SELECT * FROM tab_classes WHERE NAMA = ?", (getkelas,))
                    for row in sql:
                        idkelas = int(row[0])
                    siswa = Student(nama, idkelas, jk, alamat, nohp, 1)
                    tempo = cursor.execute("select * from tab_students where PHONE = ?", (siswa.getPhone(),))
                    if tempo.fetchone() is None:
                        cursor.execute("insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)", (siswa.getNama(), siswa.getKelas(), siswa.getGender(), siswa.getAlamat(), siswa.getPhone()))
                        conn.commit()
                        print("Siswa berhasil didaftarkan")
                    else:
                        print("Siswa sudah terdaftar")
                else:
                    print("Menu tidak tersedia")                 
#                 Teacher.dataDiri(self)
#                 Person.lihatTeman(self)
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
                    Person.dataDiri(self)
                    input("(Press Enter to Continue...)\n")
                elif a == "b":
                    nama =  input("Masukkan nama >> ")
                    mapel = input("Masukkan mata pelajaran >> ")
                    jk = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
                    if jk == "l":
                        jk = "Laki-Laki"
                    elif jk == "p":
                        jk = "Perempuan"
                    else: 
                        jk = "unset"
                    alamat = input("Masukkan alamat >> ")
                    nohp =  input("Masukkan nomor hp >> ")
                    # sql = cursor.execute("SELECT * FROM tab_classes WHERE NAMA = ?", (getkelas,))
                    # for row in sql:
                    #     idkelas = int(row[0])
                    guru = Teacher(nama, jk, mapel, alamat, nohp, 1)
                    tempo = cursor.execute("select * from tab_teachers where PHONE = ?", (guru.getPhone(),))
                    if tempo.fetchone() is None:
                        cursor.execute("insert into tab_teachers (NAMA, JENIS_KELAMIN, MAPEL, ALAMAT, PHONE) values (?,?,?,?,?)", (guru.getNama(), guru.getGender(), guru.getMapel(), guru.getAlamat(), guru.getPhone()))
                        conn.commit()
                        print("Guru berhasil didaftarkan")
                    else:
                        print("Guru sudah terdaftar")
                elif a == "c":
                    Person.dataDiri(self)
                    d = input("ingin menghapus data? ketik 'y' jika iya ")
                    if d == "y":
                        inpId = input("Masukkan id guru yang ingin dihapus ")
                        temp = cursor.execute("select * from tab_teachers where teacher_id = ?", (inpId,))
                        if temp.fetchone() is None:
                            print("Guru tidak ada")
                        else:
                            cursor.execute("delete from tab_teachers where teacher_id = ?", (inpId,))
                            conn.commit()
                            print("Guru telah dihapus")
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
[d] Edit Jadwal
=============================================
Masukkan pilihan >> """)
                if a == "a":
                    Person.lihatJadwal(self)
                    input("(Press Enter to Continue...)\n")    
#                 else:
#                     print("\n============ Menu Tidak Tersedia ============\n")
#                 input("(Press Enter to Continue...)\n")
#             elif self.cekMenu == "4":
#                 Person.dataDiri(self)
#                 input("(Press Enter to Continue...)\n")
                else:
                    print("Menu tidak tersedia")
            elif self.cekMenu == "-menu":
                Display.menuAdmin(self)
            elif self.cekMenu == "-exit":
                Display.exit(self)
            else:
                input("============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def exit(self):
        print("""
============= SEE YOU NEXT TIME =============
""")
        conn.close()
        exit()


Display().Home()
