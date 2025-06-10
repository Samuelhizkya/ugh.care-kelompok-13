#! Class untuk mengelola data top 10 lagu Spotify Indonesia
class SpotifyTop10:
    #! Constructor class, dipanggil saat objek dibuat
    def __init__(self):
        #! Memanggil method reset_data() untuk inisialisasi awal
        self.reset_data()
    
    #! Method untuk mengembalikan data ke kondisi awal (acak)
    def reset_data(self):
        #! Data lagu dalam bentuk list of dictionary
        #! Setiap lagu memiliki title, artist, dan rank
        self.songs = [
            {"title": "Komang", "artist": "Raim Laode", "rank": 6},
            {"title": "Lesung Pipi", "artist": "Raim Laode", "rank": 2},
            {"title": "Stecu Stecu", "artist": "Faris Adam", "rank": 9},
            {"title": "You'll Be in My Heart", "artist": "NIKI", "rank": 3},
            {"title": "Hitam Putih", "artist": "Fourtwnty", "rank": 8},
            {"title": "Serana", "artist": "For Revenge", "rank": 5},
            {"title": "Bila Kau Tak Disampingku", "artist": "Sheila On 7", "rank": 7},
            {"title": "Nina", "artist": ".Feast", "rank": 4},
            {"title": "Monolog", "artist": "Pamungkas", "rank": 10},
            {"title": "Mangu", "artist": "Fourtwnty, Charita Utami", "rank": 1}  
        ]

    #! 1. Implementasi Selection Sort
    def selection_sort(self):
        #! Membuat salinan list songs untuk diurutkan
        arr = self.songs.copy()
        #! Loop melalui semua elemen array
        for i in range(len(arr)):
            #! Asumsikan elemen terkecil adalah elemen saat ini
            min_idx = i
            #! Cari elemen terkecil di sisa array
            for j in range(i+1, len(arr)):
                #! Bandingkan berdasarkan rank
                if arr[j]["rank"] < arr[min_idx]["rank"]:
                    min_idx = j
            #! Tukar elemen terkecil yang ditemukan dengan elemen pertama
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    #! 2. Implementasi Insertion Sort
    def insertion_sort(self):
        #! Membuat salinan list songs
        arr = self.songs.copy()
        #! Loop dari elemen kedua sampai akhir
        for i in range(1, len(arr)):
            #! Simpan elemen saat ini sebagai key
            key = arr[i]
            #! Pindahkan elemen arr[0..i-1] yang lebih besar dari key
            j = i-1
            #! Geser elemen yang lebih besar dari key ke kanan
            while j >=0 and key["rank"] < arr[j]["rank"]:
                arr[j+1] = arr[j]
                j -= 1
            #! Tempatkan key pada posisi yang benar
            arr[j+1] = key
        return arr

    #! 3. Implementasi Bubble Sort
    def bubble_sort(self):
        #! Membuat salinan list songs
        arr = self.songs.copy()
        n = len(arr)
        #! Loop melalui semua elemen array
        for i in range(n):
            #! Elemen terakhir i sudah pada tempatnya
            for j in range(0, n-i-1):
                #! Tukar jika elemen ditemukan lebih besar dari elemen berikutnya
                if arr[j]["rank"] > arr[j+1]["rank"]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    #! 4. Implementasi Quick Sort
    def quick_sort(self, arr=None):
        #! Jika arr None, gunakan data songs sebagai default
        if arr is None:
            arr = self.songs.copy()
        #! Base case: array dengan 0 atau 1 elemen sudah terurut
        if len(arr) <= 1:
            return arr
        #! Pilih pivot di tengah array
        pivot = arr[len(arr)//2]["rank"]
        #! Partisi: elemen lebih kecil dari pivot
        left = [x for x in arr if x["rank"] < pivot]
        #! Elemen sama dengan pivot
        middle = [x for x in arr if x["rank"] == pivot]
        #! Elemen lebih besar dari pivot
        right = [x for x in arr if x["rank"] > pivot]
        #! Gabungkan hasil rekursif
        return self.quick_sort(left) + middle + self.quick_sort(right)

    #! 5. Implementasi Heap Sort
    def heap_sort(self):
        #! Fungsi helper untuk membentuk heap
        def heapify(arr, n, i):
            largest = i  #! Inisialisasi root terbesar
            l = 2 * i + 1  #! left child
            r = 2 * i + 2  #! right child
            #! Jika left child lebih besar dari root
            if l < n and arr[i]["rank"] < arr[l]["rank"]:
                largest = l
            #! Jika right child lebih besar dari largest
            if r < n and arr[largest]["rank"] < arr[r]["rank"]:
                largest = r
            #! Jika largest bukan root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  #! swap
                heapify(arr, n, largest)  #! Heapify subtree yang terpengaruh

        arr = self.songs.copy()
        n = len(arr)
        
        #! Build max heap
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)
        
        #! Ekstrak elemen satu per satu
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  #! swap
            heapify(arr, i, 0)  #! heapify root yang baru
        
        return arr

    #! 6. Sequential Search
    def sequential_search(self, title):
        #! Loop melalui semua lagu
        for song in self.songs:
            #! Bandingkan judul (case insensitive)
            if song["title"].lower() == title.lower():
                return song
        return None  #! Return None jika tidak ditemukan

    #! 7. Binary Search Tree (BST) Node class
    class BSTNode:
        #! Constructor untuk node BST
        def __init__(self, song):
            self.song = song  #! Data lagu
            self.left = None   #! Subtree kiri
            self.right = None  #! Subtree kanan

    #! Method untuk memasukkan data ke BST
    def insert_bst(self, root, song):
        #! Jika root kosong, buat node baru
        if root is None:
            return self.BSTNode(song)
        #! Jika judul lagu lebih kecil, masukkan ke subtree kiri
        if song["title"].lower() < root.song["title"].lower():
            root.left = self.insert_bst(root.left, song)
        #! Jika lebih besar atau sama, masukkan ke subtree kanan
        else:
            root.right = self.insert_bst(root.right, song)
        return root

    #! Method untuk mencari di BST
    def search_bst(self, root, title):
        #! Base case: root null atau judul cocok
        if root is None or root.song["title"].lower() == title.lower():
            return root.song if root else None
        #! Jika judul lebih kecil, cari di subtree kiri
        if title.lower() < root.song["title"].lower():
            return self.search_bst(root.left, title)
        #! Jika lebih besar, cari di subtree kanan
        return self.search_bst(root.right, title)
    
    #! Method untuk membangun BST dari data songs
    def build_bst(self):
        root = None
        #! Insert semua lagu ke BST
        for song in self.songs:
            root = self.insert_bst(root, song)
        return root

    #! Method untuk menampilkan daftar lagu dalam format tabel
    def show_songs(self, songs=None):
        #! Jika songs None, gunakan data songs default
        if songs is None:
            songs = self.songs
        
        #! Print header tabel
        print("\n+------+----------------------+---------------------------+")
        print("|             ♫  𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐓𝐎𝐏 𝟏𝟎 𝐈𝐍𝐃𝐎𝐍𝐄𝐒𝐈𝐀  ♫              |")
        print("+------+----------------------+---------------------------+")
        print("| Rank | 🎶 Title 🎶          | ✨ Artist ✨              |")
        print("+------+----------------------+---------------------------+")
        
        #! Print setiap lagu dalam tabel
        for song in songs:
            print("| {:4} | {:20} | {:25} |".format(
                song['rank'],
                song['title'][:20],  #! Batasi panjang judul 20 karakter
                song['artist'][:25]   #! Batasi panjang artist 25 karakter
            ))
        
        #! Print footer tabel
        print("+------+----------------------+---------------------------+")

