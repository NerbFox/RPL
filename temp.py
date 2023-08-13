from RPL.A import *
# class` Outfit :
#     def __init__(self):
#         conn = sqlite3.connect('Dater.db')
#         cur = conn.cursor()
#         cur.execute(
#             "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Outfit'")
#         # print(cur.execute())
        
#         # if cur.fetchone()[0] == 1:
#         #     self.fetchRiwayat()
#         # else :
#         #     self.initTableRiwayat()
#         #     self.fetchRiwayat()

#     def initTableRiwayat(self):
#         # Connect to the database (or create it if it doesn't exist)
#         conn = sqlite3.connect('Dater.db')

#         # Create a cursor object
#         cur = conn.cursor()

#         cur.execute('''
#             CREATE TABLE Outfit (
#                 NamaTemplate VARCHAR(255) NOT NULL,
#                 WaktuSelesaiLatihan TIMESTAMP NOT NULL,
#                 KaloriTerbakar FLOAT(5,2),
#                 PRIMARY KEY (NamaTemplate, WaktuSelesaiLatihan),
#                 FOREIGN KEY (NamaTemplate) REFERENCES TemplateLatihan(NamaTemplate)
#                 );''')

#         conn.commit()        

#         # Close the connection and cursor to the database
#         conn.close()
    
#     def fetchRiwayat(self):
#         conn = sqlite3.connect('Dater.db')
#         cur = conn.cursor()

#         # Eksekusi query untuk membaca data dari tabel
#         cur.execute('SELECT * FROM Outfit')

#         # Mengambil semua baris hasil query menjadi sebuah list of tuple
#         ListRiwayat = cur.fetchall()

#         conn.close()
#         self.ListRiwayat = ListRiwayat

#     def insertRiwayat(self, namaTemplate, waktuSelesai, totalKalori):
#         conn = sqlite3.connect('Dater.db')
#         cur = conn.cursor()

#         # Menampung data riwayat yang ingin ditambahkan
#         new_data = [(namaTemplate, waktuSelesai, totalKalori)]

#         # Memasukkan data baru ke dalam list of tuple yang sudah ada
#         self.ListRiwayat += new_data

#         # Memasukkan data ke dalam tabel
#         cur.executemany('INSERT INTO Outfit VALUES (?, ?, ?)', new_data)

#         conn.commit()
#         cur.close()
#         conn.close()

#     def getRiwayat(self):
#         return self.ListRiwayat
    
#     # I.S. ListRiwayat sudah berisi
#     def getRecordRiwayat(self, idx):
#          if idx <= len(self.ListRiwayat):
#             return self.ListRiwayat[idx-1]
         
#     def deleteTemplate(self):
#         return 0
        
# if __name__ == '__main__' :
#     template = Outfit()

#     # template.insert("latihan pertama", datetime.datetime.now(), 232.1)
#     # template.insert("latihan kedua", datetime.datetime.now(), 453.6)
#     # template.insert("latihan ketiga", datetime.datetime.now(), 476.9)
#     # template.insert("latihan keempat", datetime.datetime.now(), 6565.34)
#     # template.insert("latihan kelima", datetime.datetime.now(), 6565.34)
#     # template.insert("latihan kesepuluh", datetime.datetime.now(), 6565.34)

#     print(template.ListRiwayat)
#     # print()
#     # print(len(template.ListRiwayat))
#     # print()
#     # print(template.getRiwayat())
#     # print()
#     # print(template.getRecordRiwayat(5))
#     # print(template.getRecordRiwayat(2))
#     # print(template.getRecordRiwayat(10))`