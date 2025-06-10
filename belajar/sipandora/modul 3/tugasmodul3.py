import math

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]['nama']
    left = [x for x in arr if x['nama'] < pivot]
    middle = [x for x in arr if x['nama'] == pivot]
    right = [x for x in arr if x['nama'] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def jump_search(arr, nama):
    n = len(arr)
    step = int(math.sqrt(n))
    prev, steps = 0, 1
    
    while prev < n and arr[prev]['nama'].lower() < nama.lower(): 
        #setiap lompatan
        prev += step
        steps += 1
    
    start = max(0, prev-step) # memastikan tidak negatif
    for i in range(start, min(prev+1, n)):
        steps += 1
        if arr[i]['nama'].lower() == nama.lower():
            return i, steps
    return -1, steps

def linear_search_nilai(arr, nilai):
    steps, result = 0, []
    for data in arr:
        steps += 1
        if data['nilai'] == nilai:
            result.append(data)
    return result, steps

def tampilkan_data(data):
    if not data:
        print("\n+-------------------+")
        print("| Tidak ada data    |")
        print("+-------------------+")
        return
    
    max_nama = max(len(d['nama']) for d in data) or 4
    garis = f"+{'-'*(max_nama+2)}+{'-'*7}+"
    
    print(f"\n{garis}")
    print(f"| {'Nama':<{max_nama}} | {'Nilai':<5} |")
    print(garis)
    for d in data:
        print(f"| {d['nama']:<{max_nama}} | {d['nilai']:<5} |")
    print(garis)

def main():
    data_mahasiswa = []
    
    while True:
        print("\n+=====================================+")
        print("|      PROGRAM MANAJEMEN DATA         |")
        print("|            MAHASISWA                |")
        print("+=====================================+")
        print("| 1. Tampilkan Data                   |")
        print("| 2. Tambah Data                      |")
        print("| 3. Hapus Data                       |")
        print("| 4. Cari Data                        |")
        print("| 5. Keluar                           |")
        print("+=====================================+")
        
        pilihan = input("Pilihan (1-5): ")
        
        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
            
        elif pilihan == "2":
            print("\n+-----------------------------+")
            print("|       INPUT DATA           |")
            print("+-----------------------------+")
            nama = input("| Nama  : ")
            try:
                nilai = int(input("| Nilai : "))
                data_mahasiswa.append({'nama': nama, 'nilai': nilai})
                data_mahasiswa = quick_sort(data_mahasiswa)
                print(f"\n| Data {nama} berhasil ditambahkan! |")
            except ValueError:
                print("\n| ERROR: Nilai harus angka!   |")
            print("+-----------------------------+")
                
        elif pilihan == "3":
            print("\n+-----------------------------+")
            print("|       HAPUS DATA           |")
            print("+-----------------------------+")
            nama = input("| Nama yang dihapus: ")
            
            for i, data in enumerate(data_mahasiswa):
                if data['nama'] == nama:
                    del data_mahasiswa[i]
                    print(f"\n| Data {nama} berhasil dihapus! |")
                    break
            else:
                print(f"\n| Data {nama} tidak ditemukan!  |")
            print("+-----------------------------+")
                
        elif pilihan == "4":
            print("\n+-----------------------------+")
            print("|        CARI DATA            |")
            print("+-----------------------------+")
            print("| 1. Cari berdasarkan nama   |")
            print("| 2. Cari berdasarkan nilai  |")
            print("+-----------------------------+")
            sub_pilihan = input("Pilihan (1-2): ")
            
            if sub_pilihan == "1":
                nama = input("| Nama yang dicari: ")
                idx, steps = jump_search(data_mahasiswa, nama)
                if idx != -1:
                    print("\n+-----------------------------+")
                    print(f"| Nama  : {data_mahasiswa[idx]['nama']:<12}    |")
                    print(f"| Nilai : {data_mahasiswa[idx]['nilai']:<12}    |")
                    print(f"| Langkah: {steps:<10}         |")
                else:
                    print(f"\n| {nama} tidak ditemukan!     |")
                    print(f"| Langkah: {steps:<10}         |")
                print("+-----------------------------+")
                    
            elif sub_pilihan == "2":
                try:
                    nilai = int(input("| Nilai yang dicari: "))
                    hasil, steps = linear_search_nilai(data_mahasiswa, nilai)
                    if hasil:
                        print("\n+-----------------------------+")
                        print(f"| Hasil pencarian nilai {nilai} |")
                        print("+-----------------------------+")
                        for data in hasil:
                            print(f"| Nama: {data['nama']:<10}         |")
                        print(f"| Langkah: {steps:<10}         |")
                    else:
                        print(f"\n| Tidak ada nilai {nilai}      |")
                        print(f"| Langkah: {steps:<10}         |")
                    print("+-----------------------------+")
                except ValueError:
                    print("\n| ERROR: Nilai harus angka!   |")
                    print("+-----------------------------+")
            else:
                print("\n| Pilihan tidak valid!       |")
                print("+-----------------------------+")
                
        elif pilihan == "5":
            print("\n+-----------------------------+")
            print("|    PROGRAM BERHENTI        |")
            print("|    TERIMA KASIH!           |")
            print("+-----------------------------+")
            break
            
        else:
            print("\n| Pilihan tidak valid!       |")
            print("| Masukkan angka 1-5 saja.   |")
            print("+-----------------------------+")

if __name__ == "__main__":
    main()