# Impor library yang diperlukan
import csv  # Untuk membaca/menulis file CSV
from tabulate import tabulate  # Untuk menampilkan data dalam bentuk tabel

# Kelas Node merepresentasikan setiap barang dalam inventaris
class Node:
    def __init__(self, kode, nama, kategori, harga, stok, tanggal_kedaluwarsa):
        self.kode = kode  # Kode unik barang (string)
        self.nama = nama  # Nama barang (string)
        self.kategori = kategori  # Kategori barang (string)
        self.harga = int(harga)  # Harga barang (dikonversi ke integer)
        self.stok = int(stok)  # Stok barang (dikonversi ke integer)
        self.tanggal_kedaluwarsa = tanggal_kedaluwarsa  # Tanggal kedaluwarsa (string)
        self.prev = None  # Pointer ke node sebelumnya di doubly linked list
        self.next = None  # Pointer ke node berikutnya di doubly linked list

# Implementasi Doubly Linked List untuk manajemen inventaris
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Inisialisasi list kosong dengan head = None

    # Menambahkan barang baru di akhir list
    def insert(self, node):
        if not self.head:  # Jika list kosong
              self.head = node  # Jadikan node baru sebagai head
        else:  # Jika list tidak kosong
            current = self.head  # Mulai dari head
            while current.next:  # Iterasi sampai node terakhir
                current = current.next
            current.next = node  # Tambahkan node baru setelah node terakhir
            node.prev = current  # Set pointer prev node baru ke node sebelumnya

    # Menghapus barang berdasarkan kode
    def delete(self, kode):
        current = self.head  # Mulai pencarian dari head
        while current:  # Iterasi melalui seluruh list
            if current.kode == kode:  # Jika kode cocok
                if current.prev:  # Jika bukan node pertama
                    current.prev.next = current.next  # Hubungkan node sebelumnya ke node berikutnya
                if current.next:  # Jika bukan node terakhir
                    current.next.prev = current.prev  # Hubungkan node berikutnya ke node sebelumnya
                if current == self.head:  # Jika node yang dihapus adalah head
                    self.head = current.next  # Pindahkan head ke node berikutnya
                print(f"Barang dengan kode {kode} berhasil dihapus.")
                return True  # Return True jika berhasil dihapus
            current = current.next  # Pindah ke node berikutnya
        print(f"Barang dengan kode {kode} tidak ditemukan.")
        return False  # Return False jika tidak ditemukan

    # Memperbarui data barang
    def update(self, kode, **kwargs):
        current = self.head  # Mulai pencarian dari head
        while current:  # Iterasi melalui seluruh list
            if current.kode == kode:  # Jika kode cocok
                # Update data dengan nilai baru (jika diberikan) atau pertahankan nilai lama
                current.nama = kwargs.get("nama", current.nama)
                current.kategori = kwargs.get("kategori", current.kategori)
                current.harga = int(kwargs.get("harga", current.harga))
                current.stok = int(kwargs.get("stok", current.stok))
                current.tanggal_kedaluwarsa = kwargs.get("tanggal_kedaluwarsa", current.tanggal_kedaluwarsa)
                print(f"Barang dengan kode {kode} berhasil diupdate.")
                return True  # Return True jika berhasil diupdate
            current = current.next  # Pindah ke node berikutnya
        print(f"Barang dengan kode {kode} tidak ditemukan.")
        return False  # Return False jika tidak ditemukan

    # Menampilkan data barang
    def display(self, sort_by_kategori=False):
        data = []  # List untuk menyimpan data barang
        current = self.head  # Mulai dari head  
         while current:  # Iterasi melalui seluruh list
            # Tambahkan data barang ke dalam list
            data.append({
                "Kode": current.kode,
                "Nama": current.nama,
                "Kategori": current.kategori,
                "Harga": current.harga,
                "Stok": current.stok,
                "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
            })
            current = current.next  # Pindah ke node berikutnya
        if sort_by_kategori:  # Jika diminta diurutkan berdasarkan kategori
            data.sort(key=lambda x: x["Kategori"])  # Urutkan data berdasarkan kategori
        return data  # Kembalikan data barang

    # Mencari barang berdasarkan keyword
    def search(self, keyword):
        result = []  # List untuk menyimpan hasil pencarian
        current = self.head  # Mulai dari head
        while current:  # Iterasi melalui seluruh list
            # Cek apakah keyword cocok dengan nama atau kode (case insensitive)
            if keyword.lower() in current.nama.lower() or keyword.lower() in current.kode.lower():
                # Tambahkan barang ke hasil pencarian jika cocok
                result.append({
                    "Kode": current.kode, 
                    "Nama": current.nama,
                    "Kategori": current.kategori,
                    "Harga": current.harga,
                    "Stok": current.stok,
                    "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
                })
            current = current.next  # Pindah ke node berikutnya
        return result  # Kembalikan hasil pencarian

    # Menyimpan data ke file CSV
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)  # Buat CSV writer
            writer.writerow(["Kode", "Nama", "Kategori", "Harga", "Stok", "Tanggal_Kedaluwarsa"])  # Tulis header
            current = self.head  # Mulai dari head
            while current:  # Iterasi melalui seluruh list
                # Tulis data barang ke file CSV
                writer.writerow([
                    current.kode, 
                    current.nama, 
                    current.kategori,
                    current.harga, 
                    current.stok, 
                    current.tanggal_kedaluwarsa
                ])
                current = current.next  # Pindah ke node berikutnya

