import auth
import run_service
import tampilan
import utils


def menu_pengguna(username, role):
    while True:
        utils.bersihkan_layar()
        utils.judul(f"MENU {role.upper()} - {username}")
        tampilan.tampilkan_menu_pengguna(role)
        menu = input("Pilih menu: ").strip()

        if (menu == "6" and role == "admin") or (menu == "5" and role == "user"):
            break
        elif menu == "1":
            run_service.tambah_run(username)
        elif menu == "2":
            run_service.lihat_ranking()
        elif menu == "3":
            run_service.ubah_run(role, username)
        elif menu == "4":
            run_service.hapus_run(role, username)
        elif menu == "5" and role == "admin":
            auth.lihat_daftar_user()
        else:
            utils.galat("Menu tidak valid!")
            utils.tunggu()


def main():
    import data

    while True:
        utils.bersihkan_layar()
        utils.judul("PEMERINGKATAN SPEEDRUN MINECRAFT")
        tampilan.tampilkan_menu_awal()
        pilih = input("Pilih menu [1-3]: ").strip()

        if pilih == "1":
            username = auth.proses_login()
            if username is not None:
                menu_pengguna(username, data.users[username]["role"])
        elif pilih == "2":
            auth.proses_register()
        elif pilih == "3":
            utils.sukses("Terima kasih, sampai jumpa!")
            break
        else:
            utils.galat("Menu tidak valid!")
            utils.tunggu()


if __name__ == "__main__":
    main()
