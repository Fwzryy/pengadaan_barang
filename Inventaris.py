from datetime import datetime
from tabulate import tabulate

# List inventory
inventory = []

#* === CRUD ===

#? FUNCTION TAMBAH BARANG
def tambah_barang():
    while True:
        try:
            #/ INPUT ID BARANG
            print('\n')
            id_barang = int(input("ID Barang :"))

            #/ VALIDASI JIKA ID SUDAH ADA
            if any(item['id'] == id_barang for item in inventory):
                print("ID sudah ada! (Masukkan ID barang yang berbeda)\n")
                continue
            
            break  
        except ValueError:
            print("Masukkan ID dalam format angka")

    #/ INPUT TAMBAH BARANG
    nama_barang = input("Nama Barang: ")
    jumlah = int(input("Jumlah: "))
    harga = float(input("Harga: "))
    total_harga = jumlah * harga  #? Menghitung total harga
    tanggal_masuk = datetime.now().strftime("%Y-%m-%d")

    #// MENAMBAHKAN DICTIONARY KE DALAM LIST (inventory)
    inventory.append({
        'id': id_barang, 
        'nama_barang': nama_barang,
        'jumlah': jumlah,
        'harga': harga,
        'total_harga': total_harga,
        'tanggal_masuk': tanggal_masuk
    })
    print('''
          ===============================
            BARANG BERHASIL DITAMBAHKAN!
          ===============================
          ''')

#? FUNCTION UPDATE BARANG
def update_barang():
    try:
        id_barang = int(input("ID Barang: "))
        for item in inventory:
            if item['id'] == id_barang:
                item['nama_barang'] = input("Nama Barang (tekan Enter untuk tetap sama): ") or item['nama_barang']

                #> SIMPAN JUMLAH DAN HARGA LAMA
                jumlah_lama = item['jumlah']
                harga_lama = item['harga']

                #> UPDATE JUMLAH
                jumlah_input = input("Jumlah (tekan Enter untuk tetap sama): ") 
                jumlah_baru = int(jumlah_input) if jumlah_input else jumlah_lama

                #> UPDATE HARGA
                harga_input = input("Harga (tekan Enter untuk tetap sama): ")
                harga_baru = float(harga_input) if harga_input else harga_lama

                #> UPDATE ITEM
                item['jumlah'] = jumlah_baru
                item['harga'] = harga_baru
                item['total_harga'] = jumlah_baru * harga_baru  # Perbarui total harga

                print('''
                  ===============================
                    BARANG BERHASIL DI UPDATE!
                  ===============================
                  ''')
                return
        print('''
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                  BARANG TIDAK DITEMUKAN
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              ''')
    except ValueError:
        print("Masukkan ID dalam format angka!")

#? FUNCTION HAPUS BARANG
def hapus_barang():
    try:
        id_barang = int(input("ID Barang: "))
        for item in inventory:
            if item['id'] == id_barang:
                inventory.remove(item)
                print('''
                  ===============================
                      BARANG BERHASIL DIHAPUS!
                  ===============================
                  ''')
                return
        print('''
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
                  BARANG TIDAK DITEMUKAN
              -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              ''')
    except ValueError:
        print("Masukkan ID dalam format angka!")

#? FUNCTION SEARCH
def cari_barang():
    search_barang = input("Nama Barang: ")
    for item in inventory:
        if item['nama_barang'].lower() == search_barang.lower():
            print('''
              ===============================
                      BARANG DITEMUKAN!
              ===============================
              ''')
            print("\nID:", item['id'])
            print("Nama Barang:", item['nama_barang'])
            print("Jumlah:", item['jumlah'])
            print(f"Harga Satuan: Rp {item['harga']:.2f}")
            print(f"Total Harga: Rp {item['total_harga']:.2f}")
            print("Tanggal Masuk:", item['tanggal_masuk'])
            return
    print('''
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
              BARANG TIDAK DITEMUKAN
          -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
          ''')

#? FUNCTION DATA BARANG
def data_barang():
    if not inventory:
        print('''
              -------------------------------
                    INVENTARIS KOSONG
              -------------------------------
              ''')
        return

    # Data untuk tabulate
    data = [[item['id'], item['nama_barang'], item['jumlah'], f"Rp {item['harga']:.2f}", f"Rp {item['total_harga']:.2f}", item['tanggal_masuk']] for item in inventory]

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

    pilihan = input('''---------- Pilih menu (1-6): ----------''')
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
