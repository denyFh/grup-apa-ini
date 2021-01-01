import sqlite3
import os
from Schedule import Schedule
from Classes import Classes
from Student import Student
from Teacher import Teacher
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class Admin:
    def __init__(self, username, password, iD):
        self.__username = username
        self.__password = password
        self.id = iD

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def setUsername(self, value):
        self.__username = value

    def setPassword(self, value):
        self.__password = value

    def detail(self):
        password = len(self.getPassword())*"*"
        return (f"""=============================================
                 DATA DIRI                   
=============================================
Username = {self.getUsername()}
Password = {password}
""")

    def editUsername(self):
        self.editusername = input("Masukkan username: ")
        self.tempo = cursor.execute(
            "select * from tab_admins where username = ?", (self.editusername,))
        if self.tempo.fetchone() is None:
            self.setUsername(self.editusername)
            cursor.execute("UPDATE tab_admins set USERNAME = ? WHERE password = ?", (
                self.getUsername(), self.getPassword()))
            conn.commit()
            return("Username berhasil diubah!")
        else:
            return("Username sudah digunakan, silahkan gunakan username lain")

    def editPassword(self):
        self.newpassword = input("Masukkan password baru: ")
        self.tempo = cursor.execute(
            "select * from tab_admins where password = ?", (self.newpassword,))
        if self.tempo.fetchone() is None:
            self.setPassword(self.newpassword)
            cursor.execute("UPDATE tab_admins set password = ? WHERE username = ?",
                           (self.getPassword(), self.getUsername()))
            conn.commit()
            return("Password berhasil diganti, silahkan login kembali untuk melanjutkan kegiatan")
        else:
            return("Password sudah digunakan, silahkan gunakan password lain")

    def editDataDiri(self):
        self.pilihan = input("""=============================================
               EDIT DATA DIRI                
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Edit username
[b] Edit password
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            self.password = input("Masukkan password: ")
            if self.password == self.__password:
                return (self.editUsername())
            else:
                return("Password salah, kembali ke menu utama")
        elif self.pilihan == "b":
            self.password = input("Masukkan password lama: ")
            if self.password == self.__password:
                return (self.editPassword())
            else:
                return("Password salah,  kembali ke menu utama")
        else:
            return("============ Menu Tidak Tersedia ============")

    def lihatKelas(self):
        self.kelas = []
        self.query = cursor.execute("SELECT * FROM tab_classes")
        print("""=============================================
                DAFTAR KELAS                 
=============================================""")
        for row in self.query:
            print(f"""[{row[0]}] {row[1]}""")
            self.kelas.append(row[1])
        self.getdetail = (input(
            "Masukkan nama kelas untuk melihat daftar siswa >> ")).upper()
        self.clear()
        self.query = cursor.execute(
            "SELECT * FROM tab_classes WHERE NAMA = ?", (self.getdetail,))
        print(f"""=============================================
             DAFTAR SISWA KELAS {self.getdetail}            
=============================================""")
        for row in self.query:
            self.idkelas = row[0]
        if self.getdetail in self.kelas:
            self.query = cursor.execute(
                "SELECT * FROM tab_students WHERE kelas = ?", (self.idkelas,))
            for row in self.query:
                print(f"""
ID: {row[0]}
Nama: {row[1]}
Jenis Kelamin: {row[3]}
Alamat: {row[4]}
No.HP: {row[5]}""")
            return("\nFinish!")
        else:
            return(">> Kelas tidak terdaftar")

    def tambahKelas(self):
        kelas = Classes(input("Masukkan nama kelas >> "))
        self.tempo = cursor.execute(
            "select * from tab_classes where nama = ?", (kelas.getClassName(),))
        if self.tempo.fetchone() is None:
            cursor.execute(
                "insert into tab_classes (nama) values (?)", (kelas.getClassName()))
            conn.commit()
            return (">> Kelas berhasil ditambahkan")
        else:
            return (">> Nama kelas sudah terdaftar")

    def editKelas(self):
        kelasid = input("Masukkan id kelas >> ")
        nama = input("Masukkan nama kelas baru >> ")
        req = input("Masukkan password >> ")
        if req == self.__password:
            cursor.execute("UPDATE tab_classes set NAMA = ? WHERE class_id = ?", (nama, kelasid))
            conn.commit()
            return("Data berhasil diubah!")
        else:
            return("Password salah, coba lagi nanti")

    def hapusKelas(self):
        delKelas = (input("Masukkan nama kelas yang ingin dihapus >> ")).upper()
        req = input("Masukkan password >> ")
        if req == self.getPassword():
            cursor.execute(
                "delete from tab_classes where nama = ?", (delKelas,))
            conn.commit()
            return (">> Kelas berhasil dihapus")
        else:
            return(">> Password salah, coba lagi nanti")

    def tambahSiswa(self):
        nama = input("Masukkan nama >> ")
        kelas = input("Masukkan nama kelas >> ")
        gender = input(
            "Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
        if gender == "l":
            gender = "Laki-Laki"
        elif gender == "p":
            gender = "Perempuan"
        else:
            gender = "unset"
        alamat = input("Masukkan alamat >> ")
        nohp = input("Masukkan nomor hp >> ")
        query = cursor.execute(
            "SELECT * FROM tab_classes WHERE NAMA = ?", (kelas,))
        for row in query:
            idkelas = int(row[0])
        siswa = Student(nama, idkelas, gender, alamat, nohp, 1)
        tempo = cursor.execute(
            "select * from tab_students where PHONE = ?", (siswa.getPhone(),))
        if tempo.fetchone() is None:
            cursor.execute("insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)",
                           (siswa.getNama(), siswa.getKelas(), siswa.getGender(), siswa.getAlamat(), siswa.getPhone()))
            conn.commit()
            return(">> Siswa berhasil didaftarkan")
        else:
            return(">> Siswa sudah terdaftar")

    def editSiswa(self):
        data = []
        nomorid = input("Masukkan id siswa yang akan diedit >> ")
        query = cursor.execute("SELECT * FROM tab_students WHERE student_id = ?", (nomorid,))
        if query.fetchone() is None:
            return("Siswa tidak terdaftar") 
        else:
            query = cursor.execute("SELECT * FROM tab_students WHERE student_id = ?", (nomorid,))
            for row in query:
                data.append(row)
            siswa = Student(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], nomorid)
            self.clear()
            self.pilihan = input("""=============================================
               EDIT DATA SISWA               
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Edit nama
[b] Edit kelas
[c] Edit Jenis Kelamin
[d] Edit Alamat
[e] Edit Nomor Hp
=============================================
Masukkan pilihan >> """)
            if self.pilihan == "a":
                siswa.setNama(input("Masukkan nama siswa >> "))
                cursor.execute("UPDATE tab_students set NAMA = ? WHERE student_id = ?", (siswa.getNama(), nomorid))
                conn.commit()
            elif self.pilihan == "b":
                siswa.setKelas(input("Masukkan id kelas >> "))
                cursor.execute("UPDATE tab_students set Kelas = ? WHERE student_id = ?", (siswa.getKelas(), nomorid))
                conn.commit()
            elif self.pilihan == "c":
                gender = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
                if gender == "l":
                    gender = "Laki-Laki"
                elif gender == "p":
                    gender = "Perempuan"
                else:
                    gender = "unset"
                siswa.setGender(gender)
                cursor.execute("UPDATE tab_students set jenis_kelamin = ? WHERE student_id = ?", (siswa.getGender(), nomorid))
                conn.commit()
            elif self.pilihan == "d":
                siswa.setAlamat("Masukkan alamat >> ")
                cursor.execute("UPDATE tab_students set Alamat = ? WHERE student_id = ?", (siswa.getAlamat(), nomorid))
                conn.commit()
            elif self.pilihan == "e":
                siswa.setPhone("Masukkan nomor hp >> ")
                cursor.execute("UPDATE tab_students set Phone = ? WHERE student_id = ?", (siswa.getPhone(), nomorid))
                conn.commit()
            else:
                return "Pilihan tidak terdapat pada menu"
            return "Kembali ke menu.."

    def hapusSiswa(self):
        nomorid = input("Masukkan id siswa yang akan dihapus >> ")
        req = input("Masukkan password >> ")
        if req == self.getPassword():
            cursor.execute(
                "delete from tab_students where student_id = ?", (nomorid,))
            conn.commit()
            return (">> Siswa berhasil dihapus")
        else:
            return(">> Password salah, coba lagi nanti")

    def hapusGuru(self):
        d = input("ingin menghapus data? ketik 'y' jika iya ")
        if d == "y":
            inpId = input("Masukkan id guru yang ingin dihapus ")
            temp = cursor.execute(
                "select * from tab_teachers where teacher_id = ?", (inpId,))
            if temp.fetchone() is None:
                print(">> Guru tidak ada")
            else:
                cursor.execute(
                    "delete from tab_teachers where teacher_id = ?", (inpId,))
                conn.commit()
                print(">> Guru telah dihapus")
        else:
            pass

    def hapusJadwal(self):
        e = input("Ingin menghapus jadwal? ketik 'y' jika iya ")
        if e == "y":
            f = input("Pada Hari apa jadwal tersebut? >> ").upper()
            temp = cursor.execute(
                "select * from tab_schedules where DAY = ?", (f,))
            if temp.fetchone() is None:
                print(">> Jadwal tidak ada")
            else:
                tempf = cursor.execute(
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
                tempjid = cursor.execute(
                    "select * from tab_schedules where id = ?", (jid,))
                if tempjid.fetchone() is None:
                    print(">> ID Jadwal tidak ditemukan")
                else:
                    cursor.execute(
                        "delete from tab_schedules where id = ?", (jid,))
                    conn.commit()
                    print(">> Jadwal telah dihapus")
        else:
            pass

    def mengelolaKelas(self):
        self.pilihan = input("""=============================================
                KELOLA KELAS                 
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Kelas
[b] Tambahkan Kelas
[c] Edit Kelas
[d] Hapus Kelas
[e] Tambahkan Siswa
[f] Edit Siswa
[g] Hapus Siswa
[h] Kembali ke Menu Admin <-Ongoing
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            self.clear()
            return self.lihatKelas()
        elif self.pilihan == "b":
            return self.tambahKelas()
        elif self.pilihan == "c":
            return self.editKelas()
        elif self.pilihan == "d":
            return self.hapusKelas()
        elif self.pilihan == "e":
            return self.tambahSiswa()
        elif self.pilihan == "f":
            return self.editSiswa()
        elif self.pilihan == "g":
            return self.hapusSiswa()
        elif self.pilihan == "h":
            return "NOT YET"
        else:
            return("Menu tidak tersedia")

    def clear(self):
        os.system('cls')

    def lihatGuru(self):
        query = cursor.execute('''
                SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers''')
        for row in query:
            print (f"""
                    Nama: {row[0]}
                    Bidang: {row[1]}
                    Jenis Kelamin: {row[2]}
                    Alamat: {row[3]}
                    No.HP: {row[4]}
                """)
        return ("\nFinish !!")
    
    def tambahGuru(self):
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
                nohp, 1)
        tempo = cursor.execute(
            "select * from tab_teachers where PHONE = ?", (guru.getPhone(),))
        if tempo.fetchone() is None:
            cursor.execute("insert into tab_teachers (NAMA, JENIS_KELAMIN, MAPEL, ALAMAT, PHONE) values (?,?,?,?,?)", (
                guru.getNama(), guru.getGender(), guru.getMapel(), guru.getAlamat(), guru.getPhone()))
            conn.commit()
            return (">> Guru berhasil didaftarkan")
        else:
            return (">> Guru sudah terdaftar")
    
    def editGuru(self):
        data = []
        nomorid = input("Masukkan id guru yang akan diedit >> ")
        query = cursor.execute("SELECT * FROM tab_teachers WHERE teacher_id = ?", (nomorid,))
        if query.fetchone() is None:
            return("Guru tidak terdaftar") 
        else:
            query = cursor.execute("SELECT * FROM tab_teachers WHERE teacher_id = ?", (nomorid,))
            for row in query:
                data.append(row)
            guru = Teacher(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], nomorid)
            self.clear()
            self.pilihan = input("""=============================================
               EDIT DATA GURU               
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Edit Nama
[b] Edit Mapel
[c] Edit Jenis Kelamin
[d] Edit Alamat
[e] Edit Nomor Hp
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            guru.setNama(input("Masukkan nama guru >> "))
            cursor.execute("UPDATE tab_teachers set NAMA = ? WHERE teacher_id = ?", (guru.getNama(), nomorid))
            conn.commit()
        elif self.pilihan == "b":
            guru.setMapel(input("Masukkan mapel guru >> "))
            cursor.execute("UPDATE tab_teachers set MAPEL = ? WHERE teacher_id = ?", (guru.getMapel(), nomorid))
            conn.commit()
        elif self.pilihan == "c":
            gender = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
            if gender == "l":
                gender = "Laki-Laki"
            elif gender == "p":
                gender = "Perempuan"
            else:
                gender = "unset"
            guru.setGender(gender)
            cursor.execute("UPDATE tab_teachers set jenis_kelamin = ? WHERE teacher_id = ?", (guru.getGender(), nomorid))
            conn.commit()
        elif self.pilihan == "d":
            guru.setAlamat("Masukkan alamat >> ")
            cursor.execute("UPDATE tab_teachers set Alamat = ? WHERE teacher_id = ?", (guru.getAlamat(), nomorid))
            conn.commit()
        elif self.pilihan == "e":
            guru.setPhone("Masukkan nomor hp >> ")
            cursor.execute("UPDATE tab_teachers set Phone = ? WHERE teacher_id = ?", (guru.getPhone(), nomorid))
            conn.commit()
        else:
            return "Pilihan tidak terdapat pada menu"
        return "Kembali ke menu.."

    def mengelolaGuru(self):
        self.pilihan = input("""=============================================
                KELOLA GURU                 
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Guru
[b] Tambah Guru
[c] Hapus Guru
[d] Edit Guru
[e] Kembali ke Menu Admin <- Ongoing
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            return self.lihatGuru()
        elif self.pilihan == "b":
            return self.tambahGuru()
        elif self.pilihan == "c":
            return self.hapusGuru()
        elif self.pilihan == "d":
            return self.editGuru()
        elif self.pilihan == "e":
            return "NOT YET"
        else:
            return "Menu tidak tersedia"

    def lihatJadwal(self):
        query = cursor.execute("""
        SELECT tab_teachers.NAMA, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE, tab_teachers.MAPEL
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        """)

        for row in query:
            print(f"""
                Pengajar: {row[0]}
                Mata Pelajaran: {row[6]}
                Kelas: {row[1]}
                Waktu: {row[2]}, {row[3]}, {row[4]}
                Note: {row[5]}
            """)
        return "Finish !!"

    def tambahJadwal(self):
        klaslist = []
        gurulist = []
        sql1 = cursor.execute(
            "select class_id from tab_classes")
        for i in sql1:
            klaslist.append(i)
        res1 = str(klaslist)[1:-1]
        print(f"List kelas tersedia: {res1}")
        sql2 = cursor.execute(
            "select teacher_id from tab_teachers")
        for i in sql2:
            gurulist.append(i)
        res2 = str(gurulist)[1:-1]
        print(f"List guru tersedia: {res2}")
        klasid = int(input("Masukkan id kelas >> "))
        guruid = int(input("Masukkan id guru >> "))
        hari = input("Masukkan hari >> ").upper()
        thn = input("Masukkan tahun (YYYY) >> ")
        bln = input("Masukkan bulan (MM) >> ")
        tg = input("Masukkan tanggal (DD) >> ")
        tanggal = "{}/{}/{}".format(tg, bln, thn)
        waktumulai = input(
            "Masukkan waktu mulai dengan format jam 24.00 >> ")
        waktuakhir = input(
            "Masukkan waktu selesai dengan format jam 24.00 >> ")
        waktu = "{} s/d {}".format(waktumulai, waktuakhir)
        jadwal = Schedule(1, klasid, guruid,
                          hari, tanggal, waktu, 1)
        tempor = cursor.execute(
            "select * from tab_schedules where DATE = ? AND TIME = ?", (jadwal.getTanggal(), jadwal.getWaktu(),))
        if tempor.fetchone() is None:
            cursor.execute("insert into tab_schedules (class_id, teacher_id, DAY, DATE, TIME) values (?,?,?,?,?)", (
                jadwal.getKelas(), jadwal.getGuru(), jadwal.getHari(), jadwal.getTanggal(), jadwal.getWaktu()))
            conn.commit()
            print(">> Jadwal berhasil ditambahkan")
        else:
            print(">> Jadwal crash, silahkan tambahkan ulang")
    
    def editJadwal(self):
        data = []
        nomorid = input("Masukkan id jadwal yang akan diedit >> ")
        query = cursor.execute("SELECT * FROM tab_schedules WHERE id = ?", (nomorid,))
        if query.fetchone() is None:
            return("Jadwal tidak ada") 
        else:
            query = cursor.execute("SELECT * FROM tab_schedules WHERE id = ?", (nomorid,))
            for row in query:
                data.append(row)
            jadwal = Schedule(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], nomorid)
            self.clear()
            self.pilihan = input("""=============================================
               EDIT DATA JADWAL               
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Edit Kelas
[b] Edit Guru Pengajar
[c] Edit Hari
[d] Edit Tanggal
[e] Edit Waktu
[f] Edit Catatan
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            jadwal.setKelas(input("Masukkan id kelas >> "))
            cursor.execute("UPDATE tab_schedules set class_id = ? WHERE id = ?", (jadwal.getKelas(), nomorid))
            conn.commit()
        elif self.pilihan == "b":
            jadwal.setGuru(input("Masukkan id guru >> "))
            cursor.execute("UPDATE tab_schedules set teacher_id = ? WHERE id = ?", (jadwal.getGuru(), nomorid))
            conn.commit()
        # elif self.pilihan == "c":
        #     jadwal.setHari(input("Masukkan nama")).upper()
        #     cursor.execute("UPDATE tab_schedules set DAY = ? WHERE id = ?", (jadwal.getHari(), nomorid))
        #     conn.commit()
        # elif self.pilihan == "d":
        #     jadwal.setDate("Masukkan tanggal >> ")
        #     cursor.execute("UPDATE tab_schedules set teacher_id = ? WHERE id = ?", (guru.getAlamat(), nomorid))
        #     conn.commit()
        # elif self.pilihan == "e":
        #     jadwal.setWaktu("Masukkan nomor hp >> ")
        #     cursor.execute("UPDATE tab_teachers set Phone = ? WHERE teacher_id = ?", (guru.getPhone(), nomorid))
        #     conn.commit()
        elif self.pilihan == "f":
            jadwal.setNote("Masukkan catatan >> ")
            cursor.execute("UPDATE tab_schedules set NOTE = ? WHERE id = ?", jadwal.getNote(), nomorid)
        else:
            return "Pilihan tidak terdapat pada menu"
        return "Kembali ke menu.."

    def mengelolaJadwal(self):
        self.pilihan = input("""=============================================
                KELOLA JADWAL                 
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Jadwal
[b] Tambah Jadwal
[c] Hapus Jadwal
[d] Edit Jadwal
[e] Kembali ke Menu Admin <- Ongoing
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            return self.lihatJadwal()
        elif self.pilihan == "b":
            return self.tambahJadwal()
        elif self.pilihan == "c":
            return self.hapusJadwal()
        elif self.pilihan == "d":
            return self.editJadwal()
        elif self.pilihan == "e":
            return "NOT YET"
        else:
            return "Menu tidak tersedia"
