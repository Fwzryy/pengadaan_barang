from tabulate import tabulate 
from datetime import datetime
import pandas as pd

# Array Kosong inventory
inventory = []

#* === CRUD ===

#? FUNCTION TAMBAH BARANG
def tambah_barang():
    nama_barang = input("Nama Barang: ") #/input nama barang -> variable nama_barang
    jumlah = int(input("Jumlah: ")) #/input jumlah barang -> variable jumlah_barang
    harga = float(input("Harga: ")) #/input harga barang -> variable harga
    tanggal_masuk = datetime.now().strftime("%Y-%m-%d") #/mengambil waktu saat ini (datetime.now) dan diformat ke str(YYYY-DD-MM)

    inventory.append({ #! menambahkan sebuah dictionary ke dalam list inventory
        'id': len(inventory) + 1,
        'nama_barang': nama_barang,
        'jumlah': jumlah,
        'harga': harga,
        'tanggal_masuk': tanggal_masuk
    })
    print("Barang berhasil ditambahkan!")

#? FUNCTION UPDATE BARANG
def update_barang():
    id_barang = int(input("ID Barang: ")) #/Input ID Barang (int)
    for item in inventory: #/Melakukan iterasi untuk setiap item dalam list inventory
        
        if item['id'] == id_barang: #/Memeriksa setiap barang dalam inventory dengan ID yang cocok dengan id_barang
            item['nama_barang'] = input("Nama Barang (tekan Enter untuk tetap sama): ") or item['nama_barang'] #/Memasukkan nama baru, jika tidak pencet (enter) -> nama barang tetap menggunakan nilai sebelumnya
            jumlah_input = input("Jumlah (tekan Enter untuk tetap sama): ") 
            item['jumlah'] = int(jumlah_input) if jumlah_input else item['jumlah']
            harga_input = input("Harga (tekan Enter untuk tetap sama): ")
            item['harga'] = float(harga_input) if harga_input else item['harga']
            print("Barang berhasil diupdate!")
            return
    print("Barang tidak ditemukan!") #! Jika tidak ada ID yang cocok dengan ID Barang

#? FUNCTION HAPUS BARANG
def hapus_barang():
    id_barang = int(input("ID Barang: "))
    for item in inventory:
        if item['id'] == id_barang: #/ mencocokkan id dengan id_barang
            inventory.remove(item) #/ remove berdasarkan id
            print("Barang berhasil dihapus!") 
            return
    print("Barang tidak ditemukan!") #! Jika tidak ada ID yang cocok dengan ID Barang

#? FUNCTION SEARCH
def cari_barang():
    search_barang = input("Nama Barang: ") #/input nama barang yang ingin dicari dan masukkan ke var search_barang
    for item in inventory:
        if item['nama_barang'].lower() == search_barang.lower():  #/jika item nama_barang cocok dengan nilai search_barang
            print("Barang ditemukan!")
            print(tabulate([[item['id'], item['nama_barang'], item['jumlah'], item['harga'], item['tanggal_masuk']]], headers=['ID', 'Nama Barang', 'Jumlah', 'Harga', 'Tanggal Masuk']))
            return
    print("Barang tidak ditemukan!") #! Jika tidak ada ID yang cocok dengan ID Barang

#? FUNCTION DATA BARANG
def data_barang():
    if not inventory:
        print("Inventaris kosong!") #* jika function data_barang dijalankan namun tidak ada data apapun di dalamnya
        return

    print("Data Barang:") #* jika ada tampilkan
    # Menggunakan tabulate untuk menampilkan tabel yang lebih rapi
    print(tabulate(
        [[item['id'], item['nama_barang'], item['jumlah'], item['harga'], item['tanggal_masuk']] for item in inventory],
        headers=['ID', 'Nama Barang', 'Jumlah', 'Harga', 'Tanggal Masuk'],
        tablefmt='grid'  # Format tabel yang membuat garis tepi
    ))


#* Main Menu
while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Update Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("5. Data Barang")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-8): ")
    
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
