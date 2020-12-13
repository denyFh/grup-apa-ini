import sqlite3
DbName = 'db_leslesan.db'

class insiderDb:
    def __init__(self):
        self.db = sqlite3.connect(DbName)
        self.c = self.db.cursor()

    def create_table(self):
        conn = self.db
        sql = '''CREATE TABLE IF NOT EXISTS tab_teachers
            (teacher_id INTEGER PRIMARY KEY AUTOINCREMENT, NAMA TEXT NOT NULL, MAPEL TEXT NOT NULL);'''
        conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_students
            (student_id INTEGER PRIMARY KEY, NAMA TEXT NOT NULL)
        """
        conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_classes
            (class_id INTEGER PRIMARY KEY AUTOINCREMENT, NAMA TEXT NOT NULL)
        """
        conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_admins
            (admin_id INTEGER PRIMARY KEY, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)
        """
        conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_peserta_kelas
            (id INTERGER PRIMARY KEY, teacher_id INTEGER, student_id INTEGER, class_id INTEGER,
            FOREIGN KEY (teacher_id)
                REFERENCES tab_teachers (teacher_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION,
            FOREIGN KEY (student_id)
                REFERENCES tab_students (student_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION,
            FOREIGN KEY (class_id)
                REFERENCES tab_classes (class_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION)
        """
        conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tab_schedules
            (id INTEGER PRIMARY KEY, class_id INTEGER, DAY TEXT, HOURS TEXT, YEARS TEXT, 
            FOREIGN KEY (class_id)
                REFERENCES tab_classes (class_id)
                    ON DELETE CASCADE
                    ON UPDATE NO ACTION)
        """
        conn.execute(sql)

        print("Success")

    
# #-----------------FunctionCall--------------------#
#1st
a = insiderDb().create_table()
#2nd
# create_table()