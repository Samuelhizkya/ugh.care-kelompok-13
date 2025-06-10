import csv
from tabulate import tabulate

class Node:
    def __init__(self, kode, nama, kategori, harga, stok, tanggal_kedaluwarsa):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga = int(harga)
        self.stok = int(stok)
        self.tanggal_kedaluwarsa = tanggal_kedaluwarsa
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def delete(self, kode):
        current = self.head
        while current:
            if current.kode == kode:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                print(f"Barang dengan kode {kode} berhasil dihapus.")
                return True
            current = current.next
        print(f"Barang dengan kode {kode} tidak ditemukan.")
        return False

    def update(self, kode, **kwargs):
        current = self.head
        while current:
            if current.kode == kode:
                current.nama = kwargs.get("nama", current.nama)
                current.kategori = kwargs.get("kategori", current.kategori)
                current.harga = int(kwargs.get("harga", current.harga))
                current.stok = int(kwargs.get("stok", current.stok))
                current.tanggal_kedaluwarsa = kwargs.get("tanggal_kedaluwarsa", current.tanggal_kedaluwarsa)
                print(f"Barang dengan kode {kode} berhasil diupdate.")
                return True
            current = current.next
        print(f"Barang dengan kode {kode} tidak ditemukan.")
        return False

    def display(self, sort_by_kategori=False):
        data = []
        current = self.head
        while current:
            data.append({
                "Kode": current.kode,
                "Nama": current.nama,
                "Kategori": current.kategori,
                "Harga": current.harga,
                "Stok": current.stok,
                "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
            })
            current = current.next
        if sort_by_kategori:
            data.sort(key=lambda x: x["Kategori"])
        return data

    def search(self, keyword):
        result = []
        current = self.head
        while current:
            if keyword.lower() in current.nama.lower() or keyword.lower() in current.kode.lower():
                result.append({
                    "Kode": current.kode,
                    "Nama": current.nama,
                    "Kategori": current.kategori,
                    "Harga": current.harga,
                    "Stok": current.stok,
                    "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
                })
            current = current.next
        return result

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Kode", "Nama", "Kategori", "Harga", "Stok", "Tanggal_Kedaluwarsa"])   
            current = self.head   #setiap baris berikutnya berisi data satu barang
            while current:
                writer.writerow([
                    current.kode, current.nama, current.kategori,
                    current.harga, current.stok, current.tanggal_kedaluwarsa
                ])
                current = current.next

class CircularLinkedListExpiry:
    def __init__(self):
        self.tail = None

    def insert_sorted(self, node):
        #membuat node baru dgn data yg sama
        new_node = Node(node.kode, node.nama, node.kategori, node.harga, node.stok, node.tanggal_kedaluwarsa)
        #node baru itu menujuk sm dirinya sendiri
        new_node.next = new_node

        if not self.tail: #list ksong
            self.tail = new_node
        else:  #list tidak kosong
            current = self.tail.next
            prev = self.tail
            while True:
                #bandingkan tgl kadaluwarsa
                if new_node.tanggal_kedaluwarsa < current.tanggal_kedaluwarsa:
                    break
                prev = current
                current = current.next
                if current == self.tail.next:
                    break
            new_node.next = current
            prev.next = new_node
            #jika sisip di akhir list
            if prev == self.tail:
                self.tail = new_node #update tail

    def display_expiry_order(self):
        if not self.tail:
            return []
        result = []
        current = self.tail.next
        while True:
            result.append({
                "Kode": current.kode,
                "Nama": current.nama,
                "Kategori": current.kategori,
                "Harga": current.harga,
                "Stok": current.stok,
                "Tanggal Kedaluwarsa": current.tanggal_kedaluwarsa
            })
            current = current.next
            if current == self.tail.next:
                break
        return result

# Load data from CSV and build both DLL and circular list
FILENAME = "linkedlist/data_barangku.csv"
dll_barang = DoublyLinkedList()
expiry_list = CircularLinkedListExpiry()

def load_data_from_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if len(row) == 6:
                    node = Node(*row)
                    dll_barang.insert(node)
                    expiry_list.insert_sorted(node)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")

load_data_from_csv(FILENAME)

def tampilkan_tabel(data):
    if data:
        print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
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

    pilih = input("Pilih menu (1-8): ")

    if pilih == "1":
        tampilkan_tabel(dll_barang.display())
    elif pilih == "2":
        kode = input("Kode: ")
        nama = input("Nama: ")
        kategori = input("Kategori: ")
        harga = input("Harga: ")
        stok = input("Stok: ")
        tanggal = input("Tanggal Kedaluwarsa (YYYY-MM-DD): ")
        node = Node(kode, nama, kategori, harga, stok, tanggal)
        dll_barang.insert(node)
        expiry_list.insert_sorted(node)
        dll_barang.save_to_csv(FILENAME)
    elif pilih == "3":
        kode = input("Kode barang yang ingin dihapus: ")
        if dll_barang.delete(kode):
            dll_barang.save_to_csv(FILENAME)
    elif pilih == "4":
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
        dll_barang.save_to_csv(FILENAME)
    elif pilih == "5":
        keyword = input("Cari nama/kode barang: ")
        hasil = dll_barang.search(keyword)
        tampilkan_tabel(hasil)
    elif pilih == "6":
        tampilkan_tabel(dll_barang.display(sort_by_kategori=True))
    elif pilih == "7":
        tampilkan_tabel(expiry_list.display_expiry_order())
    elif pilih == "8":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")