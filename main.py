import sqlite3
from Student import Student
from Teacher import Teacher
from Admin import Admin
import os

DbName = 'db_leslesan.db'


class Display:
    def __init__(self, guestID=None):
        self.conn = sqlite3.connect(DbName)
        self.cursor = self.conn.cursor()
        self.guestID = guestID

    def clear(self):
        os.system('cls')

    @property
    def setguestID(self):
        pass

    @setguestID.setter
    def setguestID(self, value):
        self.guestID = value

    def Login(self):
        self.clear()
        global admin
        global siswa
        global guru
        print("""=============================================
           WELCOME TO TADIKA MESRA           
=============================================
(ketik (-exit) untuk keluar dari program)
""")
        self.setguestID = input("Masukkan ID : ")
        if self.guestID.isdigit():
            self.guestID = int(self.guestID)
            
        data = []
        query = self.cursor.execute(
            "SELECT * FROM tab_admins WHERE password=?", (self.guestID,))
        for row in query:
            data.append(row)
        if len(data) > 0:
            admin = Admin(data[0][1], data[0][2], data[0][0])
            self.menuAdmin()
        else:
            if self.guestID == "-exit":
                self.exit()
            elif len(str(self.guestID)) == 8:
                query = self.cursor.execute(
                    "SELECT * FROM tab_students WHERE student_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    siswa = Student(
                        data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][0])
                    self.menuSiswa()
                else:
                    print("\nID tidak terdaftar, hubungi administrator")
                    input("(Press Enter to Continue...)\n")
                    self.Login()
            elif len(str(self.guestID)) == 5:
                query = self.cursor.execute(
                    "SELECT * FROM tab_teachers WHERE teacher_id=?", (self.guestID,))
                for row in query:
                    data.append(row)
                if len(data) > 0:
                    guru = Teacher(data[0][1], data[0][2], data[0]
                                   [3], data[0][4], data[0][5], data[0][0])
                    self.menuGuru()
                else:
                    print("\nID tidak terdaftar, hubungi administrator")
                    input("(Press Enter to Continue...)\n")
                    self.Login()
            else:
                print("\nID tidak terdaftar, hubungi administrator")
                input("(Press Enter to Continue...)\n")
                self.Login()

    def role(self, x):
        if type(x) == str:
            return "Admin"
        elif type(x) == int:
            if len(str(x)) == 8:
                return "Siswa"
            elif len(str(x)) == 5:
                return "Guru"

    def menuSiswa(self):
        self.clear()
        print(f"""Hello {siswa.getNama()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Lihat Data Diri
[2] Lihat Jadwal
[3] Lihat Data Pengajar
=============================================
(ketik (-exit) untuk keluar dari program)""")
        self.cekMenu = input("Masukkan Menu : ")
        while self.cekMenu != "-exit":
            if self.cekMenu == "1":
                self.clear()
                siswa.dataDiri()
                input("(Press Enter to Continue...)")
                self.menuSiswa()
            elif self.cekMenu == "2":
                self.clear()
                siswa.lihatJadwal()
                input("(Press Enter to Continue...)")
                self.menuSiswa()
            elif self.cekMenu == "3":
                self.clear()
                siswa.lihatPengajar()
                input("(Press Enter to Continue...)")
                self.menuSiswa()
            else:
                input("\n============ Menu Tidak Tersedia ============\n\n(Press Enter to Continue...)")
                self.menuSiswa()
        else:
            self.exit()

    def menuGuru(self):
        self.clear()
        print(f"""Hello {guru.getNama()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Lihat Data Diri
[2] Lihat Data Kelas
[3] Lihat Jadwal
=============================================
(ketik (-exit) untuk keluar dari program)""")
        self.cekMenu = input("Masukkan Menu : ")
        while self.cekMenu != "-exit":
            if self.cekMenu == "1":
                self.clear()
                guru.dataDiri()
                input("(Press Enter to Continue...)")
                self.menuGuru()
            elif self.cekMenu == "2":
                self.clear()
                guru.lihatKelas()
                input("(Press Enter to Continue...)")
                self.menuGuru()
            elif self.cekMenu == "3":
                self.clear()
                guru.lihatJadwal()
                input("(Press Enter to Continue...)")
                self.menuGuru()
            else:
                input("\n============ Menu Tidak Tersedia ============\n\n(Press Enter to Continue...)")
                self.menuGuru()
        else:
            self.exit()

    def menuAdmin(self):
        self.clear()
        print(f"""Hello {admin.getUsername()}! ({self.role(self.guestID)})
=============================================
                    MENU                     
=============================================
Silahkan pilih menu yang anda inginkan:
[1] Data Diri
[2] Data Kelas
[3] Data Guru
[4] Jadwal
=============================================
(ketik (-exit) untuk keluar dari program)""")
        self.cekMenu = input("Masukkan Menu : ")
        while self.cekMenu != "-exit":
            if self.cekMenu == "1":
                self.clear()
                print(admin.detail())
                a = input("Edit data diri? (ketik 'y' jika iya) ")
                if a == "y":
                    self.clear()
                    print(admin.editDataDiri())
                else:
                    pass
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "2":
                self.clear()
                print(admin.mengelolaKelas())
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "3":
                self.clear()
                print(admin.mengelolaGuru())
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            elif self.cekMenu == "4":
                self.clear()
                print(admin.mengelolaJadwal())
                input("(Press Enter to Continue...)\n")
                self.menuAdmin()
            else:
                input(
                    "============ Menu Tidak Tersedia ============\n(Press Enter to Continue...)\n")
                self.menuAdmin()    
        else:
            self.exit()

    def exit(self):
        print("""
============= SEE YOU NEXT TIME =============
""")
        self.conn.close()
        exit()


start = Display()
start.Login()
