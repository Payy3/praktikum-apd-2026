import os

users = {
    "admin": {"password": "admin76", "role": "admin"},
    "steve": {"password": "steve123", "role": "user"}
}

kategori = ("Any% Random Seed", "Any% Set Seed", "All Achievements", "Glitchless")

runs = {
    1: {"pemain": "Steve", "kategori": "Any% Set Seed", "menit": 9, "detik": 58, "pengirim": "steve"},
    2: {"pemain": "Clementdav", "kategori": "Any% Random Seed", "menit": 9, "detik": 22, "pengirim": "Clementdav"},
    3: {"pemain": "Dream", "kategori": "Any% Random Seed", "menit": 19, "detik": 24, "pengirim": "Dream"},
    4: {"pemain": "Herobrine", "kategori": "Any% Random Seed", "menit": 1, "detik": 11, "pengirim": "admin"}
}
id_berikut = 5

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_tabel_run(daftar_id):
    print(f"{'ID':<5}{'Pemain':<18}{'Kategori':<20}{'Waktu':<9}{'Pengirim'}")
    print("-" * 60)
    for id_run in daftar_id:
        r = runs[id_run]
        print(f"{id_run:<5}{r['pemain']:<18}{r['kategori']:<20}{r['menit']:02d}:{r['detik']:02d}    {r['pengirim']}")

def ke_detik(menit, detik):
    total = menit * 60 + detik
    return total

def login_rekursif(sisa):
    if sisa == 0:
        return None
    user_in = input("Username: ").strip()
    pass_in = input("Password: ").strip()
    if user_in in users and users[user_in]["password"] == pass_in:
        return user_in
    print(f"Login gagal! Sisa percobaan: {sisa - 1}")
    return login_rekursif(sisa - 1)


def pilih_kategori():
    for i in range(len(kategori)):
        print(f"{i + 1}. {kategori[i]}")
    pilihan = input("Pilih kategori: ").strip()
    try:
        nomor = int(pilihan)
        if 1 <= nomor <= len(kategori):
            return kategori[nomor - 1]
        print("Nomor kategori di luar jangkauan!")
    except ValueError:
        print("Kategori harus berupa angka!")
    return None

def buat_id_baru():
    global id_berikut
    id_baru = id_berikut 
    id_berikut += 1
    return id_baru


