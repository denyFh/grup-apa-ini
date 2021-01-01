import sqlite3
from User import User
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class Student(User):

    def __init__(self, nama, kelas, gender, alamat, phone, iD):
        super().__init__(nama, gender, alamat, phone, iD)
        self._kelas = kelas

    def getKelas(self):
        return self._kelas

    def setKelas(self, value):
        self._kelas = value

    def dataDiri(self):
        query = cursor.execute('''\
            SELECT tab_students.student_id, tab_students.nama, tab_classes.nama, tab_students.jenis_kelamin, tab_students.alamat, tab_students.phone
            FROM tab_students
            INNER JOIN tab_classes
            ON tab_students.kelas = tab_classes.class_id
            WHERE tab_students.student_id = ?''', (self.id,))
        for row in query:
            print(f"""=============================================
                  DATA DIRI                  
=============================================
ID\t\t: {row[0]}
Nama\t\t: {row[1]}
Kelas\t\t: {row[2]}
Jenis Kelamin\t: {row[3]}
Alamat\t\t: {row[4]}
Nomor telepon\t: {row[5]}
=============================================
""")

    def lihatJadwal(self):
        query0 = cursor.execute(
            """SELECT KELAS from tab_students
            WHERE student_id = ?""", (self.id,))

        for row in query0:
            kelas = row[0]

        query = cursor.execute("""
        SELECT tab_teachers.NAMA, tab_teachers.MAPEL, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        WHERE tab_classes.class_id = ?""", (kelas,))
        print("""=============================================
              JADWAL PELAJARAN               
=============================================""")
        for row in query:
            print(f"""Pengajar: {row[0]}
Mata Pelajaran: {row[1]}
Waktu: {row[3]}, {row[4]}, {row[5]}
Note: {row[6]}
=============================================""")
        print()

    def lihatPengajar(self):
        self.pilihan = input("""=============================================
               LIHAT PENGAJAR                
=============================================
Silahkan pilih menu yang anda inginkan:
[a] Lihat semua pengajar
[b] Lihat berdasarkan mata pelajaran
=============================================
Masukkan pilihan >> """)
        if self.pilihan == "a":
            self.clear()
            query = cursor.execute('''
                SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers''')
            if query.fetchone() is None:
                print("Tidak ada pengajar")
            else:
                query = cursor.execute(
                    '''SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers''')
                print("""=============================================
                DAFTAR PENGAJAR                
=============================================""")
                for row in query:
                    print(f"""Nama: {row[0]}
Bidang: {row[1]}
Jenis Kelamin: {row[2]}
Alamat: {row[3]}
No.HP: {row[4]}
=============================================""")
            print()
        elif self.pilihan == "b":
            self.clear()
            mapel = input(
                "Masukkan mata pelajaran yang diampu >> ").capitalize()
            query = cursor.execute('''
                SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers WHERE tab_teachers.Mapel = ?''', (mapel,))
            if query.fetchone() is None:
                print(f"\nTidak ada pengajar mata pelajaran {mapel}\n")
            else:
                query = cursor.execute(
                    '''SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers WHERE tab_teachers.Mapel = ?''', (mapel,))
                print("""=============================================
                DAFTAR PENGAJAR                
=============================================""")
                for row in query:
                    print(f"""Nama: {row[0]}
Bidang: {row[1]}
Jenis Kelamin: {row[2]}
Alamat: {row[3]}
No.HP: {row[4]}
=============================================""")
                print()
        else:
            print("\n============ Menu Tidak Tersedia ============\n")

    # def lihatTeman(self):
    #     query0 = cursor.execute(
    #         """SELECT KELAS from tab_students
    #         WHERE student_id = ?""", (self.id,))

    #     for row in query0:
    #         kelas = row[0]

    #     query = cursor.execute('''\
    #             SELECT tab_students.nama, tab_classes.nama, tab_students.jenis_kelamin, tab_students.alamat, tab_students.phone
    #             FROM tab_students
    #             INNER JOIN tab_classes
    #             ON tab_students.kelas = tab_classes.class_id
    #             WHERE tab_classes.class_id = ?''', (kelas,))

    #     for row in query:
    #         print(f"""
    #                 Nama: {row[0]}
    #                 Kelas: {row[1]}
    #                 Jenis Kelamin: {row[2]}
    #                 Alamat: {row[3]}
    #                 No.HP: {row[4]}
    #             """)