# Circular Linked List untuk mengelola barang berdasarkan kedaluwarsa (FEFO)
class CircularLinkedListExpiry:
    def __init__(self):
        self.tail = None  # Inisialisasi list kosong dengan tail = None

    # Menambahkan barang baru dengan urutan berdasarkan tanggal kedaluwarsa
    def insert_sorted(self, node):
        new_node = Node(node.kode, node.nama, node.kategori, node.harga, node.stok, node.tanggal_kedaluwarsa)
        new_node.next = new_node  # Node menunjuk ke diri sendiri (circular)

        if not self.tail:  # Jika list kosong
            self.tail = new_node  # Jadikan node baru sebagai tail
        else:  # Jika list tidak kosong
            current = self.tail.next  # Mulai dari head (karena circular)
            prev = self.tail  # Simpan node sebelumnya
            while True:  # Loop untuk mencari posisi insert
                # Bandingkan tanggal kedaluwarsa
                if new_node.tanggal_kedaluwarsa < current.tanggal_kedaluwarsa:
                    break  # Temukan posisi untuk insert
                prev = current  # Simpan node sebelumnya
                current = current.next  # Pindah ke node berikutnya
                if current == self.tail.next:  # Jika sudah satu putaran penuh
                    break  # Keluar dari loop
            new_node.next = current  # Sisipkan node baru
            prev.next = new_node  # Hubungkan node sebelumnya ke node baru
            if prev == self.tail:  # Jika node baru menjadi tail baru
                self.tail = new_node  # Update tail

    # Menampilkan barang berdasarkan urutan FEFO (First Expired First Out)
    def display_expiry_order(self):
        if not self.tail:  # Jika list kosong
            return []  # Kembalikan list kosong
        result = []  # List untuk menyimpan hasil
        current = self.tail.next  # Mulai dari head (karena circular)
        while True:  # Loop circular
            # Tambahkan data barang ke hasil
            result.append({
                "Kode": current.kode,
                "Nama": current.nama,
                "Kategori": current.kategori,
                "Harga": current.harga,
                "Stok": current.stok,
                "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
            })
            current = current.next  # Pindah ke node berikutnya
            if current == self.tail.next:  # Jika sudah satu putaran penuh
                break  # Keluar dari loop
        return result  # Kembalikan hasil

