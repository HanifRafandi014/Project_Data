# Inisialisasi daftar item dan harga
daftar_item = []
harga_item = []
jumlah_item = [] 

# Fungsi untuk menambahkan item ke keranjang
def tambah_item(item, harga, jumlah):
    daftar_item.append(item)
    harga_item.append(harga)
    jumlah_item.append(jumlah)

# Fungsi untuk menghitung total belanjaan
def hitung_total():
    # list comprehension dan fungsi zip untuk mengalikan setiap harga item dengan jumlah item yang dibeli, lalu menghitung totalnya dengan sum. 
    total = sum([harga * jumlah for harga, jumlah in zip(harga_item, jumlah_item)])
    return total

# Fungsi untuk mencetak struk pembayaran
def cetak_struk():
    print("\n=============================================================")
    print("                       Struk Pembayaran                      ")
    print("=============================================================")
    for i in range(len(daftar_item)):
        print(f"|{daftar_item[i]:<20} | Rp {harga_item[i]:,.2f} | {jumlah_item[i]}| ")
    print(" ")
    total = hitung_total()
    print(f"Total Pembayaran : Rp {total:,.2f}")
    print("=============================================================")

# Fungsi utama
def main():
    while True:
        print("\nAplikasi Kasir Sederhana")
        print("1. Tambah Item")
        print("2. Cetak Struk")
        print("3. Keluar\n")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            item = input("Nama Item: ")
            harga = float(input("Harga Item: Rp "))
            jumlah = int(input("Jumlah Item: "))
            tambah_item(item, harga, jumlah)
            print(f"\n{item} ditambahkan ke keranjang.")
        elif pilihan == "2":
            if not daftar_item:
                print("Keranjang kosong.")
            else:
                cetak_struk()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            break

        print("\nTerima kasih atas kerja kerasnya!")

if __name__ == "__main__":
    main()
