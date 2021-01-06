import sqlite3
import os
from Schedule import Schedule
from Classes import Classes
from Student import Student
from Teacher import Teacher
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

#class admin
class Admin:
    #inisialisasi class object, berisi atribut admin
    def __init__(self, username, password, iD):
        self.__username = username
        self.__password = password
        self.id = iD
    #mengambil atribut username
    def getUsername(self):
        return self.__username
    #mengambil atribut password
    def getPassword(self):
        return self.__password
    #merubah atau menambahkan atribut username
    def setUsername(self, value):
        self.__username = value
    #merubah atau menambahkan atribut password
    def setPassword(self, value):
        self.__password = value
    #menunjukkan detail data diri admin
    def detail(self):
        password = len(self.getPassword())*"*"
        return (f"""=============================================
                 DATA DIRI                   
=============================================
Username = {self.getUsername()}
Password = {password}
""")

    #mengedit atau mengubah username admin
    def editUsername(self):
        self.editusername = input("Masukkan username: ")
        if self.editusername != '':
            self.tempo = cursor.execute(
                "select * from tab_admins where username = ?", (self.editusername,))
            if self.tempo.fetchone() is None:
                self.setUsername(self.editusername)
                cursor.execute("UPDATE tab_admins set USERNAME = ? WHERE password = ?", (
                    self.getUsername(), self.getPassword()))
                conn.commit()
                return(" >> Username berhasil diubah!")
            else:
                return(" >> Username sudah digunakan, silahkan gunakan username lain")
        else:
            return(" >> Username tidak boleh kosong")

    #mengedit atau mengubah password admin
    def editPassword(self):
        self.newpassword = input("Masukkan password baru: ")
        if self.newpassword != '':
            self.tempo = cursor.execute(
                "select * from tab_admins where password = ?", (self.newpassword,))
            if self.tempo.fetchone() is None:
                self.setPassword(self.newpassword)
                cursor.execute("UPDATE tab_admins set password = ? WHERE username = ?",
                            (self.getPassword(), self.getUsername()))
                conn.commit()
                return(" >> Password berhasil diubah, silahkan login kembali untuk melanjutkan kegiatan")
            else:
                return(" >> Password sudah digunakan, silahkan gunakan password lain")
        else:
            return(" >> Password tidak boleh kosong")

    #menu untuk mengedit data diri admin
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

    #melihat data kelas 
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

    #menambahkan data kelas
    def tambahKelas(self):
        kelas = Classes(input("Masukkan nama kelas >> ").upper())
        if kelas != '':
            self.tempo = cursor.execute(
                "select * from tab_classes where nama = ?", (kelas.getClassName(),))
            if self.tempo.fetchone() is None:
                cursor.execute(
                    "insert into tab_classes (nama) values (?)", (kelas.getClassName()))
                conn.commit()
                return (" >> Kelas berhasil ditambahkan")
            else:
                return (" >> Nama kelas sudah terdaftar")
        else:
            return(" >> Nama Kelas tidak boleh kosong")

    #mengedit data kelas
    def editKelas(self):
        self.query = cursor.execute("SELECT * FROM tab_classes")
        print("""=============================================
                DAFTAR KELAS                 
=============================================""")
        for row in self.query:
            print(f"""[{row[0]}] {row[1]}""")
        kelasid = input("Masukkan id kelas >> ")
        nama = input("Masukkan nama kelas baru >> ").upper()
        if kelasid and nama != '':
            req = input("Masukkan password >> ")
            if req == self.__password:
                self.tempo = cursor.execute(
                "select * from tab_classes where nama = ?", (nama,))
                if self.tempo.fetchone() is None:
                    cursor.execute("UPDATE tab_classes set NAMA = ? WHERE class_id = ?", (nama, kelasid))
                    conn.commit()
                    return(" >> Data berhasil diubah!")
                else:
                    return(" >> Kelas sudah ada")
            else:
                return(" >> Password salah, coba lagi nanti")
        else:
            return(" >> ID atau Nama Kelas tidak boleh kosong")

    #menghapus data kelas
    def hapusKelas(self):
        self.query = cursor.execute("SELECT * FROM tab_classes")
        print("""=============================================
                DAFTAR KELAS                 
=============================================""")
        for row in self.query:
            print(f"""[{row[0]}] {row[1]}""")
        delKelas = (input("Masukkan nama kelas yang ingin dihapus >> ").upper())
        if delKelas != '':
            req = input("Masukkan password >> ")
            if req == self.getPassword():
                self.tempo = cursor.execute(
                "select * from tab_classes where nama = ?", (delKelas,))
                if self.tempo.fetchone() != None:
                    cursor.execute(
                        "delete from tab_classes where nama = ?", (delKelas,))
                    conn.commit()
                    self.resetsequenceKelas()
                    return (" >> Kelas berhasil dihapus")
                else:
                    return(" >> Kelas tidak terdaftar")
            else:
                return(" >> Password salah, coba lagi nanti")
        else:
            return(" >> Nama Kelas tidak boleh kosong")

    #mengurutkan ulang kelas
    def resetsequenceKelas(self):
        jmlkelas = []
        self.query = cursor.execute(
            "select * from tab_classes")
        for row in self.query:
            jmlkelas.append(row)
        jmlseq = len(jmlkelas)
        cursor.execute(
            "update 'sqlite_sequence' set 'seq' = ? where name = 'tab_classes'", (str(jmlseq),))
        conn.commit()

    #menambahkan data siswa
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
        condition = [nama, kelas, gender, alamat, nohp]
        if '' not in condition:
            query = cursor.execute(
                "SELECT * FROM tab_classes WHERE NAMA = ?", (kelas,))
            for row in query:
                kelas = int(row[0])
            siswa = Student(nama, kelas, gender, alamat, nohp, 1)
            tempo = cursor.execute(
                "select * from tab_students where PHONE = ?", (siswa.getPhone(),))
            if tempo.fetchone() is None:
                cursor.execute("insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)",
                            (siswa.getNama(), siswa.getKelas(), siswa.getGender(), siswa.getAlamat(), siswa.getPhone()))
                conn.commit()
                return(" >> Siswa berhasil didaftarkan")
            else:
                return(" >> Siswa sudah terdaftar")
        else:
            return(" >> Semua data siswa harus terisi")

    #mengedit data siswa
    def editSiswa(self):
        self.query = cursor.execute("SELECT * FROM tab_students")
        print("""=============================================
                DAFTAR SISWA                 
=============================================""")
        for row in self.query:
            print(f"""[{row[0]}] {row[1]}""")
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
            if self.pilihan == "a": #edit nama siswa
                siswa.setNama(input("Masukkan nama siswa >> "))
                if siswa.getNama() != '':
                    cursor.execute("UPDATE tab_students set NAMA = ? WHERE student_id = ?", (siswa.getNama(), nomorid))
                    conn.commit()
                    return "Nama berhasil diubah"
                else:
                    return "Nama tidak boleh kosong"
            elif self.pilihan == "b": #edit kelas siswa
                siswa.setKelas(input("Masukkan id kelas >> "))
                if siswa.getKelas() != '':
                    cursor.execute("UPDATE tab_students set Kelas = ? WHERE student_id = ?", (siswa.getKelas(), nomorid))
                    conn.commit()
                    return "Kelas berhasil diubah"
                else:
                    return "Kelas tidak boleh kosong"
            elif self.pilihan == "c": #edit jenis kelamin siswa
                gender = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
                if gender == "l":
                    gender = "Laki-Laki"
                elif gender == "p":
                    gender = "Perempuan"
                elif gender == '':
                    gender = ''
                else:
                    gender = "unset"
                if gender != '':
                    siswa.setGender(gender)
                    cursor.execute("UPDATE tab_students set jenis_kelamin = ? WHERE student_id = ?", (siswa.getGender(), nomorid))
                    conn.commit()
                    return "Jenis Kelamin berhasil diubah"
                else:
                    return "Jenis Kelamin tidak boleh kosong"
            elif self.pilihan == "d": #edit alamat siswa
                siswa.setAlamat("Masukkan alamat >> ")
                if siswa.getAlamat() != '':
                    cursor.execute("UPDATE tab_students set Alamat = ? WHERE student_id = ?", (siswa.getAlamat(), nomorid))
                    conn.commit()
                    return "Alamat berhasil diubah"
                else:
                    return "Alamat tidak boleh kosong"
            elif self.pilihan == "e": #edit nomor hp siswa
                siswa.setPhone("Masukkan nomor hp >> ")
                if siswa.getPhone() != '':
                    cursor.execute("UPDATE tab_students set Phone = ? WHERE student_id = ?", (siswa.getPhone(), nomorid))
                    conn.commit()
                    return "Nomor Hp berhasil diubah"
                else:
                    return "Nomor Hp tidak boleh kosong"
            else:
                return "Pilihan tidak terdapat pada menu"
            return "Kembali ke menu.."

    #menghapus data siswa
    def hapusSiswa(self):
        self.query = cursor.execute("SELECT * FROM tab_students")
        print("""=============================================
                DAFTAR SISWA                 
=============================================""")
        for row in self.query:
            print(f"""[{row[0]}] {row[1]}""")
        nomorid = input("Masukkan id siswa yang akan dihapus >> ")
        req = input("Masukkan password >> ")
        if req == self.getPassword():
            if nomorid != '':
                self.tempo = cursor.execute(
                "SELECT * FROM tab_students WHERE student_id = ?", (nomorid,))
                if self.tempo.fetchone() != None:
                    cursor.execute(
                        "delete from tab_students where student_id = ?", (nomorid,))
                    conn.commit()
                    self.resetsequenceSiswa()
                    return (" >> Siswa berhasil dihapus")
                else:
                    return (" >> Siswa tidak terdaftar")
            else:
                return (" >> Harap isi ID Siswa yang ingin dihapus")
        else:
            return(">> Password salah, coba lagi nanti")
    
    #mengurutkan ulang siswa
    def resetsequenceSiswa(self):
        jmlsiswa = []
        self.query = cursor.execute(
            "select * from tab_students")
        for row in self.query:
            jmlsiswa.append(row)
        jmlseqa = len(jmlsiswa)
        jmlseq = "190610{}".format(jmlseqa)
        cursor.execute(
            "update 'sqlite_sequence' set 'seq' = ? where name = 'tab_students'", (jmlseq,))
        conn.commit()

    #menghapus data guru
    def hapusGuru(self):
        d = input("ingin menghapus data? ketik 'y' jika iya ")
        if d == "y":
            inpId = input("Masukkan id guru yang ingin dihapus >> ")
            if inpId != '':
                temp = cursor.execute(
                    "select * from tab_teachers where teacher_id = ?", (inpId,))
                if temp.fetchone() is None:
                    print(">> Guru tidak ada")
                else:
                    cursor.execute(
                        "delete from tab_teachers where teacher_id = ?", (inpId,))
                    conn.commit()
                    self.resetsequenceGuru()
                    return (" >> Guru telah dihapus")
            else:
                return (" >> Harap isi ID Guru yang akan dihapus")
        else:
            pass

    #mengurutkan ulang guru
    def resetsequenceGuru(self):
        jmlguru = []
        self.query = cursor.execute(
            "select * from tab_teachers")
        for row in self.query:
            jmlguru.append(row)
        jmlseqa = len(jmlguru)
        if jmlseqa < 10:
            jmlseq = "1100{}".format(jmlseqa)
        elif jmlseqa > 9:
            jmlseq = "110{}".format(jmlseqa)
        cursor.execute(
            "update 'sqlite_sequence' set 'seq' = ? where name = 'tab_classes'", (jmlseq,))
        conn.commit()

    #menghapus data jadwal
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

    #Mengelola data kelas
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
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            self.clear()
            return self.lihatKelas()
        elif self.pilihan == "b":
            self.clear()
            return self.tambahKelas()
        elif self.pilihan == "c":
            self.clear()
            return self.editKelas()
        elif self.pilihan == "d":
            self.clear()
            return self.hapusKelas()
        elif self.pilihan == "e":
            self.clear()
            return self.tambahSiswa()
        elif self.pilihan == "f":
            self.clear()
            return self.editSiswa()
        elif self.pilihan == "g":
            self.clear()
            return self.hapusSiswa()
        else:
            return("Menu tidak tersedia")

    #membersihkan console window
    def clear(self):
        os.system('cls')

    #melihat data guru
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
    
    #menambahkan data guru
    def tambahGuru(self):
        nama = input("Masukkan nama >> ")
        mapel = input("Masukkan mata pelajaran >> ")
        jk = input(
            "Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
        if jk == "l":
            jk = "Laki-Laki"
        elif jk == "p":
            jk = "Perempuan"
        elif jk == '':
            jk = ''
        else:
            jk = "unset"
        alamat = input("Masukkan alamat >> ")
        nohp = input("Masukkan nomor hp >> ")
        condition = [nama, jk, mapel, alamat, nohp]
        if '' not in condition:
            guru = Teacher(nama, jk, mapel, alamat,
                    nohp, 1)
            tempo = cursor.execute(
                "select * from tab_teachers where PHONE = ?", (guru.getPhone(),))
            if tempo.fetchone() is None:
                cursor.execute("insert into tab_teachers (NAMA, JENIS_KELAMIN, MAPEL, ALAMAT, PHONE) values (?,?,?,?,?)", (
                    guru.getNama(), guru.getGender(), guru.getMapel(), guru.getAlamat(), guru.getPhone()))
                conn.commit()
                return (" >> Guru berhasil didaftarkan")
            else:
                return (" >> Guru sudah terdaftar")
        else:
            return (" >> Semua data Guru harus terisi")
    
    #mengedit data guru
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
        if self.pilihan == "a": #edit nama guru
            guru.setNama(input("Masukkan nama guru >> "))
            if guru.getNama() != '':
                cursor.execute("UPDATE tab_teachers set NAMA = ? WHERE teacher_id = ?", (guru.getNama(), nomorid))
                conn.commit()
                return "Nama guru berhasil diubah"
            else:
                return "Nama guru tidak boleh kosong"
        elif self.pilihan == "b": #edit mapel guru
            guru.setMapel(input("Masukkan mapel guru >> "))
            if guru.getMapel() != '':
                cursor.execute("UPDATE tab_teachers set MAPEL = ? WHERE teacher_id = ?", (guru.getMapel(), nomorid))
                conn.commit()
                return "Mapel guru berhasil diubah"
            else:
                return "Mapel guru tidak boleh kosong"
        elif self.pilihan == "c": #edit jenis kelamin guru
            gender = input("Masukkan jenis kelamin (l) untuk laki laki dan (p) untuk perempuan >> ")
            if gender == "l":
                gender = "Laki-Laki"
            elif gender == "p":
                gender = "Perempuan"
            elif gender == '':
                gender = ''
            else:
                gender = "unset"
            if gender != '':
                guru.setGender(gender)
                cursor.execute("UPDATE tab_teachers set jenis_kelamin = ? WHERE teacher_id = ?", (guru.getGender(), nomorid))
                conn.commit()
                return "Jenis Kelamin Guru berhasil diubah"
            else:
                return "Jenis Kelamin Guru tidak boleh kosong"
        elif self.pilihan == "d": #edit alamat guru
            guru.setAlamat("Masukkan alamat >> ")
            if guru.getAlamat() != '':
                cursor.execute("UPDATE tab_teachers set Alamat = ? WHERE teacher_id = ?", (guru.getAlamat(), nomorid))
                conn.commit()
                return "Alamat Guru berhasil diubah"
            else:
                return "Alamat Guru tidak boleh kosong"
        elif self.pilihan == "e": #edit nomor hp guru
            guru.setPhone("Masukkan nomor hp >> ")
            if guru.getPhone() != '':
                cursor.execute("UPDATE tab_teachers set Phone = ? WHERE teacher_id = ?", (guru.getPhone(), nomorid))
                conn.commit()
                return "Nomor Hp Guru berhasil diubah"
            else:
                return "Nomor Hp Guru tidak boleh kosong"
        else:
            return "Pilihan tidak terdapat pada menu"
        return "Kembali ke menu.."

    #mengelola data guru
    def mengelolaGuru(self):
        self.pilihan = input("""=============================================
                KELOLA GURU                 
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Guru
[b] Tambah Guru
[c] Hapus Guru
[d] Edit Guru
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
        else:
            return "Menu tidak tersedia"

    #melihat data jadwal
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

    #menambahkan data jadwal
    def tambahJadwal(self):
        klaslist = []
        gurulist = []
        listhari = ['SENIN','SELASA','RABU','KAMIS','JUMAT','SABTU','MINGGU']
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
        inhari = input("Masukkan hari >> ").upper()
        if inhari not in listhari:
            print("Hari tidak terdaftar")
        else:
            hari = inhari
        thn = input("Masukkan tahun (YYYY) >> ")
        bln = input("Masukkan bulan (MM) >> ")
        tg = input("Masukkan tanggal (DD) >> ")
        tanggal = "{}/{}/{}".format(tg, bln, thn)
        jammulai = input("Masukkan Jam Mulai")
        menitmulai = input("Masukkan Menit Mulai")
        jamakhir = input("Masukkan Jam Berakhir")
        menitakhir = input("Masukkan Menit Berakhir")
        if int(jammulai) or int(jamakhir) > 24:
            print("Jam tidak exist")
        elif int(menitmulai) or int(menitakhir) > 59:
            print("Menit tidak exist")
        else:
            waktu = "{}.{} s/d {}.{}".format(jammulai, menitmulai, jamakhir, menitakhir)
        condition = [klasid, guruid, hari, tanggal, waktu]
        if '' not in condition:
            jadwal = Schedule(1, klasid, guruid,
                            hari, tanggal, waktu, 1)
            tempor = cursor.execute(
                "select * from tab_schedules where DATE = ? AND TIME = ?", (jadwal.getTanggal(), jadwal.getWaktu(),))
            if tempor.fetchone() is None:
                cursor.execute("insert into tab_schedules (class_id, teacher_id, DAY, DATE, TIME) values (?,?,?,?,?)", (
                    jadwal.getKelas(), jadwal.getGuru(), jadwal.getHari(), jadwal.getTanggal(), jadwal.getWaktu()))
                conn.commit()
                print(" >> Jadwal berhasil ditambahkan")
            else:
                print(" >> Jadwal crash, silahkan tambahkan ulang")
        else:
            return " >> Semua Data Jadwal harus terisi"
    
    #mengedit data jadwal
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
        if self.pilihan == "a": #edit kelas
            jadwal.setKelas(input("Masukkan id kelas >> "))
            if jadwal.getKelas() != '':
                cursor.execute("UPDATE tab_schedules set class_id = ? WHERE id = ?", (jadwal.getKelas(), nomorid))
                conn.commit()
                return "ID Kelas berhasil diubah"
            else:
                return "ID Kelas tidak boleh kosong"

        elif self.pilihan == "b": #edit guru pengajar
            jadwal.setGuru(input("Masukkan id guru >> "))
            if jadwal.getGuru() != '':
                cursor.execute("UPDATE tab_schedules set teacher_id = ? WHERE id = ?", (jadwal.getGuru(), nomorid))
                conn.commit()
                return "ID Guru berhasil diubah"
            else:
                return "ID Guru tidak boleh kosong"

        elif self.pilihan == "c": #edit hari
            listhari = ['SENIN','SELASA','RABU','KAMIS','JUMAT','SABTU','MINGGU']
            inhari = input("Masukkan hari >> ").upper()
            if inhari not in listhari:
                print("Hari tidak terdaftar")
            else:
                jadwal.setHari(inhari)
                cursor.execute("UPDATE tab_schedules set DAY = ? WHERE id = ?", (jadwal.getHari(), nomorid))
                conn.commit()
                return "Hari berhasil diubah"

        elif self.pilihan == "d": #edit tanggal
            thn = input("Masukkan tahun (YYYY) >> ")
            bln = input("Masukkan bulan (MM) >> ")
            tg = input("Masukkan tanggal (DD) >> ")
            condition = [thn, bln, tg]
            if '' not in condition:
                tanggal = "{}/{}/{}".format(tg, bln, thn)
                cursor.execute("UPDATE tab_schedules set DATE = ? WHERE id = ?", (jadwal.setTanggal(tanggal), nomorid))
                conn.commit()
                return "Tanggal berhasil diubah"
            else:
                return "Data Tanggal tidak boleh kosong"

        elif self.pilihan == "e": #edit waktu
            jammulai = input(int("Masukkan Jam Mulai"))
            menitmulai = input(int("Masukkan Menit Mulai"))
            jamakhir = input(int("Masukkan Jam Berakhir"))
            menitakhir = input(int("Masukkan Menit Berakhir"))
            condition = [jammulai, menitmulai, jamakhir, menitakhir]
            if '' not in condition:
                if jammulai or jamakhir > 24:
                    print("Jam tidak exist")
                elif menitmulai or menitakhir > 59:
                    print("Menit tidak exist")
                else:
                    waktu = "{}.{} s/d {}.{}".format(jammulai, menitmulai, jamakhir, menitakhir)
                    jadwal.setWaktu(waktu)
                    cursor.execute("UPDATE tab_teachers set TIME = ? WHERE id = ?", (jadwal.getWaktu(), nomorid))
                    conn.commit()
                    return "Jam berhasil diubah"
            else:
                return "Data jam tidak boleh kosong"

        elif self.pilihan == "f": #edit catatan
            jadwal.setNote("Masukkan catatan >> ")
            if jadwal.getNote() != '':
                cursor.execute("UPDATE tab_schedules set NOTE = ? WHERE id = ?", jadwal.getNote(), nomorid)
                conn.commit()
                return "Note berhasil diubah"
            else:
                return "Note tidak boleh kosong"
        else:
            return "Pilihan tidak terdapat pada menu"
        return "Kembali ke menu.."

    #mengelola data jadwal
    def mengelolaJadwal(self):
        self.pilihan = input("""=============================================
                KELOLA JADWAL                 
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat Jadwal
[b] Tambah Jadwal
[c] Hapus Jadwal
[d] Edit Jadwal
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
        else:
            return "Menu tidak tersedia"
