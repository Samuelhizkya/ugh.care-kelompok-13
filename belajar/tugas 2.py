def bubble_sort(arr):
    """
    Algoritma Bubble Sort
    Args:
        arr (list): List yang akan diurutkan
    Returns:
        list: List yang sudah diurutkan
    """
    n = len(arr)
    # Membuat salinan array agar array asli tidak berubah
    array = arr.copy()
    
    print("Bubble Sort dimulai dengan array:", array)
    
    # Iterasi pertama untuk mengontrol jumlah pass
    for i in range(n):
        # Flag untuk mengoptimalkan algoritma
        swapped = False
        print(f"Iterasi {i+1}:")
        
        # Iterasi kedua untuk membandingkan dan menukar elemen
        for j in range(0, n-i-1):
            # Membandingkan elemen berdekatan
            if array[j] > array[j+1]:
                # Menukar elemen jika tidak berurutan
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                print(f"  Menukar {array[j]} dan {array[j+1]}: {array}")
        
        # Jika tidak ada pertukaran pada iterasi ini, array sudah terurut
        if not swapped:
            print(f"  Tidak ada pertukaran, array sudah terurut: {array}")
            break
            
    print(f"Hasil Bubble Sort: {array}\n")
    return array


def insertion_sort(arr):
    """
    Algoritma Insertion Sort
    
    Args:
        arr (list): List yang akan diurutkan
        
    Returns:
        list: List yang sudah diurutkan
    """
    n = len(arr)
    # Membuat salinan array agar array asli tidak berubah
    array = arr.copy()
    
    print("Insertion Sort dimulai dengan array:", array)
    
    # Mulai dari elemen kedua (indeks 1)
    for i in range(1, n):
        # Simpan nilai yang akan dimasukkan
        key = array[i]
        # Indeks elemen sebelumnya
        j = i - 1
        print(f"Iterasi {i}: Memasukkan nilai {key}")
        
        # Geser elemen yang lebih besar dari key ke posisi satu di depannya
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            print(f"  Menggeser {array[j]} ke posisi {j+1}: {array}")
            j -= 1
            
        # Memasukkan key ke posisi yang tepat
        array[j+1] = key
        print(f"  Memasukkan {key} ke posisi {j+1}: {array}")
    
    print(f"Hasil Insertion Sort: {array}\n")
    return array


def selection_sort(arr):
    """
    Algoritma Selection Sort
    Args:
        arr (list): List yang akan diurutkan
    Returns:
        list: List yang sudah diurutkan
    """
    n = len(arr)
    # Membuat salinan array agar array asli tidak berubah
    array = arr.copy()
    
    print("Selection Sort dimulai dengan array:", array)
    
    # Iterasi melalui semua elemen array
    for i in range(n):
        # Temukan nilai minimum di array yang belum terurut
        min_idx = i
        print(f"Iterasi {i+1}: Mencari nilai minimum mulai dari indeks {i}")
        
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
                print(f"  Menemukan nilai minimum baru {array[min_idx]} di indeks {min_idx}")
        
        # Tukar elemen minimum dengan elemen pertama yang belum terurut
        if min_idx != i:
            print(f"  Menukar {array[i]} dengan {array[min_idx]}")
            array[i], array[min_idx] = array[min_idx], array[i]
        else:
            print(f"  Elemen {array[i]} sudah pada posisi yang benar")
            
        print(f"  Array setelah iterasi {i+1}: {array}")
    
    print(f"Hasil Selection Sort: {array}\n")
    return array


# Program utama
if __name__ == "__main__":
    # Data yang akan diurutkan
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Array awal: {data}\n")
    
    # Menjalankan algoritma sorting
    bubble_sort(data)
    insertion_sort(data)
    selection_sort(data)
    
    print("Semua algoritma menghasilkan array yang sama (terurut).")