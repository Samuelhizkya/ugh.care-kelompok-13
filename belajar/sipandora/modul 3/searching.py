def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]
    kiri = [x for x in data if x < pivot]
    tengah = [x for x in data if x == pivot]
    kanan = [x for x in data if x > pivot]
    return quick_sort(kiri) + tengah + quick_sort(kanan)
#Binary Search Method
def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1
# Contoh Penggunaan
nilai = [33, 10, 59, 26, 41, 58, 17, 99, 1]
# Mencari elemen menggunakan binary search
target = 1
hasil_sortir = quick_sort(nilai)
indeks = binary_search(hasil_sortir, target)
if indeks != -1:
    print(f"Elemen {target} Berhasil Ditemukan")
else:
    print(f"Elemen {target} Tidak Ditemukan")