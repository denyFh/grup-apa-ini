import sqlite3
from Admin import Admin
from Classes import Classes
from Schedule import Schedule
from Student import Student
from Teacher import Teacher

DbName = 'db_leslesan.db'


class insiderDb:
    def __init__(self):
        self.db = sqlite3.connect(DbName)
        self.c = self.db.cursor()

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS tab_teachers
            (teacher_id INTEGER PRIMARY KEY AUTOINCREMENT, NAMA TEXT NOT NULL, JENIS_KELAMIN TEXT NOT NULL, MAPEL TEXT NOT NULL, ALAMAT TEXT, PHONE TEXT)
        """
        self.c.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_students
            (student_id INTEGER PRIMARY KEY AUTOINCREMENT, NAMA TEXT NOT NULL, KELAS INTEGER NOT NULL, JENIS_KELAMIN TEXT NOT NULL, ALAMAT TEXT, PHONE TEXT,
            FOREIGN KEY (KELAS)
                REFERENCES tab_classes (class_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION)
        """
        self.c.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_classes
            (class_id INTEGER PRIMARY KEY AUTOINCREMENT, NAMA TEXT NOT NULL)
        """
        self.c.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_admins
            (admin_id INTEGER PRIMARY KEY, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)
        """
        self.c.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_schedules
            (id INTEGER PRIMARY KEY AUTOINCREMENT, class_id INTEGER NOT NULL, teacher_id INTEGER NOT NULL, DAY TEXT NOT NULL, DATE TEXT NOT NULL, TIME TEXT NOT NULL, NOTE TEXT,
            FOREIGN KEY (class_id)
                REFERENCES tab_classes (class_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION,
            FOREIGN KEY (teacher_id)
                REFERENCES tab_teacher (teacher_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION)
        """
        self.c.execute(sql)
        print("Success")

    def insert_admin(self):
        adminlist = [
            Admin("chintaalya_", "6Chint@6"),
            Admin("denFy", "xLut8EHJ"),
            Admin("dnxhill", "monyet")
        ]
        for adm in adminlist:
            tempo = self.c.execute(
                "select * from tab_admins where username = ?", (adm.getUsername(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_admins (username,password) values (?,?)", (adm.getUsername(), adm.getPassword()))
                self.db.commit()

    def insert_class(self):
        classlist = [
            Classes("A"),
            Classes("B"),
            Classes("C")
        ]
        for cl in classlist:
            tempo = self.c.execute(
                "select * from tab_classes where nama = ?", (cl.getClassName(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_classes (nama) values (?)", (cl.getClassName()))
                self.db.commit()

    def insert_schedule(self):
        schedulelist = [
            Schedule(1, 1,
                         11001, "SENIN", "21/12/2020", "15.00 s/d 17.00", "-"),
            Schedule(2, 1,
                         11002, "SENIN", "21/12/2020", "19.00 s/d 21.00", "-"),
            Schedule(3, 2,
                         11003, "SELASA", "22/12/2020", "15.00 s/d 17.00", "-"),
            Schedule(4, 2,
                         11004, "SELASA", "22/12/2020", "19.00 s/d 21.00", "-"),
            Schedule(5, 3,
                         11006, "RABU", "23/12/2020", "15.00 s/d 17.00", "-"),
            Schedule(6, 3,
                         11003, "RABU", "23/12/2020", "19.00 s/d 21.00", "-"),
            Schedule(7, 1,
                         11002, "KAMIS", "24/12/2020", "12.00 s/d 14.00", "-"),
            Schedule(8, 2,
                         11005, "KAMIS", "24/12/2020", "15.00 s/d 17.00", "-"),
            Schedule(9, 3,
                         11004, "KAMIS", "24/12/2020", "19.00 s/d 21.00", "-")
        ]
        for sch in schedulelist:
            tempo = self.c.execute(
                "select * from tab_schedules where id = ?", (sch.getiD(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_schedules (class_id, teacher_id, day, date, time, note) values (?,?,?,?,?,?)", (sch.getKelas(), sch.getGuru(), sch.getHari(), sch.getTanggal(), sch.getWaktu(), sch.getNote()))
        self.db.commit()

    def insert_student(self):
        self.c.execute("delete from tab_students where student_id = '1'")
        # self.c.execute("INSERT INTO tab_students VALUES (1,'a',1,'b','c','d')")
        studentlist = [
            Student("Abyaz Dzaki Habbab", "Laki-Laki",
                        "Jln. Dahlia", "082638927362", 1, 19061001),
            Student("Almira Nur Ainunisa", "Perempuan",
                        "Jln. Matahari", "087453678290", 2, 19061002),
            Student("Baslan Izzam", "Laki-Laki",
                        "Jln. Melati", "087369026718", 3, 19061003),
            Student("Erza Kaila Auristela", "Perempuan",
                        "Jln. Bugenville", "082748930277", 1, 19061004),
            Student("Freya Ayudia", "Perempuan",
                        "Jln. Kenanga", "082674890372", 2, 19061005),
            Student("Fidelya Naura Cantika", "Perempuan",
                        "Jln. Teratai", "088904678930", 3, 19061006),
            Student("Meisie Khansa", "Perempuan",
                        "Jln. Daisy", "0826389264783", 1, 19061007),
            Student("Muhammad Gibran Fadl", "Laki-Laki",
                        "Jln. Mawar", "087489372638", 2, 19061008),
            Student("Naila Zanna Kirania", "Perempuan",
                        "Jln. Anggrek", "089456378927", 3, 19061009),
            Student("Rafka Shawqi", "Laki-Laki",
                        "Jln. Dandelion", "082647893028", 1, 190610010)
        ]
        for sl in studentlist:
            tempo = self.c.execute(
                "select * from tab_students where nama = ?", (sl.getNama(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)", (sl.getNama(), sl.getKelas(), sl.getGender(), sl.getAlamat(), sl.getPhone()))
        self.db.commit()

    def insert_teacher(self):
        teacherlist = [
            Teacher("Afsana Chinta Putri", "Perempuan",
                        "Jln. Pisang", "082331550064", "Matematika", 11001),
            Teacher("Aksa Camilla", "Perempuan",
                        "Jln. Rambutan", "087352789026", "Biologi", 11002),
            Teacher("Ezra Fakhri Firdaus", "Laki-Laki",
                        "Jln. Pepaya", "088364920273", "Kimia", 11003),
            Teacher("Fiza Kurniawan", "Laki-Laki",
                        "Jln. Jambu", "089357628368", "Fisika", 11004),
            Teacher("Hafizhah Inayah Kanza", "Perempuan",
                        "Jln. Mangga", "087354826353", "Bahasa Indonesia", 11005),
            Teacher("Deny Efendy Gaaziy", "Laki-Laki",
                        "Jln. Kelengkeng", "089364789362", "Bahasa Inggris", 11006)
        ]
        for tl in teacherlist:
            tempo = self.c.execute(
                "select * from tab_teachers where NAMA = ?", (tl.getNama(),))
            if tempo.fetchone() is None:
                self.c.execute("insert into tab_teachers (NAMA, JENIS_KELAMIN, MAPEL, PHONE, ALAMAT) values (?,?,?,?,?)", (
                    tl.getNama(), tl.getGender(), tl.getMapel(), tl.getPhone(), tl.getAlamat()))
        self.db.commit()
    def update_teacher(self):
        # self.c.execute(
        #     "update 'sqlite_sequence' set 'seq' = 11000 where name = 'tab_teachers'")
        self.db.commit()
    def update_student(self):
        # self.c.execute(
        #     "update 'sqlite_sequence' set 'seq' = 19061000 where name = 'tab_students'")
        self.db.commit()
    def drop_admin(self):
        self.c.execute("drop table tab_admins")
        self.db.commit()
    def drop_classes(self):
        self.c.execute("drop table tab_classes")
        self.db.commit()
    def drop_schedule(self):
        self.c.execute("drop table tab_schedules")
        self.db.commit()
    def drop_student(self):
        self.c.execute("drop table tab_students")
        self.db.commit()
    def drop_teacher(self):
        self.c.execute("drop table tab_teachers")
        self.db.commit()
    def close(self):
        self.db.close()


# #-----------------FunctionCall--------------------#
# insiderDb().create_table()
# insiderDb().insert_teacher()
# insiderDb().insert_class()
# insiderDb().insert_student()
# insiderDb().insert_admin()
# insiderDb().insert_schedule()
# insiderDb().update_teacher()
# insiderDb().update_student()
# insiderDb().drop_teacher()
# insiderDb().drop_admin()
# insiderDb().drop_student()
# insiderDb().drop_schedule()
# insiderDb().drop_classes()
# insiderDb().close()

# hapusrow
# conn.execute("delete from teacher where iD = '6'")
# conn.commit()
