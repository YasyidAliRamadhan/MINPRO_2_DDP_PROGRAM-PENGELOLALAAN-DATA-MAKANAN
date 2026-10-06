import pwinput

# Dictionary akun
akun = {
    "penjual": {
        "password": "12345",
        "role": "penjual"
    },
    "pembeli": {
        "password": "54321",
        "role": "pembeli"
    }
}

# Dictionary menu makanan
menu = {
    1: {
        "nama": "Nasi Goreng",
        "kategori": "Makanan",
        "harga": 15000
    },
    2: {
        "nama": "Mie Ayam",
        "kategori": "Makanan",
        "harga": 12000
    },
    3: {
        "nama": "Es Teh",
        "kategori": "Minuman",
        "harga": 5000
    }
}


# Function untuk login
def login():
    print("\n===== LOGIN =====")

    username = input("Username : ")
    password = pwinput.pwinput("Password : ")

    if username in akun:
        if password == akun[username]["password"]:
            print("Login berhasil!")
            return akun[username]["role"]
        else:
            print("Password salah!")
            return ""
    else:
        print("Username tidak ditemukan!")
        return ""


# Function untuk menampilkan menu
def tampilkan_menu():
    print("\n===== DAFTAR MENU =====")

    for nomor in menu:
        print(
            nomor,
            menu[nomor]["nama"],
            "-",
            menu[nomor]["kategori"],
            "- Rp",
            menu[nomor]["harga"]
        )


# Function untuk menambah menu
def tambah_menu():
    print("\n===== TAMBAH MENU =====")

    nama = input("Nama menu : ")
    kategori = input("Kategori : ")
    harga = input("Harga : ")

    if nama == "" or kategori == "" or harga == "":
        print("Data tidak boleh kosong!")
    elif not harga.isdigit():
        print("Harga harus berupa angka!")
    else:
        nomor = max(menu) + 1

        menu[nomor] = {
            "nama": nama,
            "kategori": kategori,
            "harga": int(harga)
        }

        print("Menu berhasil ditambahkan!")


# Function untuk mengubah menu
def ubah_menu():
    tampilkan_menu()

    nomor = input("\nMasukkan nomor menu yang ingin diubah : ")

    if not nomor.isdigit():
        print("Nomor harus berupa angka!")
    elif int(nomor) not in menu:
        print("Menu tidak ditemukan!")
    else:
        nomor = int(nomor)

        nama = input("Nama baru : ")
        kategori = input("Kategori baru : ")
        harga = input("Harga baru : ")

        if nama == "" or kategori == "" or harga == "":
            print("Data tidak boleh kosong!")
        elif not harga.isdigit():
            print("Harga harus berupa angka!")
        else:
            menu[nomor]["nama"] = nama
            menu[nomor]["kategori"] = kategori
            menu[nomor]["harga"] = int(harga)

            print("Menu berhasil diubah!")


# Function untuk menghapus menu
def hapus_menu():
    tampilkan_menu()

    nomor = input("\nMasukkan nomor menu yang ingin dihapus : ")

    if not nomor.isdigit():
        print("Nomor harus berupa angka!")
    elif int(nomor) not in menu:
        print("Menu tidak ditemukan!")
    else:
        del menu[int(nomor)]
        print("Menu berhasil dihapus!")


# Menu khusus penjual
def menu_penjual():
    while True:
        print("\n===== MENU PENJUAL =====")
        print("1. Lihat Menu")
        print("2. Tambah Menu")
        print("3. Ubah Menu")
        print("4. Hapus Menu")
        print("5. Logout")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tampilkan_menu()

        elif pilihan == "2":
            tambah_menu()

        elif pilihan == "3":
            ubah_menu()

        elif pilihan == "4":
            hapus_menu()

        elif pilihan == "5":
            print("Logout berhasil!")
            break

        else:
            print("Pilihan tidak tersedia!")


# Menu khusus user
def menu_pembeli():
    while True:
        print("\n===== MENU PEMBELI =====")
        print("1. Lihat Menu")
        print("2. Logout")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tampilkan_menu()

        elif pilihan == "2":
            print("Logout berhasil!")
            break

        else:
            print("Pilihan tidak tersedia!")


# Program utama
while True:
    print("\n===== MANAJEMEN MENU MAKANAN =====")
    print("1. Login")
    print("2. Selesai")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        role = login()

        if role == "penjual":
            menu_penjual()

        elif role == "pembeli":
            menu_pembeli()

    elif pilihan == "2":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")