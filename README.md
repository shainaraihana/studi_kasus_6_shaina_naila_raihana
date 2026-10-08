# studi_kasus_6_shaina_naila_raihana

Nama: Shaina Naila Raihana

NIM: 2609116090

Kelas: C


# Sistem Manajemen Inventaris Barang

Program ini dibuat untuk membantu toko kelontong dalam mengelola data inventaris barang. Program menggunakan file JSON sebagai tempat penyimpanan data. Pengguna dapat melihat seluruh data barang dan menambahkan barang baru. Data yang ditambahkan akan disimpan ke dalam file sehingga tidak hilang ketika program dijalankan kembali.

**Data JSON**

Data barang disimpan dalam file inventaris.json.

Isi awal:

<img width="1708" height="629" alt="Screenshot (522)" src="https://github.com/user-attachments/assets/74b632d8-29b0-454b-8495-3f9238b2ab84" />

Setiap data barang memiliki kode, nama, kategori, dan stok.

**Penjelasan Program**

1. Import JSON

<img width="128" height="12" alt="Screenshot 2026-10-08 223504" src="https://github.com/user-attachments/assets/37b2f136-ca27-407c-b97e-d8243094b9a6" />

Library json digunakan untuk membaca data dari file JSON dan menyimpan data ke dalam file JSON.

2. Menentukan lokasi file

<img width="524" height="11" alt="Screenshot 2026-10-08 223548" src="https://github.com/user-attachments/assets/865f3832-9626-459d-9762-fe61f3c852b5" />

path digunakan untuk menentukan lokasi file inventaris.json yang digunakan untuk menyimpan data inventaris.

3. Membaca data dari JSON

<img width="263" height="30" alt="Screenshot 2026-10-08 223708" src="https://github.com/user-attachments/assets/3f3d3c7b-2f3a-4148-86b3-b74d150f1898" />

Program membuka file JSON dalam mode "r" atau read, kemudian json.load() digunakan untuk mengambil data dari file dan menyimpannya ke variabel data.

4. Fungsi Menambahkan Data

<img width="476" height="50" alt="Screenshot 2026-10-08 223803" src="https://github.com/user-attachments/assets/0d9ea01c-356c-4883-9c34-c1095f266c76" />

Fungsi tambah_data() digunakan untuk menambahkan barang baru.

Bagian:

<img width="524" height="11" alt="Screenshot 2026-10-08 223548" src="https://github.com/user-attachments/assets/2d2f5436-b670-41d6-9e0b-1f264c4085b2" />

digunakan untuk memasukkan data baru ke dalam data yang sudah ada.

Misalnya pengguna memasukkan:

<img width="1846" height="358" alt="Screenshot (523)" src="https://github.com/user-attachments/assets/7c4d4f91-59b8-4a50-9042-008e1f80efa8" />

Maka data tersebut akan ditambahkan ke dalam data.

5. Fungsi Menyimpan Data

<img width="333" height="64" alt="Screenshot 2026-10-08 223831" src="https://github.com/user-attachments/assets/0075eb94-1286-42c6-a2d4-3c15f8de195b" />

Fungsi simpan_file() digunakan untuk menyimpan data yang sudah ditambahkan ke dalam file JSON.

"w" berarti write, yaitu menulis atau memperbarui isi file.

Sedangkan:

<img width="199" height="15" alt="Screenshot 2026-10-08 230423" src="https://github.com/user-attachments/assets/96084671-8293-4ced-bee0-4bdd0049bb61" />

digunakan untuk memasukkan data dari program ke dalam file inventaris.json.

Jadi data baru tidak hanya muncul di program, tetapi benar-benar tersimpan di file.

6. While Loop dan Menu

<img width="245" height="79" alt="Screenshot 2026-10-08 230510" src="https://github.com/user-attachments/assets/22bdcd57-2fbd-44d2-b01a-23bec2a1e83a" />

while True membuat program terus berjalan dan menampilkan menu berulang kali.

Program baru berhenti ketika pengguna memilih menu 3.

7. Menampilkan Data

Jika pengguna memilih menu 1:

<img width="319" height="53" alt="Screenshot 2026-10-08 230654" src="https://github.com/user-attachments/assets/7768e0bf-0d02-4c5a-b5bb-0281618a36e4" />

Menu 1 digunakan untuk menampilkan seluruh data inventaris barang yang sudah dibaca dari file inventaris.json. Data ditampilkan menggunakan print(data).

**OUTPUT:**

<img width="1847" height="526" alt="Screenshot (526)" src="https://github.com/user-attachments/assets/5a9eb4a5-f26f-49c0-8a31-6279a7c0d53b" />

8. Menambahkan Data

Jika pengguna memilih menu 2:

<img width="353" height="113" alt="Screenshot 2026-10-08 230950" src="https://github.com/user-attachments/assets/dc107f38-28e4-4caf-8f14-eaeac5625ecb" />

Program meminta pengguna memasukkan data barang.

Contohnya:

<img width="239" height="33" alt="Screenshot 2026-10-08 231750" src="https://github.com/user-attachments/assets/21302fc7-2cad-450e-b09b-f476ab869fcd" />

kemudian:

<img width="549" height="80" alt="Screenshot (523)" src="https://github.com/user-attachments/assets/e1661a90-30ae-49b5-94f4-ab452772a269" />

Data B004 kemudian masuk ke data menggunakan data.append(), lalu disimpan ke JSON menggunakan json.dump().

<img width="1844" height="869" alt="Screenshot (527)" src="https://github.com/user-attachments/assets/e55b32d6-f01f-4d5d-aa8c-8810235827f6" />

9. Keluar dari Program

Jika pengguna memilih 3:

<img width="178" height="56" alt="Screenshot 2026-10-08 231230" src="https://github.com/user-attachments/assets/c159783a-01be-43ea-b14f-15ae00073888" />

break digunakan untuk menghentikan while loop, sehingga program selesai.

Kesimpulan

Program ini menggunakan JSON sebagai penyimpanan data, def untuk membuat fungsi tambah_data() dan simpan_file(), serta while loop agar program dapat berjalan terus sampai pengguna memilih keluar. Data barang baru ditambahkan menggunakan append() dan disimpan secara permanen menggunakan json.dump().