#! Fungsi utama program
def main():
    #! Buat objek SpotifyTop10
    spotify = SpotifyTop10()
    
    #! Loop menu utama
    while True:
        #! Tampilkan menu
        print("\nMenu Spotify Top 10 Indonesia:")
        print("1. Tampilkan Lagu")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Bubble Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Cari Lagu (Sequential Search)")
        print("8. Cari Lagu (Binary Search Tree)")
        print("9. Reset Data (Acak Ulang)")
        print("0. Keluar")
        
        #! Input pilihan user
        choice = input("Pilih menu: ")
        
        #! Handler untuk setiap pilihan menu
        if choice == "1":
            spotify.show_songs()
        elif choice == "2":
            sorted_songs = spotify.selection_sort()
            print("\nHasil Selection Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "3":
            sorted_songs = spotify.insertion_sort()
            print("\nHasil Insertion Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "4":
            sorted_songs = spotify.bubble_sort()
            print("\nHasil Bubble Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "5":
            sorted_songs = spotify.quick_sort()
            print("\nHasil Quick Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "6":
            sorted_songs = spotify.heap_sort()
            print("\nHasil Heap Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "7":
            title = input("Masukkan judul lagu: ")
            result = spotify.sequential_search(title)
            if result:
                print(f"\nDitemukan: {result['title']} - {result['artist']} (Rank: {result['rank']})")
            else:
                print("\nLagu tidak ditemukan!")
        elif choice == "8":
            title = input("Masukkan judul lagu: ")
            bst_root = spotify.build_bst()
            result = spotify.search_bst(bst_root, title)
            if result:
                print(f"\nDitemukan: {result['title']} - {result['artist']} (Rank: {result['rank']})")
            else:
                print("\nLagu tidak ditemukan!")
        elif choice == "9":
            spotify.reset_data()
            print("\nData telah diacak ulang!")
            spotify.show_songs()
        elif choice == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

#! Entry point program
if __name__ == "__main__":
    (main)