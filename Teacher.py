import sqlite3
from User import User
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class Teacher(User):
    daftarid = []
    def __init__(self, nama, gender, mapel, alamat, phone, iD):
        super().__init__(nama, gender, alamat, phone, iD)
        self._mapel = mapel

    def getMapel(self):
        return self._mapel

    def lihatJadwal(self):
        query = conn.execute("""
        SELECT tab_schedules.id, tab_teachers.NAMA, tab_classes.NAMA, tab_schedules.DAY, tab_schedules.DATE, tab_schedules.TIME, tab_schedules.NOTE, tab_teachers.MAPEL
        FROM tab_schedules
        INNER JOIN tab_classes 
        ON tab_schedules.class_id = tab_classes.class_id
        INNER JOIN tab_teachers
        ON tab_schedules.teacher_id = tab_teachers.teacher_id
        WHERE tab_teachers.teacher_id = ?""", (self.id,))

        for row in query:
            Teacher.daftarid.append(row[0])
            print(f"""
                ID: {row[0]}
                Pengajar: {row[1]}
                Mata Pelajaran: {row[7]}
                Kelas: {row[2]}
                Waktu: {row[3]}, {row[4]}, {row[5]}
                Note: {row[6]}
            """)

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
            """)
