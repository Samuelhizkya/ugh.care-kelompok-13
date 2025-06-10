import math
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # ukuran loncatan
    prev = 0
    
    # Lompat sampai elemen lebih besar atau sama dengan target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search di blok terakhir
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1  # target tidak ketemu

# Contoh penggunaan
data = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24, 27]
target = 15

hasil = jump_search(data, target)

if hasil != -1:
    print(f"Data {target} ditemukan di indeks ke-{hasil}")
else:
    print(f"Data {target} tidak ditemukan dalam array")