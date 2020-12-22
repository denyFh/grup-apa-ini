import sqlite3
from connector import Connect
from Person import Person
from Student import Student
from Teacher import Teacher
from Admin import Admin
from Schedule import Schedule


class Display:
    guestID = None

    def __init__(self):
        pass

    def Home(self):
        global objek
        check = []
        print("""
=============================================
|||||||||| WELCOME TO TADIKA MESRA ||||||||||
=============================================
(ketik (-exit) untuk keluar dari program)
""")
        Display.guestID = input("Masukkan ID : ")
        self.id = Display.guestID
        if Display.guestID.isdigit():
            Display.guestID = int(Display.guestID)

        query = Connect().c.execute(
            "SELECT * FROM tab_admins WHERE password=?", (Display.guestID,))
        for row in query:
            check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                objek = Admin(row[1], row[2], Display.guestID)
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
            query = Connect().c.execute(
                "SELECT * FROM tab_students WHERE student_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                objek = Student(row[1], row[2], row[3], row[4], row[5], Display.guestID)
                print(
                    "\n- Selamat datang, {} ({}) -".format(self.status[1], self.status[0]))
                Display.menuSiswa(self)
            else:
                print("\nID tidak terdaftar, hubungi administrator")
                input("(Press Enter to Continue...)\n")
                check = []
                Display.Home(self)
        elif len(str(Display.guestID)) == 5:
            query = Connect().c.execute(
                "SELECT * FROM tab_teachers WHERE teacher_id=?", (Display.guestID,))
            for row in query:
                check.append(row)
            if len(check) > 0:
                self.status = [self.role(Display.guestID), check[0][1]]
                objek = Teacher(row[1], row[2], row[3], row[4],row[5], Display.guestID)
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
[5] Tampilkan Menu
=============================================""")
        self.cekMenu = "0"
        while self.cekMenu != "-1":
            self.cekMenu = input("(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
            if self.cekMenu == "1":
                Student.dataDiri(self)
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "2":
                Person.dataDiri(self)
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
                    Person.lihatJadwal(self)
                elif a == "b":
                    Student.lihatJadwal(self)
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
                    Student.lihatTeman(self)
                elif a == "b":
                    Person.lihatTeman(self)
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
[5] Tampilkan Menu
=============================================""")
        self.cekMenu = "0"
        while self.cekMenu != "-1":
            self.cekMenu = input("(ketik (-menu) untuk melihat menu dan (-exit) untuk keluar dari program)\nMasukkan Menu : ")
            if self.cekMenu == "1":
                Teacher.dataDiri(self)
                input("(Press Enter to Continue...)\n")
            elif self.cekMenu == "2":
                Person.lihatTeman(self)
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
                    Person.lihatJadwal(self)
                elif a == "b":
                    Teacher.lihatJadwal(self)
                    a = input("Edit catatan? (ketik 'y' jika iya) ")
                    if a == "y":
                        jadwal = input("Masukkan ID Jadwal: ")
                        note = input("Masukkan catatan: ")
                        query = "UPDATE tab_schedules set NOTE = ? WHERE id = ? ", (note, jadwal,)
                        Connect().c.execute(query)
                        Connect().db.commit()
                    else:
                        continue
                else:
                    print("\n============ Menu Tidak Tersedia ============\n")
                input("(Press Enter to Continue...)\n")
#             elif self.cekMenu == "4":
#                 a = input("""
# =============================================
# Silahkan pilih menu yang anda inginkan:
# [a] Lihat Daftar Teman Sekelas
# [b] Lihat Daftar Semua Teman
# =============================================
# Masukkan pilihan >> """)
#                 if a == "a":
#                     Student.lihatTeman(self)
#                 elif a == "b":
#                     Person.lihatTeman(self)
#                 else:
#                     print("\n============ Menu Tidak Tersedia ============\n")
#                 input("(Press Enter to Continue...)\n")
#             elif self.cekMenu == "-menu":
#                 Display.menuSiswa(self)
#             elif self.cekMenu == "-exit":
#                 Display.exit(self)
#             else:
#                 input("============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")

    def menuAdmin(self):
        Display.Home(self)

    def exit(self):
        print("""
============= SEE YOU NEXT TIME =============
""")
        Connect().db.close()
        exit()


Display().Home()
