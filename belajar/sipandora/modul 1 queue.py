from collections import deque

class Queue:
    def __init__(self): 
        self.items = deque()

    # Untuk memeriksa apakah queue kosong
    def is_empty(self):
        return not self.items

    # Untuk menambahkan elemen ke queue (enqueue)
    def enqueue(self, item):
        self.items.append(item)

    # Untuk menghapus elemen pertama dari queue (dequeue)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            print("Queue is empty")
            return None

    # Mengambil elemen pertama (front)
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    # Mengambil elemen terakhir (rear)
    def rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Queue is empty")
            return None

    # Mengembalikan jumlah elemen di queue
    def size(self):
        return len(self.items)

# ===================== TESTING =====================

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue setelah enqueue:", list(q.items))  # konversi deque ke list 
print("Ukuran Queue:", q.size())
print("Dequeue item:", q.dequeue())
print("Elemen pertama (front) dalam queue:", q.front())
print("Elemen terakhir (rear) dalam queue:", q.rear())
print("Queue setelah dequeue:", list(q.items))

