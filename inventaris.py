import json

path = r"C:\Users\hp\OneDrive\Documents\vscode shaina\studkas 6\inventaris.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(kode, nama, kategori, stok):
    data.append({"kode": kode, "nama": nama, "kategori": kategori, "stok": stok})
    return "data berhasil ditambahkan."

def simpan_file():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Data berhasil disimpan ke inventaris.json!"

while True:
    print("\n=== INVENTARIS BARANG ===")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Keluar")

    pilihan = input("pilih menu: ")

    if pilihan == "1":
        print("\n ===== data inventaris barang =====")
        print(data)

    elif pilihan == "2":
        kode = input("masukkan kode: ")
        nama = input("masukkan nama: ")
        kategori = input("masukkan kategori: ")
        stok = input("masukkan stok: ")

        print("\n", tambah_data(kode, nama, kategori, stok))
        print(simpan_file())

    elif pilihan == "3":
        print("program selesai.")
        break

    else:
        print("pilihan tidak valid.")