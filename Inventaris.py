from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style

# List inventory
inventory = []

#* === CRUD ===

line_1 = '-' * 40
line_2 = '+' * 40

#? FUNCTION TAMBAH BARANG
def tambah_barang():
  while True:
      try:
          # INPUT ID BARANG
          id_barang = int(input("\nID Barang: "))
          # VALIDASI JIKA ID SUDAH ADA
          if any(item['id'] == id_barang for item in inventory):
              print("ID sudah ada! (Masukkan ID barang yang berbeda)\n")
              continue
          break  
      except ValueError:
          print("Masukkan ID dalam format angka")

    # INPUT TAMBAH BARANG
  while True:
    nama_barang = input("Nama Barang: ").strip() #INPUT NAMA
    if nama_barang: #>(True)
        break
    else:
        print(f"{Fore.YELLOW} -- Nama Barang tidak boleh kosong, Silahkan isi kembali. -- {Style.RESET_ALL}")

  while True:
      try:
        harga = int(input("Harga: ")) #INPUT HARGA
        break
      except ValueError:
        print("Masukkan harga dalam format angka!")

  while True:
      try:
        jumlah = int(input("Jumlah: ")) #INPUT JUMLAH
        break
      except ValueError:
        print("Masukkan jumlah dalam format angka!")
  total_harga = jumlah * harga  #? Menghitung total harga
  tanggal_masuk = datetime.now().strftime("%Y-%m-%d")
    # MENAMBAHKAN DICTIONARY KE DALAM LIST (inventory)
  inventory.append({
      'id': id_barang, 
      'nama_barang': nama_barang,
      'jumlah': jumlah,
      'harga': harga,
      'total_harga': total_harga,
      'tanggal_masuk': tanggal_masuk
  })
  print(f"{line_1}\n{'BARANG BERHASIL DITAMBAHKAN!✅'.center(40)}\n{line_1}")

#? KONFIRMASI UNTUK MENGINPUT ULANG
  while True:  # Validasi input y/n
    konfirmasi = input("Ingin menambahkan barang lagi? (y/n): ").strip().lower()
    if konfirmasi == 'y':
      tambah_barang()
      break  # Balik ke loop
    elif konfirmasi == 'n':
      print(f"{Fore.GREEN}{line_1}\n{'SELESAI MENAMBAH DATA ✅'.center(40)}\n{line_1}{Style.RESET_ALL}")
      return  # Keluar 
    else:
        print("Pilihan tidak valid! Ketik 'y' untuk Ya atau 'n' untuk Tidak.")

def update_barang():
    try:
        id_barang = int(input("ID Barang: "))
        found = False  #FLAG UNTUK ID

        for item in inventory:
            if item['id'] == id_barang:
                found = True # FLAG => TRUE JIKA ID DITEMUKAN
                print("\nPilih kategori update:\n1. Update Nama Barang📝\n2. Update Stok dan Harga💵")
                pilihan = input("Pilihan (1/2): ")

                if pilihan == '1':  # Update Nama Barang
                    item['nama_barang'] = input("Nama Barang (tekan Enter untuk tetap sama): ") or item['nama_barang']

                    print(f"{Fore.GREEN}{line_1}\n {'NAMA BARANG BERHASIL DIPERBARUI ✅'.center(40)}\n{line_1}{Style.RESET_ALL}")

                elif pilihan == '2':  # Update Stok dan Harga
                    jumlah_lama = item['jumlah']
                    print("\nPilih jenis update stok:\n1. Tambah Stok\n2. Kurangi Stok\n3. Update Harga")
                    stok_pilihan = input("Pilihan (1/2/3): ")

                    if stok_pilihan == '1':  # Tambah Stok
                        jumlah_input = input("Jumlah tambahan stok (masukkan angka): ")
                        if jumlah_input.isdigit():
                            tambahan_stok = int(jumlah_input)
                            item['jumlah'] = jumlah_lama + tambahan_stok
                            item['total_harga'] = item['jumlah'] * item['harga']

                            print(f"{Fore.GREEN}{line_1}\n {'STOK BERHASIL DITAMBAH ✅'.center(40)}\n{line_1}{Style.RESET_ALL}")
                        else:
                            print("Jumlah harus berupa angka positif (+)")

                    elif stok_pilihan == '2':  # Kurangi Stok
                        jumlah_input = input("Jumlah pengurangan stok (masukkan angka): ")
                        if jumlah_input.isdigit():
                            pengurangan_stok = int(jumlah_input)
                            if pengurangan_stok <= jumlah_lama:
                                item['jumlah'] = jumlah_lama - pengurangan_stok
                                item['total_harga'] = item['jumlah'] * item['harga']

                                print(f"{Fore.GREEN}{line_1}\n {'BARANG BERHASIL DIKURANGI!'.center(40)}\n{line_1}{Style.RESET_ALL}")
                            else:
                                print("Pengurangan stok melebihi jumlah stok yang tersedia")
                        else:
                            print("Jumlah harus berupa angka positif (+)")

                    elif stok_pilihan == '3':  # Update Harga
                        harga_lama = item['harga']
                        harga_baru = input("Harga (tekan Enter untuk tetap sama): ")
                        item['harga'] = int(harga_baru) if harga_baru else harga_lama

                        item['total_harga'] = item['jumlah'] * item['harga']
                        print(f"{Fore.GREEN}{line_1}\n {'HARGA BARANG BERHASIL DIPERBARUI ✅'.center(40)}\n{line_1}{Style.RESET_ALL}")
                    else:
                        print("Pilihan tidak valid. Silakan pilih 1, 2 atau 3.")
                else:
                    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
                return  #Keluar dari fungsi setelah update

        # Jika ID tidak ditemukan, tampilkan pesan 
            if not found:
                print(f"{Fore.RED}{line_2}\n{'BARANG TIDAK DITEMUKAN!❌'.center(40)}\n{line_2}{Style.RESET_ALL}")
    except ValueError:
        print("Masukkan ID dalam format angka!")

