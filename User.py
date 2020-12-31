import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()


class User:
    def __init__(self, nama, gender, alamat, phone, iD):
        self._nama = nama
        self._gender = gender
        self._alamat = alamat
        self._phone = phone
        self.id = iD

    def getNama(self):
        return self._nama
    
    def setNama(self, nama):
        self._nama = nama

    def getGender(self):
        return self._gender

    def setGender(self,gender):
        self._gender = gender

    def getAlamat(self):
        return self._alamat

    def setAlamat(self, alamat):
        self._alamat = alamat

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def dataDiri(self):
        query = cursor.execute('''
                SELECT tab_teachers.nama, tab_teachers.mapel, tab_teachers.jenis_kelamin, tab_teachers.alamat, tab_teachers.phone FROM tab_teachers''')
        for row in query:
            print(f"""
                    Nama: {row[0]}
                    Bidang: {row[1]}
                    Jenis Kelamin: {row[2]}
                    Alamat: {row[3]}
                    No.HP: {row[4]}
                """)

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

    def lihatTeman(self):
        query = cursor.execute('''\
                SELECT tab_students.nama, tab_classes.nama, tab_students.jenis_kelamin, tab_students.alamat, tab_students.phone
                FROM tab_students
                INNER JOIN tab_classes
                ON tab_students.kelas = tab_classes.class_id
                ''')

        for row in query:
            print(f"""
                    Nama: {row[0]}
                    Kelas: {row[1]}
                    Jenis Kelamin: {row[2]}
                    Alamat: {row[3]}
                    No.HP: {row[4]}
                """)
