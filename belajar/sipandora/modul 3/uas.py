def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['nama']
    left = [x for x in arr if x['nama'].lower() < pivot.lower()]
    middle = [x for x in arr if x['nama'].lower() == pivot.lower()]
    right = [x for x in arr if x['nama'].lower() > pivot.lower()]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(arr, nama):
    low = 0
    high = len(arr) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid]['nama'].lower() == nama.lower():
            return mid, steps
        elif arr[mid]['nama'].lower() < nama.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

def linear_search_by_nilai(arr, nilai):
    steps = 0
    result = []
    for data in arr:
        steps += 1
        if data['nilai'] == nilai:
            result.append(data)
    return result, steps

def tampilkan_data(data_mahasiswa):
    if not data_mahasiswa:
        print("\n+------------------------+")
        print("|     TIDAK ADA DATA     |")
        print("+------------------------+")
        return
    
    max_nama = max(len(data['nama']) for data in data_mahasiswa)
    max_nama = max(max_nama, 4)
    garis = "+" + "-"*(max_nama + 2) + "+-------+"
    
    print("\n" + garis)
    print(f"| {'NAMA':<{max_nama}} | NILAI |")
    print(garis)
    
    for data in data_mahasiswa:
        print(f"| {data['nama']:<{max_nama}} | {data['nilai']:>5} |")
    
    print(garis)

def main():
    data_mahasiswa = []
    
    while True:
        print("\n+=====================================+")
        print("|       MANAJEMEN DATA MAHASISWA     |")
        print("+=====================================+")
        print("| 1. Tampilkan Data                  |")
        print("| 2. Tambah Data                     |")
        print("| 3. Hapus Data                      |")
        print("| 4. Cari Data                       |")
        print("| 5. Keluar                          |")
        print("+=====================================+")
        
        pilihan = input("| Pilih menu [1-5]: ").strip()
        print("+-------------------------------------+")
        
        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
            
        elif pilihan == "2":
            print("\n+-----------------------------+")
            print("|        TAMBAH DATA         |")
            print("+-----------------------------+")
            nama = input("| Nama  : ").strip()
            try:
                nilai = int(input("| Nilai : ").strip())
                print("+-----------------------------+")
                data_mahasiswa.append({'nama': nama, 'nilai': nilai})
                data_mahasiswa = quick_sort(data_mahasiswa)
                print(f"| Data berhasil ditambahkan!  |")
                print("+-----------------------------+")
            except ValueError:
                print("+-----------------------------+")
                print("| Nilai harus berupa angka!   |")
                print("+-----------------------------+")
                
        elif pilihan == "3":
            print("\n+-----------------------------+")
            print("|         HAPUS DATA         |")
            print("+-----------------------------+")
            nama = input("| Nama mahasiswa : ").strip()
            print("+-----------------------------+")
            
            found = False
            for i, data in enumerate(data_mahasiswa):
                if data['nama'].lower() == nama.lower():
                    del data_mahasiswa[i]
                    found = True
                    print(f"| Data {nama} dihapus!        |")
                    print("+-----------------------------+")
                    break
            
            if not found:
                print(f"| {nama} tidak ditemukan!     |")
                print("+-----------------------------+")
                
        elif pilihan == "4":
            print("\n+-----------------------------+")
            print("|          CARI DATA         |")
            print("+-----------------------------+")
            print("| 1. Cari berdasarkan nama   |")
            print("| 2. Cari berdasarkan nilai  |")
            print("+-----------------------------+")
            sub_pilihan = input("| Pilihan [1-2]: ").strip()
            print("+-----------------------------+")
            
            if sub_pilihan == "1":
                nama = input("| Nama yang dicari : ").strip()
                print("+-----------------------------+")
                
                # Ganti jump search dengan binary search
                idx, steps = binary_search(data_mahasiswa, nama)
                
                if idx != -1:
                    print(f"| Nama  : {data_mahasiswa[idx]['nama']:<18} |")
                    print(f"| Nilai : {data_mahasiswa[idx]['nilai']:<18} |")
                    print(f"| Langkah pencarian: {steps:<8} |")
                    print("+-----------------------------+")
                else:
                    # Tambahkan linear search fallback
                    found = False
                    for i, data in enumerate(data_mahasiswa):
                        if data['nama'].lower() == nama.lower():
                            print(f"| Nama  : {data['nama']:<18} |")
                            print(f"| Nilai : {data['nilai']:<18} |")
                            print("| (Ditemukan dengan linear search) |")
                            print("+-----------------------------+")
                            found = True
                            break
                    
                    if not found:
                        print(f"| {nama} tidak ditemukan!     |")
                        print("+-----------------------------+")
                    
            elif sub_pilihan == "2":
                try:
                    nilai = int(input("| Nilai yang dicari : ").strip())
                    print("+-----------------------------+")
                    hasil, steps = linear_search_by_nilai(data_mahasiswa, nilai)
                    if hasil:
                        print(f"| Data dengan nilai {nilai}:    |")
                        print("+-----------------------------+")
                        for data in hasil:
                            print(f"| • {data['nama']:<20} |")
                        print("+-----------------------------+")
                        print(f"| Langkah pencarian: {steps:<3} |")
                        print("+-----------------------------+")
                    else:
                        print(f"| Tidak ada nilai {nilai}      |")
                        print(f"| Langkah pencarian: {steps:<3} |")
                        print("+-----------------------------+")
                except ValueError:
                    print("+-----------------------------+")
                    print("| Nilai harus berupa angka!   |")
                    print("+-----------------------------+")
            else:
                print("+-----------------------------+")
                print("| Pilihan tidak valid!       |")
                print("+-----------------------------+")
                
        elif pilihan == "5":
            print("\n+-----------------------------+")
            print("|    PROGRAM BERHENTI       |")
            print("|    TERIMA KASIH           |")
            print("+-----------------------------+")
            break
            
        else:
            print("\n+-----------------------------+")
            print("| Pilihan tidak valid!       |")
            print("| Harap pilih 1-5           |")
            print("+-----------------------------+")

if __name__ == "__main__":
    main()