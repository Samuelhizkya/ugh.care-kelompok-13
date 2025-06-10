import csv
from datetime import datetime

class Barang:
    def __init__(self, kode, nama, kategori, harga, stok, expired=None):
        self.kode, self.nama, self.kategori = kode, nama, kategori
        self.harga, self.stok = int(harga), int(stok)
        self.expired = expired

    def __str__(self):
        return f"{self.kode:5} | {self.nama:15} | {self.kategori:10} | {self.harga:6} | {self.stok:4} | {self.expired or '-'}"

class Node:
    def __init__(self, data):
        self.data, self.next, self.prev = data, None, None

class DLL:
    def __init__(self): self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head: self.head = node
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next, node.prev = node, cur

    def delete(self, kode):
        cur = self.head
        while cur:
            if cur.data.kode == kode:
                if cur.prev: cur.prev.next = cur.next
                else: self.head = cur.next
                if cur.next: cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def update(self, kode, field, val):
        cur = self.head
        while cur:
            if cur.data.kode == kode and hasattr(cur.data, field):
                setattr(cur.data, field, int(val) if field in ['harga', 'stok'] else val)
                return True
            cur = cur.next
        return False

    def search(self, field, val):
        cur, result = self.head, []
        while cur:
            if getattr(cur.data, field).lower() == val.lower() if isinstance(getattr(cur.data, field), str) else getattr(cur.data, field) == val:
                result.append(cur.data)
            cur = cur.next
        return result

    def display(self, filter_expired=False):
        cur = self.head
        print("\nKode  | Nama           | Kategori   | Harga  | Stok | Expired")
        while cur:
            if not filter_expired or cur.data.expired:
                print(cur.data)
            cur = cur.next

class ManajemenStok:
    def __init__(self):
        self.dll = DLL()
        self.load()

    def load(self):
        try:
            with open("data_barang.csv", newline='') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    self.dll.append(Barang(r['kode'], r['nama'], r['kategori'], r['harga'], r['stok'], r['expired'] or None))
        except: print("CSV tidak ditemukan. Mulai dari kosong.")

    def save(self):
        with open("data_barang.csv", 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['kode', 'nama', 'kategori', 'harga', 'stok', 'expired'])
            cur = self.dll.head
            while cur:
                d = cur.data
                w.writerow([d.kode, d.nama, d.kategori, d.harga, d.stok, d.expired or ''])
                cur = cur.next
        print("Data disimpan.")

    def tambah(self):
        d = input("Kode,Nama,Kategori,Harga,Stok,Expired(YYYY-MM-DD/Enter): ").split(",")
        self.dll.append(Barang(d[0], d[1], d[2], d[3], d[4], d[5] if len(d) > 5 and d[5] else None))

    def hapus(self): print("Berhasil" if self.dll.delete(input("Kode: ")) else "Tidak ditemukan")

    def update(self):
        k = input("Kode: ")
        f = input("Field (nama/kategori/harga/stok/expired): ")
        v = input("Nilai baru: ")
        print("Berhasil" if self.dll.update(k, f, v) else "Gagal update")

    def cari(self):
        f = input("Field (kode/nama/kategori): ")
        v = input("Nilai: ")
        hasil = self.dll.search(f, v)
        if hasil:
            print("\nDitemukan:")
            for h in hasil: print(h)
        else: print("Tidak ditemukan")

    def menu(self):
        while True:
            print("\n1.Tambah 2.Hapus 3.Update 4.Tampil 5.Cari 6.Tampil Expired 7.Simpan & Keluar")
            p = input("Pilih: ")
            if p == '1': self.tambah()
            elif p == '2': self.hapus()
            elif p == '3': self.update()
            elif p == '4': self.dll.display()
            elif p == '5': self.cari()
            elif p == '6': self.dll.display(filter_expired=True)
            elif p == '7': self.save(); break
            else: print("Pilihan salah.")
 
if __name__ == "__main__":
    ManajemenStok().menu()
