def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Contoh penggunaan
data = [17, 3, 5, 12, 9, 21, 4]
cari = 12

hasil = linear_search(data, cari)

# Output
if hasil != -1:
    print(f"Data {cari} ditemukan di indeks ke-{hasil}.")
else:
    print(f"Data {cari} tidak ditemukan dalam list.")