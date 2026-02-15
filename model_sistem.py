# File: model_sistem.py
# Deskripsi: Modul definisi kelas untuk Sistem Perpustakaan

class Buku:
    def __init__(self, judul, penulis, isbn):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.status = "Tersedia"

    def update_status(self, status_baru):
         self.status = status_baru

class Anggota:
    def __init__(self, id_anggota, nama, alamat):
      self.id_anggota = id_anggota
      self.nama = nama 
      self.alamat = alamat
      self.jumlah_buku = 0

class Petugas:
    def __init__(self, id_petugas, nama, shift):
      self.id_petugas = id_petugas
      self.nama = nama
      self.shift = shift

    def buat_laporan(self):
         print(f"[laporan] Petugas {self.nama} telah memvalidasi data hari ini. ")

class Peminjaman:
    def __init__(self, id_transaksi, anggota, buku, tgl_peminjaman):
      self.id_transaksi = id_transaksi 
      self.anggota = anggota
      self.buku = buku
      self.tgl_pinjam = tgl_peminjaman

    def proses_pinjam(self):
      if self.buku.status == "Tersedia":
            self.buku.status = "Dipinjam"
            self.anggota.jumlah_buku += 1
            print(f"Transaksi {self.id_transaksi}: {self.anggota.nama} meminjam {self.buku.judul}")

class Pengembalian:
    def __init__(self, id_kembali, peminjaman, tgl_kembali):
        self.id_kembali = id_kembali
        self.peminjaman = peminjaman
        self.tgl_kembali = tgl_kembali

    def proses_kembali(self):
        self.peminjaman.buku.status = "Tersedia"
        self.peminjaman.anggota.jumlah_buku -= 1
        print(f"Pengembalian {self.id_kembali}: {self.peminjaman.buku.judul} telah kembali.")    

