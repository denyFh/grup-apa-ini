import sqlite3
import method as morphs

databaseName = 'db_leslesan.db'
conn = sqlite3.connect(databaseName)


class Display:
    guestID = None

    def __init__(self):
        pass

    def Home(self):
            print("""
            
            \t------------------------HOME-----------------------""")
            Display.guestID = input("\t\tMasukkan ID : ")
            if len(Display.guestID) == 8:
                Display.menuSiswa(self)

    def menuSiswa(self):
        status = ["Siswa", Display.guestID]
        print("""
                -----------Selamat datang, {} {}-----------
                Silahkan pilih menu yang anda inginkan (1-3):
                1. Lihat Jadwal
                2. Lihat Data Siswa
                3. Lihat Data Pengajar
                4. Logout
                ----------------------------------------------------""".format(status[0], status[1]))
        cekMenu = "0"
        while cekMenu is not "4":
            cekMenu = input("\t\tMasukkan Menu : ")
            if cekMenu == '1':
                morphs.Student().lihatJadwal()
            elif cekMenu == '2':
                morphs.Person().lihatdata()
            elif cekMenu == '3':
                morphs.Person().lihatdata()
            elif cekMenu == '4':
                Display.exit(self)
            else:
                print("Menu tidak tersedia")
            

    def exit(self):
        print("""
            \t---------------------Terima Kasih--------------------""")
        conn.close()

a = Display().Home()
