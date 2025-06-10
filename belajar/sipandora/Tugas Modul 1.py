# Setiap kali membuka halaman baru,
# halaman itu ditambahkan ke Stack.
# Lalu ketika di klik “Kembali”,
# maka akan keluar dari halaman terakhir yang di buka,
# dan kembali ke halaman sebelumnya.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

# Simulasi Navigasi Halaman Buku
halaman = Stack()
halaman.push("Halaman 1")
halaman.push("Halaman 2")
halaman.push("Halaman 3")

print("📖 Saat ini berada di:", halaman.peek())  # Lihat halaman paling atas
print("🔙 Tekan tombol kembali...")
halaman.pop()  # Keluar dari Halaman 3
print("📖 Kembali ke:", halaman.peek())  # Harusnya Halaman 2



print ("\n")
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            print("Antrian kosong!")
            return None
    def size(self):
        return len(self.items)

antrian_infokus = Queue()
antrian_infokus.enqueue("Nabil - Kelas SI A")
antrian_infokus.enqueue("Eca - Kelas SI B")
antrian_infokus.enqueue("Ellen - Kelas TI A")

print("Sistem peminjaman infokus kampus:\n")
print("jumlah infokus:" , antrian_infokus.size())
print("Infokus dipinjam oleh:", antrian_infokus.dequeue())
print("Selanjutnya:", antrian_infokus.dequeue())
print("Berikutnya:", antrian_infokus.dequeue())



