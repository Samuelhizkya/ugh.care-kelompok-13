import time

class AntrianBansos:
    def __init__(self):
        self.queue = []  # List sebagai queue

    def enqueue(self, nama, keperluan):
        waktu_kedatangan = time.strftime("%H:%M:%S")  # Mencatat waktu kedatangan
        self.queue.append({"nama": nama, "keperluan": keperluan, "waktu": waktu_kedatangan})
        print(f"{nama} telah masuk ke dalam antrian untuk {keperluan} (Waktu: {waktu_kedatangan})\n")

    def dequeue(self):
        if self.queue:
            orang_dilayani = self.queue.pop(0)  # Menghapus orang pertama dalam antrian (FIFO)
            print(f"{orang_dilayani['nama']} telah dilayani. (Datang: {orang_dilayani['waktu']})\n")
        else:
            print("Antrian kosong!\n")

    def show_queue(self):
        if not self.queue:
            print("Antrian kosong!\n")
        else:
            print("📌 **Daftar Antrian:**")
            for i, p in enumerate(self.queue, 1):
                print(f"{i}. {p['nama']} - {p['keperluan']} (Waktu: {p['waktu']})")
            print()

# Program CLI untuk interaksi
def main():
    antrian = AntrianBansos()

    while True:
        print("\n=== Sistem Antrian Pengambilan Bantuan Sosial ===")
        print("1. Tambah Antrian")
        print("2. Layani Penerima Bansos")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama: ")
            keperluan = input("Masukkan Jenis Bantuan (Beras/Uang Tunai/Minyak): ")
            antrian.enqueue(nama, keperluan)

        elif pilihan == "2":
            antrian.dequeue()

        elif pilihan == "3":
            antrian.show_queue()

        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem antrian!")
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
