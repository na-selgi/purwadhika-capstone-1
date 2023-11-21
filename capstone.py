listBarang = [
    {
        "id": "1",
        "nama": "baju",
        "stock": 5,
        "harga": 150000,
        "tipe": "import" 

    },
    {
        "id": "2",
        "nama": "celana",
        "stock": 5,
        "harga": 200000,
        "tipe": "local" 
    }, 
    {
        "id": "3",
        "nama": "sepatu",
        "stock": 5,
        "harga": 200000,
        "tipe": "import" 
    },
]

# Fungsi Cari ID
def cariID(id):
    for item in listBarang:
        if item["id"] == id:
            return item
    return False

# Fungsi Tampilkan Semua
def tampilkanSemua():
    if listBarang:
        print("\nID\tNama\tHarga\tTipe")
        for i in range(len(listBarang)):
            print(f"{listBarang[i]["id"]}\t{listBarang[i]["nama"]}\t{listBarang[i]["harga"]}\t{listBarang[i]["tipe"]}")
    else:
        print("Barang kosong.")

# Fungsi Tampilkan Satuan
def tampilkanSatuan():
    if listBarang:
        tampilkanSemua()
        idSatuan = input("\nMasukan ID barang untuk menampilkan stok: ")
        hasilCari = cariID(idSatuan)
        if hasilCari:
            print(f"Jumlah stok {hasilCari["nama"]}: {hasilCari["stock"]}")
        else:
            print(f"Tidak ada barang dengan ID {idSatuan}")
    else:
        print("Barang kosong.")

# MENU TAMPILKAN BARANG
def menuTampil():
    while True:
        print("\nMENU TAMPILKAN BARANG")
        print("1. Tampilkan daftar barang")
        print("2. Tampilkan stok barang")
        print("3. Kembali")
        menuTampil = input("Silahkan pilih (1-3): ")
        if menuTampil == "1":
            tampilkanSemua()
        elif menuTampil == "2":
            tampilkanSatuan()
        elif menuTampil == "3":
            break
        else:
            print("Masukan anda salah, silahkan pilih menu (1-3)")

# Fungsi tambah barang 
def tambahBarang():
    while True:
        idBarang = input("\nMasukan ID barang: ")
        hasilCari = cariID(idBarang)
        if hasilCari:
            print(f"ID {idBarang} sudah terdaftar.")
        else:
            namaBarang = input("Masukan Nama barang: ")
            stokBarang = input("Masukan jumlah stok: ")
            hargaBarang = input("Masukan harga barang: ")
            tipeBarang = input("Masukan tipe barang: ")
            while True:
                confirmTambah = input(f"Anda yakin akan menambahkan {namaBarang} sebanyak {stokBarang} dengan harga {hargaBarang}? (y/t): ")
                if confirmTambah == "y":
                    listBarang.append({"id":idBarang, "nama":namaBarang, "stock": stokBarang, "harga": hargaBarang, "tipe": tipeBarang})
                    return print ("Data tersimpan!")
                elif confirmTambah == "t":
                    return print ("Data tidak disimpan.")
                else:
                    print("Input yang anda masukan salah (y/t): ")

# MENU TAMBAH BARANG
def menuTambah():
    while True:
        print("\nMENU TAMBAH BARANG")
        print("1. Tambahkan barang")
        print("2. Kembali")
        menuTampil = input("Silahkan pilih (1-2): ")
        if menuTampil == "1":
            tambahBarang()
        elif menuTampil == "2":
            break
        else:
            print("Masukan anda salah, silahkan pilih menu (1-2):")

# MENU UBAH BARANG
def ubahBarang():
    while True:
        print("\nMENU UBAH BARANG")
        print("1. Ubah barang")
        print("2. Kembali")
        menuUbah = input("Pilih menu (1-2): ")
        if menuUbah == "1":
            tampilkanSemua()
            idUbah = input("Masukan ID barang yang diubah: ")
            hasilCari = cariID(idUbah)
            if hasilCari:
                while True:
                    barangUbah = input(f"Anda yakin akan mengubah {hasilCari["nama"]}? (y/t) ")
                    if barangUbah == "y":
                        kolom = input("Masukan kolom yang diganti: ")
                        dataBaru = input("Masukan data baru: ")
                        while True:
                            confirmUbah = input(f"\nAnda yakin akan mengubah {kolom} {hasilCari["nama"]} menjadi {dataBaru}? (y/t): ")
                            if confirmUbah == "y":
                                hasilCari[kolom] = dataBaru
                                print ("Data tersimpan!")
                                break
                            elif confirmUbah == "t":
                                print ("Data tidak disimpan.")
                                break
                            else:
                                print("Input yang and masukan salah.")
                        break
                    elif barangUbah == "t":
                        print ("Data tidak disimpan.")
                        break
                    else:
                        print("\nInput yang and masukan salah (y/t): ")
            else:
                print(f"ID {idUbah} tidak terdaftar.")
        elif menuUbah == "2":
            break
        else:
            print("\nMasukan anda salah, silahkan pilih menu (1-2)")

