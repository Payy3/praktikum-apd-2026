mahasiswa = {
    "nama": "Nawfal",
    "NIM": "2509106076",
    "prodi": "Informatika",
    "semester": 1
}
print("=== Dictionary awal ===")
print(mahasiswa)
awal = mahasiswa.copy()  

mahasiswa["alamat"] = "Samarinda"
mahasiswa["email"] = "fahry@email.com"
print("=== Setelah tambah alamat & email ===")
print(mahasiswa)
setelah_tambah = mahasiswa.copy()

mahasiswa["semester"] = mahasiswa["semester"] + 1
print("=== Setelah semester diubah ===")
print(mahasiswa)
setelah_ubah = mahasiswa.copy()

print("Jumlah item:", len(mahasiswa))

print("=== Isi Dictionary (for + items) ===")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")

terhapus = mahasiswa.pop("alamat")
print("Nilai yang dihapus:", terhapus)
print("=== Setelah pop alamat ===")
print(mahasiswa)

print("=== PERBANDINGAN ===")
print(f"{'Tahap':<22}{'Jumlah item':<14}{'Semester'}")
print(f"{'Awal':<22}{len(awal):<14}{awal['semester']}")
print(f"{'Tambah alamat+email':<22}{len(setelah_tambah):<14}{setelah_tambah['semester']}")
print(f"{'Ubah semester':<22}{len(setelah_ubah):<14}{setelah_ubah['semester']}")
print(f"{'Setelah pop alamat':<22}{len(mahasiswa):<14}{mahasiswa['semester']}")