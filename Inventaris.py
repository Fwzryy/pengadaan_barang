from tabulate import tabulate 
from datetime import datetime
from termcolor import colored


# List inventory
inventory = []

#* === CRUD ===

#? FUNCTION TAMBAH BARANG
def tambah_barang():
    
    #/ INPUT TAMBAH BARANG
    nama_barang = input("Nama Barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga: "))
    total_harga = jumlah * harga  #// Menghitung total harga
    tanggal_masuk = datetime.now().strftime("%Y-%m-%d")

    #// MENAMBAHKAN DICTIONARY KE DALAM LIST (inventory)
    inventory.append({
        'id': len(inventory) + 1, 
        'nama_barang': nama_barang,
        'jumlah': jumlah,
        'harga': harga,
        'total_harga': total_harga,
        'tanggal_masuk': tanggal_masuk
    })
    print(colored('''
          ===============================
            BARANG BERHASIL DITAMBAHKAN!
          ===============================
          ''','green'))

#? FUNCTION UPDATE BARANG
def update_barang():
    id_barang = int(input("ID Barang: "))
    for item in inventory:
        if item['id'] == id_barang:
            item['nama_barang'] = input("Nama Barang (tekan Enter untuk tetap sama): ") or item['nama_barang']
            
            #> SIMPAN JUMLAH DAN HARGA LAMA
            jumlah_lama = item['jumlah']
            harga_lama = item['harga']
            
            #> UPDATE JUMLAHS
            jumlah_input = input("Jumlah (tekan Enter untuk tetap sama): ") 
            jumlah_baru = int(jumlah_input) if jumlah_input else jumlah_lama
            
            #> UPDATE HARGA
            harga_input = input("Harga (tekan Enter untuk tetap sama): ")
            harga_baru = float(harga_input) if harga_input else harga_lama
            
            #> UPDATE ITEM
            item['jumlah'] = jumlah_baru
            item['harga'] = harga_baru
            item['total_harga'] = jumlah_baru * harga_baru  # Perbarui total harga
            
            print(colored('''
              ===============================
                BARANG BERHASIL DI UPDATE!
              ===============================
              ''','green'))
            return
    print(colored('''
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              BARANG TIDAK DITEMUKAN
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
          ''', 'red'))

#? FUNCTION HAPUS BARANG
def hapus_barang():
    id_barang = int(input("ID Barang: "))
    for item in inventory:
        if item['id'] == id_barang:
            inventory.remove(item)
            print(colored('''
              ===============================
                  BARANG BERHASIL DIHAPUS!
              ===============================
              ''','green'))
            return
    print(colored('''
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              BARANG TIDAK DITEMUKAN
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
          ''', 'red'))

#? FUNCTION SEARCH
def cari_barang():
    search_barang = input("Nama Barang: ")
    for item in inventory:
        if item['nama_barang'].lower() == search_barang.lower():
            print(colored('''
              ===============================
                      BARANG DITEMUKAN!
              ===============================
              ''','green'))
            print(tabulate([[
                item['id'], 
                item['nama_barang'], 
                item['jumlah'], 
                f"Rp {item['harga']:,.2f}", 
                f"Rp {item['total_harga']:,.2f}",  # Menampilkan total harga
                item['tanggal_masuk']
            ]], headers=['ID', 'Nama Barang', 'Jumlah', 'Harga Satuan', 'Total Harga', 'Tanggal Masuk']))
            return
    print(colored('''
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              BARANG TIDAK DITEMUKAN
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
          ''', 'red'))

#? FUNCTION DATA BARANG
def data_barang():
    if not inventory:
        print('''
              -------------------------------
                    INVENTARIS KOSONG
              -------------------------------
              ''')
        return

    print("\nData Barang:")
    # Menghitung total harga seluruh inventaris
    total_harga_inventaris = sum(item['total_harga'] for item in inventory)
    
    # Menggunakan tabulate untuk menampilkan tabel yang lebih rapi
    print(tabulate(
        [[
            item['id'], 
            item['nama_barang'], 
            item['jumlah'], 
            f"Rp {item['harga']:,.2f}", 
            f"Rp {item['total_harga']:,.2f}",  #> Menampilkan total harga per item (HARGA SATUAN)
            item['tanggal_masuk']
        ] for item in inventory],
        headers=['ID', 'Nama Barang', 'Jumlah', 'Harga Satuan', 'Total Harga', 'Tanggal Masuk'],
        tablefmt='grid'
    ))
    
    # Menampilkan total harga seluruh inventaris
    print(f"\nTotal Harga Seluruh Inventaris: Rp {total_harga_inventaris:,.2f}")

#* Main Menu
while True:
    menu_data = [
        [1, "Tambah Barang"],
        [2, "Update Barang"],
        [3, "Hapus Barang"],
        [4, "Cari Barang"],
        [5, "Data Barang"],
        [6, "Keluar"]
    ]
    print("\nMenu:")
    print(tabulate(menu_data, headers=["No", "Aksi"], tablefmt="grid"))  # Menampilkan tabel dengan format grid
    
    pilihan = input("Pilih menu (1-6): ")
    if pilihan == '1':
        tambah_barang() 
    elif pilihan == '2':
        update_barang()
    elif pilihan == '3':
        hapus_barang()
    elif pilihan == '4':
        cari_barang()
    elif pilihan == '5':
        data_barang()
    elif pilihan == '6':
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")