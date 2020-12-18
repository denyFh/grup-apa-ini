import rule as oop
import sqlite3
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
            (id TEXT PRIMARY KEY NOT NULL, class_id INTEGER NOT NULL, teacher_id INTEGER NOT NULL, DAY TEXT NOT NULL, DATE TEXT NOT NULL, TIME TEXT NOT NULL, NOTE TEXT,
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
            oop.Admin("chintaalya_", "6Chint@6"),
            oop.Admin("denFy", "xLut8EHJ"),
            oop.Admin("dnxhill", "monyet")
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
            oop.Classes("A"),
            oop.Classes("B"),
            oop.Classes("C")
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
            oop.Schedule("S01", 1,
                         1, "SENIN", "21/12/2020", "15.00 s/d 17.00", "-"),
            oop.Schedule("S02", 1,
                         2, "SENIN", "21/12/2020", "19.00 s/d 21.00", "-"),
            oop.Schedule("S03", 2,
                         3, "SELASA", "22/12/2020", "15.00 s/d 17.00", "-"),
            oop.Schedule("S04", 2,
                         4, "SELASA", "22/12/2020", "19.00 s/d 21.00", "-"),
            oop.Schedule("S05", 3,
                         6, "RABU", "23/12/2020", "15.00 s/d 17.00", "-"),
            oop.Schedule("S06", 3,
                         3, "RABU", "23/12/2020", "19.00 s/d 21.00", "-"),
            oop.Schedule("S07", 1,
                         2, "KAMIS", "24/12/2020", "12.00 s/d 14.00", "-"),
            oop.Schedule("S08", 2,
                         5, "KAMIS", "24/12/2020", "15.00 s/d 17.00", "-"),
            oop.Schedule("S09", 3,
                         4, "KAMIS", "24/12/2020", "19.00 s/d 21.00", "-")
        ]
        for sch in schedulelist:
            tempo = self.c.execute(
                "select * from tab_schedules where id = ?", (sch.getiD(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_schedules (id, class_id, teacher_id, day, date, time, note) values (?,?,?,?,?,?,?)", (sch.getiD(), sch.getKelas(), sch.getGuru(), sch.getHari(), sch.getTanggal(), sch.getWaktu(), sch.getNote()))
        self.db.commit()

    def insert_student(self):
        self.c.execute("delete from tab_students where student_id = '1'")
        # self.c.execute("INSERT INTO tab_students VALUES (1,'a',1,'b','c','d')")
        studentlist = [
            oop.Student("Abyaz Dzaki Habbab", "Laki-Laki",
                        "Jln. Dahlia", "082638927362", 1),
            oop.Student("Almira Nur Ainunisa", "Perempuan",
                        "Jln. Matahari", "087453678290", 2),
            oop.Student("Baslan Izzam", "Laki-Laki",
                        "Jln. Melati", "087369026718", 3),
            oop.Student("Erza Kaila Auristela", "Perempuan",
                        "Jln. Bugenville", "082748930277", 1),
            oop.Student("Freya Ayudia", "Perempuan",
                        "Jln. Kenanga", "082674890372", 2),
            oop.Student("Fidelya Naura Cantika", "Perempuan",
                        "Jln. Teratai", "088904678930", 3),
            oop.Student("Meisie Khansa", "Perempuan",
                        "Jln. Daisy", "0826389264783", 1),
            oop.Student("Muhammad Gibran Fadl", "Laki-Laki",
                        "Jln. Mawar", "087489372638", 2),
            oop.Student("Naila Zanna Kirania", "Perempuan",
                        "Jln. Anggrek", "089456378927", 3),
            oop.Student("Rafka Shawqi", "Laki-Laki",
                        "Jln. Dandelion", "082647893028", 1)
        ]
        for sl in studentlist:
            tempo = self.c.execute(
                "select * from tab_students where nama = ?", (sl.getNama(),))
            if tempo.fetchone() is None:
                self.c.execute(
                    "insert into tab_students (NAMA, KELAS, JENIS_KELAMIN, ALAMAT, PHONE) values (?,?,?,?,?)", (sl.getNama(), sl.getKelas(), sl.getGender(), sl.getAlamat(), sl.getPhone()))
        self.db.commit()

    def update_student(self):
        self.c.execute(
            "update 'sqlite_sequence' set 'seq' = 19061000 where name = 'tab_students'")
        self.db.commit()

    def insert_teacher(self):
        # self.c.execute("INSERT INTO tab_teachers VALUES (1,'a','b','c','d','e')")
        teacherlist = [
            oop.Teacher("Afsana Chinta Putri", "Perempuan",
                        "Jln. Pisang", "082331550064", "Matematika"),
            oop.Teacher("Aksa Camilla", "Perempuan",
                        "Jln. Rambutan", "087352789026", "Biologi"),
            oop.Teacher("Ezra Fakhri Firdaus", "Laki-Laki",
                        "Jln. Pepaya", "088364920273", "Kimia"),
            oop.Teacher("Fiza Kurniawan", "Laki-Laki",
                        "Jln. Jambu", "089357628368", "Fisika"),
            oop.Teacher("Hafizhah Inayah Kanza", "Perempuan",
                        "Jln. Mangga", "087354826353", "Bahasa Indonesia"),
            oop.Teacher("Deny Efendy Gaaziy", "Laki-Laki",
                        "Jln. Kelengkeng", "089364789362", "Bahasa Inggris")
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
    def drop(self):
        self.c.execute("drop table tab_schedules")
        self.db.commit()
    def close(self):
        self.db.close()


# #-----------------FunctionCall--------------------#
a = insiderDb().create_table()
# b = insiderDb().insert_teacher()
# c = insiderDb().update_teacher()
# d = insiderDb().insert_class()
# e = insiderDb().insert_student()
# f = insiderDb().insert_admin()
g = insiderDb().insert_schedule()
# h = insiderDb().update_admin()
# i = insiderDb().update_student()
# j = insiderDb().update_schedule()
# k = insiderDb().update_classes()
# l = insiderDb().close()
# m = insiderDb().drop()
