# File: jalankan_perpus.py
# Modul utama untuk menjalankan simulasi sistem perpustakaan
from model_sistem import Buku, Anggota, Petugas, Peminjaman, Pengembalian

# 1. Inisialisasi Data Petugas
# Mendefinisikan petugas yang bertanggung jawab pada shift terkait
petugas_piket = Petugas("P01", "Fika", "Pagi")
petugas_piket.buat_laporan()

# 2. Inisialisasi Data Buku
# Menambahkan koleksi buku ke dalam sistem
buku_rakyat1 = Buku("Malin Kundang", "Cerita Rakyat", "978-001")
buku_rakyat2 = Buku("Timun Mas", "Cerita Rakyat", "978-002")

# 3. Registrasi Anggota
# Membuat data mahasiswa sebagai entitas peminjam
data_mhs = Anggota("125501", "Fitri Khairani Sitorus", "Pekanbaru")

# Menampilkan status awal sebelum transaksi dilakukan
print(f"Kondisi Awal: Buku {buku_rakyat2.judul} adalah {buku_rakyat2.status}")

# 4. Eksekusi Peminjaman
print("Memulai Proses Peminjaman...")
transaksi_pinjam = Peminjaman("TRX-001", data_mhs, buku_rakyat2, "15-02-2026")
transaksi_pinjam.proses_pinjam()

# 5. Eksekusi Pengembalian
print("Memulai Proses Pengembalian...")
transaksi_balik = Pengembalian("RET-001", transaksi_pinjam, "22-02-2026")
transaksi_balik.proses_kembali()

# Validasi akhir status buku
print(f"Kondisi Akhir: Buku {buku_rakyat2.judul} adalah {buku_rakyat2.status}")