while True:
    bersihkan_layar()
    print("=" * 45)
    print("   PEMERINGKATAN SPEEDRUN MINECRAFT")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu [1-3]: ").strip()

    if pilih == "1":
        bersihkan_layar()
        print("=== LOGIN ===")
        username = login_rekursif(3)

        if username is None:
            print("Terlalu banyak percobaan gagal. Kembali ke menu utama.")
            input("Tekan Enter untuk lanjut...")
        else:
            role = users[username]["role"]

            while True:
                bersihkan_layar()
                print("=" * 45)
                print(f"   MENU {role.upper()} - {username}")
                print("=" * 45)
                print("1. Tambah Run")
                print("2. Lihat Ranking")
                print("3. Ubah Run")
                print("4. Hapus Run")
                if role == "admin":
                    print("5. Lihat Daftar User")
                    print("6. Logout")
                else:
                    print("5. Logout")
                menu = input("Pilih menu: ").strip()

                logout = (menu == "6" and role == "admin") or (menu == "5" and role == "user")

                if logout:
                    break

                elif menu == "1":
                    bersihkan_layar()
                    print("=== TAMBAH RUN ===")
                    pemain = input("Nama pemain: ").strip()
                    if pemain == "":
                        print("Nama pemain tidak boleh kosong!")
                    else:
                        nama_kat = pilih_kategori()
                        if nama_kat is not None:
                            try:
                                menit = int(input("Waktu - menit: ").strip())
                                detik = int(input("Waktu - detik: ").strip())
                                if menit < 0 or detik < 0 or detik > 59:
                                    print("Menit tidak boleh negatif, detik harus 0-59!")
                                elif ke_detik(menit, detik) == 0:
                                    print("Waktu tidak boleh 00:00!")
                                else:
                                    id_run = buat_id_baru()
                                    runs[id_run] = {
                                        "pemain": pemain,
                                        "kategori": nama_kat,
                                        "menit": menit,
                                        "detik": detik,
                                        "pengirim": username
                                    }
                                    print("Run berhasil ditambahkan!")
                            except ValueError:
                                print("Menit dan detik harus berupa angka bulat!")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "2":
                    bersihkan_layar()
                    print("=== RANKING SPEEDRUN ===")
                    nama_kat = pilih_kategori()
                    if nama_kat is not None:

                        tampil = []
                        for id_run in runs:
                            if runs[id_run]["kategori"] == nama_kat:
                                tampil.append(id_run)

                        for i in range(len(tampil)):
                            for j in range(len(tampil) - i - 1):
                                a = runs[tampil[j]]
                                b = runs[tampil[j + 1]]
                                if ke_detik(a["menit"], a["detik"]) > ke_detik(b["menit"], b["detik"]):
                                    temp = tampil[j]
                                    tampil[j] = tampil[j + 1]
                                    tampil[j + 1] = temp

                        print()
                        print(f"Ranking kategori: {nama_kat}")
                        if len(tampil) == 0:
                            print("Belum ada data run pada kategori ini.")
                        else:
                            print(f"{'Rank':<6}{'Pemain':<18}{'Waktu':<10}{'Pengirim'}")
                            print("-" * 45)
                            for i in range(len(tampil)):
                                r = runs[tampil[i]]
                                print(f"{i + 1:<6}{r['pemain']:<18}{r['menit']:02d}:{r['detik']:02d}     {r['pengirim']}")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "3":
                    bersihkan_layar()
                    print("=== UBAH RUN ===")
                    bisa = []
                    for id_run in runs:
                        if role == "admin" or runs[id_run]["pengirim"] == username:
                            bisa.append(id_run)

                    if len(bisa) == 0:
                        print("Tidak ada data yang dapat diubah.")
                    else:
                        tampilkan_tabel_run(bisa)
                        try:
                            idx = int(input("ID run yang diubah: ").strip())
                            if idx in bisa:
                                menit_lama = runs[idx]["menit"]
                                detik_lama = runs[idx]["detik"]
                                print("Kosongkan input jika tidak ingin mengubah.")

                                baru = input(f"Pemain [{runs[idx]['pemain']}]: ").strip()
                                if baru != "":
                                    runs[idx]["pemain"] = baru

                                ubah_kat = input(f"Ubah kategori [{runs[idx]['kategori']}]? (y/n): ").strip().lower()
                                if ubah_kat == "y":
                                    kat_baru = pilih_kategori()
                                    if kat_baru is not None:
                                        runs[idx]["kategori"] = kat_baru
                                    else:
                                        print("Kategori tidak diubah.")

                                menit_baru = input(f"Menit [{runs[idx]['menit']}]: ").strip()
                                if menit_baru != "":
                                    try:
                                        if int(menit_baru) < 0:
                                            print("Menit tidak boleh negatif, tidak diubah.")
                                        else:
                                            runs[idx]["menit"] = int(menit_baru)
                                    except ValueError:
                                        print("Menit harus angka, tidak diubah.")

                                detik_baru = input(f"Detik [{runs[idx]['detik']}]: ").strip()
                                if detik_baru != "":
                                    try:
                                        if 0 <= int(detik_baru) <= 59:
                                            runs[idx]["detik"] = int(detik_baru)
                                        else:
                                            print("Detik harus 0-59, tidak diubah.")
                                    except ValueError:
                                        print("Detik harus angka, tidak diubah.")

                                if ke_detik(runs[idx]["menit"], runs[idx]["detik"]) == 0:
                                    runs[idx]["menit"] = menit_lama
                                    runs[idx]["detik"] = detik_lama
                                    print("Waktu tidak boleh 00:00, waktu dikembalikan.")
                                print("Proses update selesai.")
                            else:
                                print("ID tidak valid atau bukan milik Anda!")
                        except ValueError:
                            print("ID harus berupa angka!")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "4":
                    bersihkan_layar()
                    print("=== HAPUS RUN ===")
                    bisa = []
                    for id_run in runs:
                        if role == "admin" or runs[id_run]["pengirim"] == username:
                            bisa.append(id_run)

                    if len(bisa) == 0:
                        print("Tidak ada data yang dapat dihapus.")
                    else:
                        tampilkan_tabel_run(bisa)
                        try:
                            idx = int(input("ID run yang dihapus: ").strip())
                            if idx in bisa:
                                yakin = input(f"Hapus run {runs[idx]['pemain']}? (y/n): ").strip().lower()
                                if yakin == "y":
                                    runs.pop(idx)
                                    print("Run berhasil dihapus!")
                                else:
                                    print("Penghapusan dibatalkan.")
                            else:
                                print("ID tidak valid atau bukan milik Anda!")
                        except ValueError:
                            print("ID harus berupa angka!")
                    input("Tekan Enter untuk lanjut...")

                elif menu == "5" and role == "admin":
                    bersihkan_layar()
                    print("=== DAFTAR USER ===")
                    print(f"{'No':<5}{'Username':<18}{'Role'}")
                    print("-" * 35)
                    nomor = 1
                    for nama in users:
                        print(f"{nomor:<5}{nama:<18}{users[nama]['role']}")
                        nomor += 1
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("Menu tidak valid!")
                    input("Tekan Enter untuk lanjut...")

    elif pilih == "2":
        bersihkan_layar()
        print("=== REGISTER ===")
        user_baru = input("Username baru: ").strip()
        pass_baru = input("Password baru: ").strip()

        sudah_ada = False
        for nama in users:
            if nama.lower() == user_baru.lower():
                sudah_ada = True

        if user_baru == "" or pass_baru == "":
            print("Username dan password tidak boleh kosong!")
        elif len(user_baru) < 3:
            print("Username minimal 3 karakter!")
        elif len(pass_baru) < 4:
            print("Password minimal 4 karakter!")
        elif sudah_ada:
            print("Username sudah dipakai!")
        else:
            users[user_baru] = {"password": pass_baru, "role": "user"}
            print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    elif pilih == "3":
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")