# Memuat data dari file CSV dan membangun kedua linked list
FILENAME = "linkedlist/data_barangku.csv"  # Nama file CSV
dll_barang = DoublyLinkedList()  # Inisialisasi DLL untuk manajemen barang
expiry_list = CircularLinkedListExpiry()  # Inisialisasi circular list untuk FEFO

def load_data_from_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)  #buat objek reader untuk membaca file csv baris per baris
            next(reader)  # Lewati header 
            for row in reader:  #perulangan setiap baris data
                if len(row) == 6:  # Pastikan data lengkap (6 kolom)
                    node = Node(*row)  #memasukan semua isi daftar row sbgi argumen 1 per 1 dlm node
                    dll_barang.insert(node)  # Tambahkan ke DLL
                    expiry_list.insert_sorted(node)  # Tambahkan ke circular list (FEFO)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")

# Memuat data saat program dimulai
load_data_from_csv(FILENAME)

# Fungsi untuk menampilkan data dalam bentuk tabel
def tampilkan_tabel(data):
    if data:  # Jika data tidak kosong
        print(tabulate(data, headers="keys", tablefmt="grid"))  # Tampilkan tabel
    else:  # Jika data kosong
        print("Data tidak ditemukan.")

# Menu Utama
while True:
    print("\n===== MENU =====")
    print("1. Tampilkan Semua Data")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Update Barang")
    print("5. Cari Barang")
    print("6. Tampilkan Data Urut Kategori")
    print("7. Tampilkan Urutan FEFO")
    print("8. Keluar")

    pilih = input("Pilih menu (1-8): ")  # Input pilihan user

    if pilih == "1":  # Tampilkan semua data
        tampilkan_tabel(dll_barang.display())
    
    elif pilih == "2":  # Tambah barang baru
        kode = input("Kode: ")
        nama = input("Nama: ")
        kategori = input("Kategori: ")
        harga = input("Harga: ")
        stok = input("Stok: ")
        tanggal = input("Tanggal Kedaluwarsa (YYYY-MM-DD): ")
        node = Node(kode, nama, kategori, harga, stok, tanggal)  # Buat node baru
        dll_barang.insert(node)  # Tambahkan ke DLL
        expiry_list.insert_sorted(node)  # Tambahkan ke circular list
        dll_barang.save_to_csv(FILENAME)  # Simpan ke CSV
    
    elif pilih == "3":  # Hapus barang
        kode = input("Kode barang yang ingin dihapus: ")
        if dll_barang.delete(kode):  # Jika berhasil dihapus
            dll_barang.save_to_csv(FILENAME)  # Simpan perubahan ke CSV
    
    elif pilih == "4":  # Update barang
        kode = input("Kode barang yang ingin diupdate: ")
        nama = input("Nama baru (biarkan kosong jika tidak diubah): ")
        kategori = input("Kategori baru: ")
        harga = input("Harga baru: ")
        stok = input("Stok baru: ")
        tanggal = input("Tanggal Kedaluwarsa baru: ")
        dll_barang.update(
            kode,
            nama=nama or None,
            kategori=kategori or None,
            harga=harga or None,
            stok=stok or None,
            tanggal_kedaluwarsa=tanggal or None
        )
        dll_barang.save_to_csv(FILENAME)  # Simpan perubahan ke CSV
    
    elif pilih == "5":  # Cari barang
        keyword = input("Cari nama/kode barang: ")
        hasil = dll_barang.search(keyword)  # Lakukan pencarian
        tampilkan_tabel(hasil)  # Tampilkan hasil
    
    elif pilih == "6":  # Tampilkan data urut kategori
        tampilkan_tabel(dll_barang.display(sort_by_kategori=True))
    
    elif pilih == "7":  # Tampilkan urutan FEFO
        tampilkan_tabel(expiry_list.display_expiry_order())
    
    elif pilih == "8":  # Keluar dari program
        print("Program selesai.")
        break
    
    else:  # Input tidak valid
        print("Menu tidak valid.")