class Stack:  # Mendefinisikan Kelas Stack
    def __init__(self):  # Metode Inisialisasi Kelas
        self.items = []  # Membuat List Kosong Untuk Menyimpan Data
    
    def is_empty(self):  # Metode Untuk Memeriksa Apakah Stack Kosong
        return not bool(self.items)  # Mengembalikan True Jika Stack Kosong
    
    def push(self, item):  # Metode Untuk Menambahkan Item Ke Stack
        self.items.append(item)  # Menambahkan Item Ke Bagian Atas Stack
    
    def pop(self):  # Metode Untuk Mengeluarkan Item Dari Stack
        return self.items.pop()  # Mengeluarkan Dan Mengembalikan Item Teratas
    
    def peek(self):  # Metode Untuk Melihat Item Di 
                     # Atas Stack Tanpa Mengeluarkannya
        return self.items[-1] if self.items else None  # Mengembalikan Item Teratas
                                                       # Atau None Jika Kosong
    
    def size(self):  # Metode Untuk Mendapatkan Ukuran Stack
        return len(self.items)  # Mengembalikan Jumlah Item Dalam Stack

# Contoh Penggunaan Stack !
s = Stack()  # Membuat Objek Stack Baru
s.push(1)  # Menambahkan Angka 1 Ke Stack
s.push(2)  # Menambahkan Angka 2 Ke Stack
s.push(3)  # Menambahkan Angka 3 Ke Stack
print("Stack Setelah Push: ", s.items)  # Mencetak Isi Stack Setelah Push
print("Ukuran Stack: ", s.size())  # Mencetak Ukuran Stack
print("Elemen Teratas Stack: ", s.peek())  # Mencetak Elemen Teratas Stack
print("Pop Item: ", s.pop())  # Mencetak Item Yang Dikeluarkan Dari Stack
print("Stack Setelah Pop: ", s.items)  # Mencetak Isi Stack Setelah Pop