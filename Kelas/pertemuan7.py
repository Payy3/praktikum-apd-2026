
def tampilkan_menu():
    print("========= MENU =========")
    print("[1] Lihat Data Buku")
    print("[2] Tambahkan Data Buku")
    print("[3] Edit Data Buku")
    print("[4] Hapus Data Buku")
    print("[5] Keluar")
    menu = input("PILIH MENU > ")


    if menu == "1":
        lihat_buku()
    elif menu == "2":
        tambah_buku()
    elif menu =="3":
        edit_buku()
    elif menu =="4":
        hapus_buku()
    elif menu == "5":
        exit()
    else:
        print("Pilihan tidak valid!")