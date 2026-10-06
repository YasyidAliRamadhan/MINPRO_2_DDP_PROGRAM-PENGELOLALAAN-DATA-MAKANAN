# MINPRO_2_DDP_PROGRAM PENGELOLALAAN DATA MAKANAN

NAMA: YASYID ALI RAMADHAN

NIM: 2609116072

KELAS: B

**1. Deskripsi Singkat Program**

Program yang dibuat adalah Program Manajemen Menu Makanan. Program ini digunakan untuk mengelola daftar makanan dan minuman dengan dua jenis pengguna, yaitu penjual dan pembeli. Data akun dan data menu disimpan menggunakan Dictionary. Penjual memiliki akses untuk melihat, menambah, mengubah, dan menghapus menu, sedangkan pembeli hanya dapat melihat daftar menu.

**2. Penjelasan Alur Flowchart**

**A. Mulai dan Menu Utama**

Program dimulai dari Mulai, kemudian menampilkan menu utama yang memiliki dua pilihan:

- Login
- Selesai

Pengguna kemudian memasukkan pilihan. Jika memilih 2, program menampilkan pesan "Program selesai." dan program berhenti. Jika memilih 1, program masuk ke proses login.

**B. Proses Login**

Pengguna memasukkan username dan password. Password dimasukkan menggunakan pwinput sehingga password tidak terlihat secara langsung ketika diketik. Program kemudian mengecek apakah username terdapat di dalam dictionary akun dan apakah password yang dimasukkan sesuai.

Jika login berhasil, program mengambil role dari akun tersebut. Jika login gagal, program menampilkan pesan kesalahan dan kembali ke menu utama.

**C. Pengecekan Role**

Setelah berhasil login, program mengecek role pengguna.

Jika role penjual, program menjalankan menu_penjual().
Jika role pembeli, program menjalankan menu_pembeli().

**D. Menu Penjual**

Penjual memiliki lima pilihan:

- Lihat Menu
- Tambah Menu
- Ubah Menu
- Hapus Menu
- Logout

Pilihan 1 sampai 4 digunakan untuk mengelola data menu. Pilihan 5 digunakan untuk logout dan kembali ke menu utama. Menu penjual menggunakan perulangan while True, sehingga menu akan terus ditampilkan sampai penjual memilih logout.

**E. Menu Pembeli**

Pembeli memiliki dua pilihan:

- Lihat Menu
- Logout

Pembeli hanya dapat melihat daftar menu dan tidak memiliki akses untuk menambah, mengubah, atau menghapus menu. Jika memilih logout, pengguna kembali ke menu utama.

**F. Pengelolaan Menu**

Pada bagian pengelolaan menu:

- Tambah menu → memasukkan nama, kategori, dan harga.
- Ubah menu → memilih nomor menu kemudian mengubah datanya.
- Hapus menu → memilih nomor menu yang ingin dihapus.
- Lihat menu → menampilkan seluruh data menu.

Program juga melakukan pengecekan agar data tidak kosong dan harga harus berupa angka.

**3. Dokumentasi Program dan Output**

**A. Login**

Ini adalah program pembuatan login nya:

<img width="467" height="313" alt="image" src="https://github.com/user-attachments/assets/29be9df5-1c08-48b1-93c6-8f59578c1891" />


Program menyediakan dua akun, yaitu:

| Username  | Password | Role    |
| --------- | -------- | ------- |
| `penjual` | `12345`  | Penjual |
| `pembeli` | `54321`  | Pembeli |

Ini adalah programnya:

<img width="134" height="101" alt="Screenshot 2026-10-06 214342" src="https://github.com/user-attachments/assets/a4958a8f-0159-40b6-a4f6-846d2e60a5bb" />

Pengguna akan diminta memasukin password yang telah dibuat tadi.

<img width="85" height="46" alt="Screenshot 2026-10-06 214941" src="https://github.com/user-attachments/assets/63ea819c-717a-46d7-9fe2-c386630b53fd" />

Disini kita bisa memasukkan 2 role yang ingin kita akses yaitu penjual dan pembeli.


**Role Penjual.**

Penjual akan diminta memasukin username dan password yang telah dibuat.

contoh:

<img width="143" height="75" alt="Screenshot 2026-10-06 215718" src="https://github.com/user-attachments/assets/e3ebbec8-b9f9-4e5a-87b9-59efe7e1c9a3" />

Ini adalah menu role penjual dia dapat melihat menu, menambah menu, mengubah menu, dan menghapus menu

contoh program:

<img width="179" height="82" alt="Screenshot 2026-10-06 215450" src="https://github.com/user-attachments/assets/17e07f45-5bf8-4c3c-a087-c3ec52d7ffc3" />

Dan ini adalah output yang berhasil dijalankan program.

contoh output:

<img width="149" height="116" alt="Screenshot 2026-10-06 215748" src="https://github.com/user-attachments/assets/0f745486-94aa-4dde-bb81-0424972f4b55" />

**Role Pembeli.**

Ini adalah menu role pembeli dia hanya dapat melihat menu.

contoh program:

<img width="399" height="115" alt="image" src="https://github.com/user-attachments/assets/b2b8dcf6-6f6d-47f1-8867-6bee978fa53e" />

Dan ini adalah output yang berhasil dijalankan program.

contoh output:

<img width="113" height="97" alt="Screenshot 2026-10-06 221957" src="https://github.com/user-attachments/assets/b51a64a6-ad05-4721-8af5-80a1231b6018" />

