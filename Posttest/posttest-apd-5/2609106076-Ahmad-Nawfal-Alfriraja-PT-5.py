import os

# DATA
users = [
    ["admin", "admin76", "admin"],
    ["steve", "steve123", "user"]
]

# Tuple kategori speedrun
kategori = ("Any% Random Seed", "Any% Set Seed", "All Achievements", "Glitchless")

# Runs: [pemain, kategori, menit, detik, pengirim]
runs = [
    ["Steve", "Any% Set Seed", 9, 58, "steve"],
    ["Clementdav", "Any% Random Seed", 9, 22, "Clementdav"],
    ["Dream", "Any% Random Seed", 19, 24, "Dream"],
    ["Herobrine", "Any% Random Seed", 1, 11, "admin"] 
]

# PROGRAM UTAMA
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 45)
    print("   PEMERINGKATAN SPEEDRUN MINECRAFT")
    print("=" * 45)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu [1-3]: ").strip()

    # LOGIN
    if pilih == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        berhasil = False
        percobaan = 0
        akun = []
        while percobaan < 3 and berhasil == False:
            user_in = input("Username: ").strip()
            pass_in = input("Password: ").strip()
            for u in users:
                if u[0] == user_in and u[1] == pass_in:
                    berhasil = True
                    akun = u
            if berhasil == False:
                percobaan += 1
                print(f"Login gagal! Sisa percobaan: {3 - percobaan}")

        if berhasil == False:
            print("Terlalu banyak percobaan gagal. Kembali ke menu utama.")
            input("Tekan Enter untuk lanjut...")
        else:
            username = akun[0]
            role = akun[2]

            # MENU SETELAH LOGIN
            while True:
                os.system("cls" if os.name == "nt" else "clear")
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

                # LOGOUT
                if logout:
                    break

                # CREATE
                elif menu == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== TAMBAH RUN ===")
                    pemain = input("Nama pemain: ").strip()
                    if pemain == "":
                        print("Nama pemain tidak boleh kosong!")
                    else:
                        for i in range(len(kategori)):
                            print(f"{i + 1}. {kategori[i]}")
                        k = input("Pilih kategori: ").strip()
                        if k.isdigit() and 1 <= int(k) <= len(kategori):
                            menit = input("Waktu - menit: ").strip()
                            detik = input("Waktu - detik: ").strip()
                            if menit.isdigit() and detik.isdigit() and int(detik) < 60:
                                if int(menit) == 0 and int(detik) == 0:
                                    print("Waktu tidak boleh 00:00!")
                                else:
                                    runs.append([pemain, kategori[int(k) - 1], int(menit), int(detik), username])
                                    print("Run berhasil ditambahkan!")
                            else:
                                print("Menit/detik harus angka, dan detik harus 0-59!")
                        else:
                            print("Kategori tidak valid!")
                    input("Tekan Enter untuk lanjut...")

                # READ (RANKING)
                elif menu == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== RANKING SPEEDRUN ===")
                    for i in range(len(kategori)):
                        print(f"{i + 1}. {kategori[i]}")
                    k = input("Pilih kategori: ").strip()
                    if k.isdigit() and 1 <= int(k) <= len(kategori):
                        nama_kat = kategori[int(k) - 1]
                        tampil = []
                        for r in runs:
                            if r[1] == nama_kat:
                                tampil.append(r)

                        # bubble sort: waktu tercepat paling atas
                        for i in range(len(tampil)):
                            for j in range(len(tampil) - i - 1):
                                waktu_a = tampil[j][2] * 60 + tampil[j][3]
                                waktu_b = tampil[j + 1][2] * 60 + tampil[j + 1][3]
                                if waktu_a > waktu_b:
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
                                r = tampil[i]
                                print(f"{i + 1:<6}{r[0]:<18}{r[2]:02d}:{r[3]:02d}     {r[4]}")
                    else:
                        print("Kategori tidak valid!")
                    input("Tekan Enter untuk lanjut...")

                # UPDATE
                elif menu == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== UBAH RUN ===")
                    bisa = []
                    print(f"{'No':<5}{'Pemain':<18}{'Kategori':<20}{'Waktu':<9}{'Pengirim'}")
                    print("-" * 60)
                    for i in range(len(runs)):
                        if role == "admin" or runs[i][4] == username:
                            bisa.append(i)
                            print(f"{i + 1:<5}{runs[i][0]:<18}{runs[i][1]:<20}{runs[i][2]:02d}:{runs[i][3]:02d}    {runs[i][4]}")

                    if len(bisa) == 0:
                        print("Tidak ada data yang dapat diubah.")
                    else:
                        no = input("Nomor run yang diubah: ").strip()
                        if no.isdigit() and (int(no) - 1) in bisa:
                            idx = int(no) - 1
                            menit_lama = runs[idx][2]
                            detik_lama = runs[idx][3]
                            print("Kosongkan input jika tidak ingin mengubah.")

                            baru = input(f"Pemain [{runs[idx][0]}]: ").strip()
                            if baru != "":
                                runs[idx][0] = baru

                            for i in range(len(kategori)):
                                print(f"{i + 1}. {kategori[i]}")
                            kat_baru = input(f"Kategori [{runs[idx][1]}]: ").strip()
                            if kat_baru != "":
                                if kat_baru.isdigit() and 1 <= int(kat_baru) <= len(kategori):
                                    runs[idx][1] = kategori[int(kat_baru) - 1]
                                else:
                                    print("Kategori tidak valid, tidak diubah.")

                            menit_baru = input(f"Menit [{runs[idx][2]}]: ").strip()
                            if menit_baru != "":
                                if menit_baru.isdigit():
                                    runs[idx][2] = int(menit_baru)
                                else:
                                    print("Menit harus angka, tidak diubah.")

                            detik_baru = input(f"Detik [{runs[idx][3]}]: ").strip()
                            if detik_baru != "":
                                if detik_baru.isdigit() and int(detik_baru) < 60:
                                    runs[idx][3] = int(detik_baru)
                                else:
                                    print("Detik harus angka 0-59, tidak diubah.")

                            if runs[idx][2] == 0 and runs[idx][3] == 0:
                                runs[idx][2] = menit_lama
                                runs[idx][3] = detik_lama
                                print("Waktu tidak boleh 00:00, waktu dikembalikan.")
                            print("Proses update selesai.")
                        else:
                            print("Nomor tidak valid atau bukan milik Anda!")
                    input("Tekan Enter untuk lanjut...")

                # DELETE
                elif menu == "4":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== HAPUS RUN ===")
                    bisa = []
                    print(f"{'No':<5}{'Pemain':<18}{'Kategori':<20}{'Waktu':<9}{'Pengirim'}")
                    print("-" * 60)
                    for i in range(len(runs)):
                        if role == "admin" or runs[i][4] == username:
                            bisa.append(i)
                            print(f"{i + 1:<5}{runs[i][0]:<18}{runs[i][1]:<20}{runs[i][2]:02d}:{runs[i][3]:02d}    {runs[i][4]}")

                    if len(bisa) == 0:
                        print("Tidak ada data yang dapat dihapus.")
                    else:
                        no = input("Nomor run yang dihapus: ").strip()
                        if no.isdigit() and (int(no) - 1) in bisa:
                            idx = int(no) - 1
                            yakin = input(f"Hapus run {runs[idx][0]}? (y/n): ").strip().lower()
                            if yakin == "y":
                                runs.pop(idx)
                                print("Run berhasil dihapus!")
                            else:
                                print("Penghapusan dibatalkan.")
                        else:
                            print("Nomor tidak valid atau bukan milik Anda!")
                    input("Tekan Enter untuk lanjut...")

                # LIHAT USER (ADMIN)
                elif menu == "5" and role == "admin":
                    os.system("cls" if os.name == "nt" else "clear")
                    print("=== DAFTAR USER ===")
                    print(f"{'No':<5}{'Username':<18}{'Role'}")
                    print("-" * 35)
                    for i in range(len(users)):
                        print(f"{i + 1:<5}{users[i][0]:<18}{users[i][2]}")
                    input("Tekan Enter untuk lanjut...")

                else:
                    print("Menu tidak valid!")
                    input("Tekan Enter untuk lanjut...")

    # REGISTER
    elif pilih == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        user_baru = input("Username baru: ").strip()
        pass_baru = input("Password baru: ").strip()

        sudah_ada = False
        for u in users:
            if u[0].lower() == user_baru.lower():
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
            users.append([user_baru, pass_baru, "user"])
            print("Register berhasil! Silakan login.")
        input("Tekan Enter untuk lanjut...")

    # KELUAR
    elif pilih == "3":
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Menu tidak valid!")
        input("Tekan Enter untuk lanjut...")
