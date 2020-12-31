import sqlite3
DbName = 'db_leslesan.db'
conn = sqlite3.connect(DbName)
cursor = conn.cursor()
class Admin:
    def __init__(self, username, password, iD):
        self.__username = username
        self.__password = password
        self.id = iD

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
    def setUsername(self, value):
        self.__username = value
    def setPassword(self, value):
        self.__password = value    
    def detail(self):
        password = len(Admin.getPassword(self))*"*"
        return (f"""=============================================
                 DATA DIRI                   
=============================================
Username = {Admin.getUsername(self)}
Password = {password}
""")

    def editUsername(self):
        username = input("Masukkan username: ")
        tempo = cursor.execute(
            "select * from tab_admins where username = ?", (username,))
        if tempo.fetchone() is None:
            self.setUsername(username)
            cursor.execute("UPDATE tab_admins set USERNAME = ? WHERE password = ?", (
            self.getUsername(), self.getPassword()))
            conn.commit()
        else:
            print(
                "Username sudah digunakan, silahkan gunakan username lain")

    def editPassword(self):
        pass
    
    def lihatKelas(self):
        kelas = []
        query = cursor.execute("SELECT * FROM tab_classes")
        for row in query:
            print(f"""[{row[0]}] {row[1]}""")
            kelas.append(row[1])
        getdetail = input(
            "Masukkan nama kelas untuk melihat detail >> ")
        sql = cursor.execute(
            "SELECT * FROM tab_classes WHERE NAMA = ?", (getdetail,))
        for row in sql:
            idkelas = row[0]
        if getdetail in kelas:
            query = cursor.execute(
                "SELECT * FROM tab_students WHERE kelas = ?", (idkelas,))
            for row in query:
                print(f"""
ID: {row[0]}
Nama: {row[1]}
Jenis Kelamin: {row[3]}
Alamat: {row[4]}
No.HP: {row[5]}
""")
        else:
            print(">> Kelas tidak terdaftar")

    def tambahKelas(self):
        nama = input("Masukkan nama kelas >> ")
        kelas = Classes(nama) #<-problem, harus nge import class lain
        tempo = self.cursor.execute(
            "select * from tab_classes where nama = ?", (kelas.getClassName(),))
        if tempo.fetchone() is None:
            self.cursor.execute(
                "insert into tab_classes (nama) values (?)", (kelas.getClassName()))
            self.conn.commit()
            print(">> Kelas berhasil ditambahkan")
        else:
            print(">> Nama kelas sudah terdaftar")

    def hapusGuru(self):
        d = input("ingin menghapus data? ketik 'y' jika iya ")
        if d == "y":
            inpId = input("Masukkan id guru yang ingin dihapus ")
            temp = cursor.execute(
                "select * from tab_teachers where teacher_id = ?", (inpId,))
            if temp.fetchone() is None:
                print(">> Guru tidak ada")
            else:
                cursor.execute(
                    "delete from tab_teachers where teacher_id = ?", (inpId,))
                conn.commit()
                print(">> Guru telah dihapus")
        else:
            pass

    def hapusJadwal(self):
        e = input("Ingin menghapus jadwal? ketik 'y' jika iya ")
        if e == "y":
            f = input("Pada Hari apa jadwal tersebut? >> ").upper()
            temp = cursor.execute(
                "select * from tab_schedules where DAY = ?", (f,))
            if temp.fetchone() is None:
                print(">> Jadwal tidak ada")
            else:
                tempf = cursor.execute(
                    "select * from tab_schedules where DAY = ?", (f,))
                for row in tempf:
                    print(f"""
        ID Jadwal : {row[0]}
        ID Kelas : {row[1]}
        ID Guru : {row[2]}
        Hari : {row[3]}
        Tanggal : {row[4]}
        Waktu : {row[5]}
        Catatan : {row[6]}
                    """)
                jid = input(
                    "Masukkan ID Jadwal yang ingin dihapus >> ")
                tempjid = cursor.execute(
                    "select * from tab_schedules where id = ?", (jid,))
                if tempjid.fetchone() is None:
                    print(">> ID Jadwal tidak ditemukan")
                else:
                    cursor.execute(
                        "delete from tab_schedules where id = ?", (jid,))
                    conn.commit()
                    print(">> Jadwal telah dihapus")
        else:
            pass