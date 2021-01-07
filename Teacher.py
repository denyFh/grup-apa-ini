import sqlite3
from User import User
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()

#class guru, merupakan peranakan / turunan dari class user
class Teacher(User):
    daftarid = []
    #inisialisasi class object, atribut diambil dari class user dan terdapat perbedaan/tambahan atribut mapel
    def __init__(self, nama, gender, mapel, alamat, phone, iD):
        super().__init__(nama, gender, alamat, phone, iD)
        self._mapel = mapel

    #mengambil atribut mapel
    def getMapel(self):
        return self._mapel

    #merubah atau menambahkan atribut mapel
    def setMapel(self, value):
        self._mapel = value

    #melihat data diri guru
    def dataDiri(self):
        query = conn.execute('''\
            SELECT tab_teachers.teacher_id, tab_teachers.nama, tab_teachers.jenis_kelamin, tab_teachers.mapel, tab_teachers.alamat, tab_teachers.phone
            FROM tab_teachers WHERE tab_teachers.teacher_id = ?''', (self.id,))
        for row in query:
            print(f"""=============================================
                  DATA DIRI                  
=============================================
ID\t\t: {row[0]}
Nama\t\t: {row[1]}
Mata Pelajaran\t: {row[3]}
Jenis Kelamin\t: {row[2]}
Alamat\t\t: {row[4]}
Nomor telepon\t: {row[5]}
=============================================
""")

    #melihat data kelas yang akan diajar guru
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
            "=============================================\nMasukkan nama kelas untuk melihat daftar siswa >> ")).upper()
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
                print(f"""ID: {row[0]}
Nama: {row[1]}
Jenis Kelamin: {row[3]}
Alamat: {row[4]}
No.HP: {row[5]}
=============================================""")
            print()
        else:
            print(">> Kelas tidak terdaftar\n")

    #melihat jadwal mengajar guru
    def lihatJadwal(self):
        query = conn.execute("""
        SELECT tab_schedules.id, tab_teachers.NAMA, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE, tab_teachers.MAPEL
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        WHERE tab_teachers.teacher_id = ?""", (self.id,))

        print("""=============================================
               DAFTAR JADWAL                 
=============================================""")
        for row in query:
            Teacher.daftarid.append(row[0])
            print(f"""ID: {row[0]}
Pengajar: {row[1]}
Mata Pelajaran: {row[7]}
Kelas: {row[2]}
Waktu: {row[3]}, {row[4]}, {row[5]}
Note: {row[6]}
=============================================""")
        print()
        self.editCatatan()

    #mengedit atau menambahkan catatan pada kolom note jadwal sesuai dengan guru yang akan mengajar
    def editCatatan(self):
        a = input("Edit catatan? (ketik 'y' jika iya) ")
        if a == "y":
            jadwal = int(input("Masukkan ID Jadwal: "))
            note = input("Masukkan catatan: ")
            if jadwal and note != '':
                cursor.execute(
                    "UPDATE tab_schedules set NOTE = ? WHERE id = ?", (note, jadwal))
                if jadwal in Teacher.daftarid:
                    print (">> Catatan berhasil di tambahkan")
                    conn.commit()
                else:
                    print(
                        ">> Hubungi guru yang bertugas untuk memberikan catatan")
            else:
                print("Tolong isi semua isian")
        else:
            pass
