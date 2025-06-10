# Kelas node (simpul)
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan data
        self.next = None      # Penunjuk ke node setelahnya
        self.prev = None      # Penunjuk ke node sebelumnya

# Kelas Doubly Circular Linked List
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None  # Awal dari linked list

    # Menambahkan data di akhir (append)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            # Jika list kosong, node menunjuk ke dirinya sendiri
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev  # Node terakhir
            tail.next = new_node   # Tail ke node baru
            new_node.prev = tail   # Node baru ke tail
            new_node.next = self.head  # Node baru ke head
            self.head.prev = new_node  # Head ke node baru

    # Menampilkan isi list searah (maju)
    def display(self):
        if self.head is None:
            print("List kosong.")
            return

        print("Isi list:")
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(kembali ke head)")

    # Menghapus data yang duplikat
    def remove_duplicates(self):
        if self.head is None:
            print("List kosong.")
            return

        seen = set()
        current = self.head

        while True:
            next_node = current.next
            if current.data in seen:
                # Hapus node
                current.prev.next = current.next
                current.next.prev = current.prev

                # Jika node yang dihapus adalah head
                if current == self.head:
                    self.head = current.next
            else:
                seen.add(current.data)

            current = next_node
            if current == self.head:
                break

        print("Duplikat berhasil dihapus.")
