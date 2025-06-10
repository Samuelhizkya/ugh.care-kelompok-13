class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Menambahkan elemen ke dalam antrian."""
        self.queue.append(item)

    def dequeue(self):
        """Menghapus elemen pertama dari antrian."""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        """Mengecek apakah antrian kosong."""
        return len(self.queue) == 0

    def quick_sort(self):
        """Mengurutkan antrian menggunakan Quick Sort."""
        def quick(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick(left) + middle + quick(right)

        self.queue = quick(self.queue)

    def display(self):
        """Menampilkan isi antrian."""
        print("Queue:", self.queue)

# Contoh Penggunaan
queue = Queue()
queue.enqueue(25)
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(40)
queue.enqueue(30)
queue.enqueue(20)
queue.enqueue(15)

print("Sebelum Sorting:")
queue.display()

queue.quick_sort()

print("Setelah Quick Sort:")
queue.display()