#MENU HAPUS BARANG
def hapusBarang():
    while True:
        print("\nMENU HAPUS BARANG")
        print("1. Hapus barang")
        print("2. Kembali")
        menuHapus = input("Pilih menu (1-2): ")
        if menuHapus == "1":
            tampilkanSemua()
            idHapus = input("Masukan ID barang yang dihapus: ")
            hasilCari = cariID(idHapus)
            if hasilCari:
                while True:
                    barangHapus = input(f"Anda yakin akan menghapus {hasilCari["nama"]}? (y/t) ")
                    if barangHapus == "y":
                        listBarang.remove(hasilCari)
                        return print("Data terhapus!")
                    elif barangHapus == "t":
                        break
                    else:
                        print("Input yang anda masukan salah (y/t): ")
            else:
                print("Barang tidak terdaftar.")

        elif menuHapus == "2":
            break
        else:
            print("Masukan anda salah, silahkan pilih menu (1-2)")    

# Fungsi naikan harga
def naikanHarga():
    hargaTambah = int(input("Masukan penambahan harga: "))
    for x in range(len(listBarang)):
        listBarang[x]["harga"] += hargaTambah
    print("Data tersimpan, berikut data terbaru:")
    tampilkanSemua()

# Fungsi diskon barang dalam list
def diskonBarang(barang,diskon):
    return {"id": barang["id"], "nama": barang["nama"], "stock": barang["stock"], "harga": int ( barang["harga"] * (100-diskon)/100 ), "tipe": barang["tipe"]}

# Fungsi diskon semua harga
def diskonHarga():
    global listBarang
    diskon = int( input("Masukan diskon dalam persen (%): "))
    listBarang = list(map(lambda barang: diskonBarang(barang, diskon), listBarang))   
    print("Data tersimpan, berikut data terbaru:")
    tampilkanSemua()

# Fungsi Urutkan termurah
def urutkanTermurah():
    global listBarang
    listBarang = sorted(listBarang, key=lambda barang: barang["harga"])
    print("Data tersimpan, berikut data terbaru:")
    tampilkanSemua()

# Fungsi Urutkan termahal
def urutkanTermahal():
    global listBarang
    listBarang = sorted(listBarang, key=lambda barang: barang["harga"], reverse=True)
    print("Data tersimpan, berikut data terbaru:")
    tampilkanSemua()
    
# Fungsi filter barang
def filterBarang():
    min_harga = int(input("Masukan batas bawah: ")) 
    max_harga = int(input("Masukan batas atas: "))
    listBarangFilter = list(filter(lambda barang: min_harga <= barang["harga"] <= max_harga, listBarang))
    print("Berikut data filter:")
    print("\nID\tNama\tHarga\tTipe")
    for i in range(len(listBarangFilter)):
        print(f"{listBarangFilter[i]["id"]}\t{listBarangFilter[i]["nama"]}\t{listBarangFilter[i]["harga"]}\t{listBarangFilter[i]["tipe"]}")

# MENU FITUR TAMBAHAN
def fiturTambahan():
    while True:
        print("\nMENU FITUR TAMBAHAN")
        print("1. Naikan harga semua barang")
        print("2. Diskon semua barang")
        print("3. Urutkan barang dari yang termurah")
        print("4. Urutkan barang dari yang termahal")
        print("5. Filter berdasar harga")
        print("6. Kembali")
        menuTambahan = input("Silahkan pilih (1-6): ")
        if menuTambahan == '1':
            naikanHarga()
        elif menuTambahan == '2':
            diskonHarga()
        elif menuTambahan == '3':
            urutkanTermurah()
        elif menuTambahan == '4':
            urutkanTermahal()
        elif menuTambahan == '5':
            filterBarang()
        elif menuTambahan == "6":
            break
        else:
            print("Masukan anda salah, silahkan pilih menu (1-6): ") 

# MENU UTAMA
while True:
    menu = input('''
MENU UTAMA
1. Tampilkan barang
2. Tambah barang                 
3. Ubah barang
4. Hapus barang
5. Fitur tambahan
6. Selesai                 
Silahkan pilih menu (1-6): ''')

    if menu == "1":
        menuTampil()
    elif menu == "2":
        menuTambah()
    elif menu == "3":
        ubahBarang()
    elif menu == "4":
        hapusBarang()
    elif menu == "5":
        fiturTambahan()
    elif menu == "6":
        print("Program dimatikan...")
        break
    else:
        print("Masukan anda salah, silahkan ketik menu (1-6)")