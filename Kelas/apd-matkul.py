
mahasiswa = {
    "nama": "Nawfal",
    "NIM": "2509106076",
    "prodi": "Informatika",
    "semester": 1
}
print("=== Dictionary awal ===")
print(mahasiswa)

mahasiswa["alamat"] = "Samarinda"
mahasiswa["email"] = "nawfal@email.com"
print("\n=== Setelah ditambah alamat dan email ===")
print(mahasiswa)

mahasiswa["semester"] += 1
print("\n=== Setelah semester diubah ===")
print("Semester sekarang:", mahasiswa["semester"])

print("\nJumlah item:", len(mahasiswa))

print("\n=== Isi dictionary ===")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")

# 6. Hapus key alamat dengan pop()
alamat_dihapus = mahasiswa.pop("alamat")
print("\nAlamat yang dihapus:", alamat_dihapus)
print("=== Dictionary setelah pop ===")
print(mahasiswa)
print("Jumlah item sekarang:", len(mahasiswa))