import time
from tabulate import tabulate

class AntrianBansos:
    def __init__(self):
        self.antrian_sembako = []  # Queue untuk Sembako
        self.antrian_pkh = []  # Queue untuk PKH

    def enqueue(self, nama, jenis_bantuan):
        waktu_kedatangan = time.strftime("%H:%M:%S")  # Mencatat waktu kedatangan
        data = {"No": len(self.antrian_sembako) + 1 if jenis_bantuan == "Sembako" else len(self.antrian_pkh) + 1, 
                "Nama": nama, 
                "Waktu Kedatangan": waktu_kedatangan}

        if jenis_bantuan == "Sembako":
            self.antrian_sembako.append(data)
        else:
            self.antrian_pkh.append(data)

        print(f"\n✅ {nama} telah masuk ke antrian {jenis_bantuan} (Waktu: {waktu_kedatangan})\n")

    def dequeue(self, jenis_bantuan):
        if jenis_bantuan == "Sembako":
            if self.antrian_sembako:
                orang_dilayani = self.antrian_sembako.pop(0)
                print(f"\n🚀 {orang_dilayani['Nama']} telah dilayani untuk Sembako. (Datang: {orang_dilayani['Waktu Kedatangan']})\n")
            else:
                print("\n⚠️ Antrian Sembako kosong!\n")

        elif jenis_bantuan == "PKH":
            if self.antrian_pkh:
                orang_dilayani = self.antrian_pkh.pop(0)
                print(f"\n🚀 {orang_dilayani['Nama']} telah dilayani untuk PKH. (Datang: {orang_dilayani['Waktu Kedatangan']})\n")
            else:
                print("\n⚠️ Antrian PKH kosong!\n")

    def show_queue(self):
        print("\n📌 **Daftar Antrian Sembako:**")
        if not self.antrian_sembako:
            print("⚠️ Antrian Sembako kosong!\n")
        else:
            print(tabulate(self.antrian_sembako, headers="keys", tablefmt="grid"))

        print("\n📌 **Daftar Antrian PKH:**")
        if not self.antrian_pkh:
            print("⚠️ Antrian PKH kosong!\n")
        else:
            print(tabulate(self.antrian_pkh, headers="keys", tablefmt="grid"))
        print()

# Program CLI untuk interaksi
def main():
    antrian = AntrianBansos()

    while True:
        print("\n=== 🏛 Sistem Antrian Pengambilan Bantuan Sosial ===")
        print("1. Tambah Antrian")
        print("2. Layani Penerima Bansos")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama: ")

            # Memilih jenis bantuan
            while True:
                print("\nPilih jenis bantuan:")
                print("1. Sembako")
                print("2. Uang Tunai (PKH)")
                jenis = input("Masukkan pilihan (1/2): ")

                if jenis == "1":
                    jenis_bantuan = "Sembako"
                    break
                elif jenis == "2":
                    jenis_bantuan = "PKH"
                    break
                else:
                    print("⚠️ Pilihan tidak valid! Harap pilih 1 atau 2.")

            antrian.enqueue(nama, jenis_bantuan)

        elif pilihan == "2":
            print("\nPilih antrian yang akan dilayani:")
            print("1. Sembako")
            print("2. Uang Tunai (PKH)")
            jenis = input("Masukkan pilihan (1/2): ")

            if jenis == "1":
                antrian.dequeue("Sembako")
            elif jenis == "2":
                antrian.dequeue("PKH")
            else:
                print("⚠️ Pilihan tidak valid!\n")

        elif pilihan == "3":
            antrian.show_queue()

        elif pilihan == "4":
            print("👋 Terima kasih telah menggunakan sistem antrian!")
            break

        else:
            print("⚠️ Pilihan tidak valid! Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
