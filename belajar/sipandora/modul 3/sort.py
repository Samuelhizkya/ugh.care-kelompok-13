def quick_sort(data):
    if len(data) <= 1:
        return data
# Menentukan pivot dan mencari left, mid, right
    pivot = data[len(data) // 2]
    kiri = [x for x in data if x < pivot]
    tengah = [x for x in data if x == pivot]
    kanan = [x for x in data if x > pivot]

    return quick_sort(kiri) + tengah + quick_sort(kanan)

# Contoh penggunaan
nilai = [33, 10, 59, 26, 41, 58, 17, 99, 1]
print("Data Sebelum Di - Sort :", nilai)
hasil_sortir = quick_sort(nilai)
print("Data Setelah Di - Sort :", hasil_sortir)