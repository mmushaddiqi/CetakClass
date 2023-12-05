'''
Buatlah sebuah class anggota keluarga dengan atribut/properti sebagai berikut:
Nama
Peran, misal: Ayah/Ibu/Anak
Jenis kelamin
Usia
Gunakan class tersebut untuk membuat dua buah object
'''

class anggotaKeluarga:
    def __init__(self,nama,peran,jk,usia):
        self.nama = nama
        self.peran = peran
        self.jk = jk
        self.usia = usia
        
    