#? FUNCTION HAPUS BARANG
def hapus_barang():
    try:
        id_barang = int(input("ID Barang: "))
        for item in inventory:
            if item['id'] == id_barang:
                inventory.remove(item)
                print(f"{line_1}\n {'BARANG BERHASIL DIHAPUS ✅'.center(40)} \n{line_1}")
                return
        print(f"{Fore.RED}{line_2}\n {'BARANG TIDAK DITEMUKAN❌'.center(40)}\n{line_2}{Style.RESET_ALL}")
    except ValueError:
        print("Masukkan ID dalam format angka!")

#? FUNCTION SEARCH
def cari_barang():
    search_barang = input("Nama Barang: ")
    barang_ditemukan = [item for item in inventory if item['nama_barang'].lower() == search_barang.lower()]
    
    if barang_ditemukan:
        print(f"{Fore.MAGENTA}{line_1}\n {'BARANG DITEMUKAN ✅'.center(40)}\n{line_1}{Style.RESET_ALL}")
        # Data untuk tabulate
        data = [[item['id'], item['nama_barang'], item['jumlah'], 
                f"Rp {item['harga']:,}", f"Rp {item['total_harga']:,}", 
                item['tanggal_masuk']] for item in barang_ditemukan]
        
        headers = ["ID", "Nama Barang", "Jumlah", "Harga Satuan", "Total Harga", "Tanggal Masuk"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print(f"{Fore.RED}{line_2}\n{'BARANG TIDAK DITEMUKAN❌'.center(40)}\n{line_2}{Style.RESET_ALL}")


#? FUNCTION DATA BARANG
def data_barang():
    if not inventory:
        print(f"{Fore.MAGENTA}{line_1}\n {'INVENTARIS KOSONG'.center(40)} \n{line_1}{Style.RESET_ALL}")
        return

    # Data untuk tabulate
    data = [[item['id'], item['nama_barang'], item['jumlah'], f"Rp {int(item['harga']):,}", f"Rp {int(item['total_harga']):,}", item['tanggal_masuk']] for item in inventory]

    headers = ["ID", "Nama Barang", "Jumlah", "Harga Satuan", "Total Harga", "Tanggal Masuk"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

#* Main Menu
while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Update Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("5. Data Barang")
    print("6. Keluar")
    print('')

    pilihan = input('Pilih Menu (1-6):')
    if pilihan == '1':
        print('---- Tambah Barang ----')
        tambah_barang() 
    elif pilihan == '2':
        print('---- Update Barang ----')
        update_barang()
    elif pilihan == '3':
        print('---- Hapus Barang ----')
        hapus_barang()
    elif pilihan == '4':
        print('---- Cari Barang ----')
        cari_barang()
    elif pilihan == '5':
        print('---- Data Barang ----')
        data_barang()
    elif pilihan == '6':
        print('---- Program Keluar ----')
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
