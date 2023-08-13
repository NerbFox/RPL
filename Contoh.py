import datetime
import sqlite3

# this is inside Dater.db
# CREATE TABLE Outfit (
#     OID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#     UID INT(5) NOT NULL,
#     nama VARCHAR(30) NOT NULL,
#     kategori VARCHAR(15) NOT NULL,
#     label VARCHAR(10),
#     gambar BLOB,
#     FOREIGN KEY (UID) REFERENCES Profil(UID)
# );

# CREATE TABLE Jadwal (
#     JID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#     UID INT(5) NOT NULL,
#     waktu DATETIME NOT NULL,
#     tempat VARCHAR(20) NOT NULL,
#     status BOOL NOT NULL,
#     rating NUMERIC(2,1) CHECK (rating >= 0 AND rating <= 5),
#     FOREIGN KEY (UID) REFERENCES Profil(UID)
# );

# CREATE TABLE Pemakaian (
#     JID INT(5) NOT NULL,
#     OID INT(5) NOT NULL,
#     PRIMARY KEY (JID, OID),
#     FOREIGN KEY (JID) REFERENCES Jadwal(JID),
#     FOREIGN KEY (OID) REFERENCES Outfit(OID)
# );

# CREATE TABLE Profil (
#     UID INT(5) NOT NULL PRIMARY KEY, 
#     nama_lengkap VARCHAR(30) NOT NULL,
#     nama_panggilan VARCHAR(30),
#     tanggal_lahir DATE NOT NULL,
#     jenis_kelamin VARCHAR(1),
#     foto VARCHAR(100),
#     deskripsi_tambahan VARCHAR(100)
# );

print("Hello World")
# Connect to the database
connection = sqlite3.connect('DaterApp.db')
cursor = connection.cursor()
#  check for each table if table is not exist then create it
def create_table():
    connection.execute("""CREATE TABLE IF NOT EXISTS Profil (
        UID INTEGER NOT NULL PRIMARY KEY, 
        nama_lengkap VARCHAR(30) NOT NULL,
        nama_panggilan VARCHAR(30),
        tanggal_lahir DATE NOT NULL,
        jenis_kelamin VARCHAR(1),
        foto VARCHAR(100),
        deskripsi_tambahan VARCHAR(100));""")
    connection.execute("""CREATE TABLE IF NOT EXISTS Outfit (
        OID INTEGER PRIMARY KEY AUTOINCREMENT, 
        UID INT(5) NOT NULL,
        nama VARCHAR(30) NOT NULL,
        kategori VARCHAR(15) NOT NULL,
        label VARCHAR(10),
        gambar BLOB,
        FOREIGN KEY (UID) REFERENCES Profil(UID));""")
    connection.execute("""CREATE TABLE IF NOT EXISTS Jadwal (
        JID INTEGER PRIMARY KEY AUTOINCREMENT, 
        UID INT(5) NOT NULL,
        waktu DATETIME NOT NULL,
        tempat VARCHAR(20) NOT NULL,
        status BOOL NOT NULL,
        rating NUMERIC(2,1) CHECK (rating >= 0 AND rating <= 5),
        FOREIGN KEY (UID) REFERENCES Profil(UID));""")
    connection.execute("""CREATE TABLE IF NOT EXISTS Pemakaian (
        JID INT(5) NOT NULL,
        OID INT(5) NOT NULL,
        PRIMARY KEY (JID, OID),
        FOREIGN KEY (JID) REFERENCES Jadwal(JID),
        FOREIGN KEY (OID) REFERENCES Outfit(OID));""")
    connection.commit()

# def reset():
    # connection.execute("""DROP TABLE profil;""")
    # connection.execute("""DROP TABLE Outfit;""")
    # connection.execute("""DROP TABLE Jadwal;""")
    # connection.execute("""DROP TABLE Pemakaian;""")    

# insert to profil
# connection.execute("""INSERT INTO Profil (nama_lengkap, nama_panggilan, tanggal_lahir) VALUES ('Ubi', 'Nigel', '1999-01-01');""")
#  insert to outfit
# connection.execute("""INSERT INTO Outfit (UID, nama, kategori, label) VALUES (1, 'Outfit Baru', 'Atasan', 'Label Baru');""")
# connection.commit()


# reset()
create_table()
A = connection.execute("SELECT * FROM Profil;")
B = connection.execute("SELECT * FROM Outfit;")
print(A.fetchall())
print(B.fetchall())

# Close the database connection
connection.close()