**B. Menampilkan Menu**

Data awal program terdiri dari:

| No | Nama        | Kategori |    Harga |
| -- | ----------- | -------- | -------: |
| 1  | Nasi Goreng | Makanan  | Rp15.000 |
| 2  | Mie Ayam    | Makanan  | Rp12.000 |
| 3  | Es Teh      | Minuman  |  Rp5.000 |


Ini adalah program saat penjual/pembeli memilih nomor 1 "lihat menu".

contoh program:

<img width="184" height="167" alt="Screenshot 2026-10-06 221216" src="https://github.com/user-attachments/assets/321a42b1-62bf-4cb2-8651-9cec14a5d33e" />

Ini adalah output yang berhasil dijalankan program. Program akan menampilkan daftar menu.

<img width="295" height="217" alt="image" src="https://github.com/user-attachments/assets/f7c7e257-d46c-4339-b149-25265b46f313" />

**C. Tambah Menu**

Penjual dapat memilih menu Tambah Menu, kemudian memasukkan nama, kategori, dan harga. Tetapi kategori nya tidak boleh kosong, dan harga harus berupa angka, jika tidak menu tidak akan tertambah.

contoh program:

<img width="463" height="411" alt="image" src="https://github.com/user-attachments/assets/626dcc9b-14ed-4a22-a6fb-63989f644278" />

Pengguna akan diminta menu apa yang ingin ditambah. dan ketika berhasil ditambahkan akan muncul tulisan "Menu Berhasil Ditambahkan"

contoh:

<img width="342" height="238" alt="image" src="https://github.com/user-attachments/assets/76ffae3f-b4b4-406b-91c7-2901d1776175" />


Jika program berhasil maka menu di daftar menu akan otomatis tertambah.

contoh:

<img width="149" height="49" alt="Screenshot 2026-10-06 222428" src="https://github.com/user-attachments/assets/33d35958-5512-4226-ab75-a0e1c805d139" />

**D. Ubah Menu**

Penjual dapat memilih nomor menu yang ingin diubah. Tetapi kategori nya tidak boleh kosong, dan harga harus berupa angka, jika tidak menu tidak akan terubah.

contoh program:

<img width="531" height="503" alt="image" src="https://github.com/user-attachments/assets/a5d7c85b-5eed-4f96-8ab9-710a26fed906" />

Pengguna akan diminta nomor menu mana yang ingin diubah. dan ketika berhasil ditambahkan akan muncul tulisan "Menu Berhasil Diubah"

contoh: 

<img width="185" height="172" alt="Screenshot 2026-10-06 223042" src="https://github.com/user-attachments/assets/46af6e3c-19b8-456e-b5f7-cc10cc79ad3a" />

Jika program berhasil maka menu di daftar menu akan otomatis terubah.

<img width="148" height="58" alt="Screenshot 2026-10-06 223051" src="https://github.com/user-attachments/assets/c722ac28-345b-48c4-ac2a-e033b7b1da4f" />

**E. Hapus Menu**

Penjual dapat menghapus menu berdasarkan nomor menu yang dipilih di daftar menu. Dan nomor nya harus ada di daftar menu, dan berupa angka, jika tidak program tidak dapat memproses nya

contoh program:

<img width="524" height="235" alt="image" src="https://github.com/user-attachments/assets/03ca5913-2931-4183-8a92-883f06dc6d2a" />

Pengguna akan diminta nomor menu mana yang ingin dihapus. dan ketika berhasil dihapus akan muncul tulisan "Menu Berhasil Dihapus"

contoh:

<img width="367" height="281" alt="image" src="https://github.com/user-attachments/assets/e967ec96-7d1e-4981-ad70-6f5eaf32984a" />

Jika program berhasil maka menu di daftar menu akan otomatis terhapus.

contoh:

<img width="286" height="219" alt="image" src="https://github.com/user-attachments/assets/8349479f-b8dd-40bb-8b4e-6aad04685ff8" />

**F. Validasi Input**

Program memiliki beberapa validasi sederhana. Contohnya, jika harga tidak berupa angka:

<img width="240" height="237" alt="image" src="https://github.com/user-attachments/assets/574b92b6-3df9-482a-a35f-11e31723eac4" />

jika data tidak diiisi:

<img width="249" height="247" alt="image" src="https://github.com/user-attachments/assets/67851dcd-5188-4402-8539-264dd3eb7d5c" />

Validasi ini dibuat menggunakan if dan elif.

**4. Penjelasan Penerapan Nilai Tambah**

Program menerapkan 1 library Python, yaitu pwinput. Library tersebut digunakan pada proses login untuk menerima password tanpa menampilkan karakter password secara langsung pada terminal.

contoh program: 

<img width="389" height="105" alt="image" src="https://github.com/user-attachments/assets/32fc03d6-9e85-4632-8268-0a25be8bf19d" />

Dengan penggunaan pwinput, ketika pengguna memasukkan password, password tidak ditampilkan secara jelas pada layar/di blur. Hal ini membuat proses login menjadi lebih aman.

contoh output:

<img width="299" height="142" alt="image" src="https://github.com/user-attachments/assets/0dde5185-531e-49ab-bdb8-a2a547d2e49b" />


- **FLOWCHART**

<img width="1179" height="1471" alt="FLOWCHART drawio" src="https://github.com/user-attachments/assets/30dd2be4-b37e-45d9-a555-ea85f3b79c1e" />

























































