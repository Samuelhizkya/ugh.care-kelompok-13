# nabil
class SpotifyTop10:
    def __init__(self):
        # Inisialisasi data lagu dalam posisi acak
        self.reset_data()
    
    def reset_data(self):
        # Data asli dengan ranking benar tapi posisi acak
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
# amel
    # 1. Selection Sort
    def selection_sort(self):
        arr = self.songs.copy()
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j]["rank"] < arr[min_idx]["rank"]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # 2. Insertion Sort
    def insertion_sort(self):
        arr = self.songs.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key["rank"] < arr[j]["rank"]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
# Ratu
    # 3. Bubble Sort
    def bubble_sort(self):
        arr = self.songs.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j]["rank"] > arr[j+1]["rank"]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # 4. Quick Sort
    def quick_sort(self, arr=None):
        if arr is None:
            arr = self.songs.copy()
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]["rank"]
        left = [x for x in arr if x["rank"] < pivot]
        middle = [x for x in arr if x["rank"] == pivot]
        right = [x for x in arr if x["rank"] > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
# sela
    # 5. Heap Sort
    def heap_sort(self):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i]["rank"] < arr[l]["rank"]:
                largest = l
            if r < n and arr[largest]["rank"] < arr[r]["rank"]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        arr = self.songs.copy()
        n = len(arr)
        
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)
        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        
        return arr

    # 6. Sequential Search
    def sequential_search(self, title):
        for song in self.songs:
            if song["title"].lower() == title.lower():
                return song
        return None
# Eca
    # 7. Binary Search Tree
    class BSTNode:
        def __init__(self, song):
            self.song = song
            self.left = None
            self.right = None

    def insert_bst(self, root, song):
        if root is None:
            return self.BSTNode(song)
        if song["title"].lower() < root.song["title"].lower():
            root.left = self.insert_bst(root.left, song)
        else:
            root.right = self.insert_bst(root.right, song)
        return root

    def search_bst(self, root, title):
        if root is None or root.song["title"].lower() == title.lower():
            return root.song if root else None
        if title.lower() < root.song["title"].lower():
            return self.search_bst(root.left, title)
        return self.search_bst(root.right, title)
    
    def build_bst(self):
        root = None
        for song in self.songs:
            root = self.insert_bst(root, song)
        return root
# Muel
    def show_songs(self, songs=None):
        if songs is None:
            songs = self.songs
        
        # Print header
        print("\n+------+----------------------+---------------------------+")
        print("|             ♫  𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐓𝐎𝐏 𝟏𝟎 𝐈𝐍𝐃𝐎𝐍𝐄𝐒𝐈𝐀  ♫              |")
        print("+------+----------------------+---------------------------+")
        print("| Rank | 🎶 Title 🎶          | ✨ Artist ✨              |")
        print("+------+----------------------+---------------------------+")
        
        # Print each song
        for song in songs:
            print("| {:4} | {:20} | {:25} |".format(
                song['rank'],
                song['title'][:20],  # Limit title to 20 chars
                song['artist'][:25]   # Limit artist to 25 chars
            ))
        
        # Print footer
        print("+------+----------------------+---------------------------+")

def main():
    spotify = SpotifyTop10()
    
    while True:
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
        
        choice = input("Pilih menu: ")
        
        if choice == "1": #muel
            spotify.show_songs()
        elif choice == "2": #amel
            sorted_songs = spotify.selection_sort()
            print("\nHasil Selection Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "3":
            sorted_songs = spotify.insertion_sort()
            print("\nHasil Insertion Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "4": # Ratu
            sorted_songs = spotify.bubble_sort()
            print("\nHasil Bubble Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "5":
            sorted_songs = spotify.quick_sort()
            print("\nHasil Quick Sort:")
            spotify.show_songs(sorted_songs)
        elif choice == "6": # Sela
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
        elif choice == "8": # Eca/Muel
            title = input("Masukkan judul lagu: ")
            bst_root = spotify.build_bst()
            result = spotify.search_bst(bst_root, title)
            if result:
                print(f"\nDitemukan: {result['title']} - {result['artist']} (Rank: {result['rank']})")
            else:
                print("\nLagu tidak ditemukan!")
        elif choice == "9": # Nabil
            spotify.reset_data()
            print("\nData telah diacak ulang!")
            spotify.show_songs()
        elif choice == "0": # Nabil
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__": 
    main()