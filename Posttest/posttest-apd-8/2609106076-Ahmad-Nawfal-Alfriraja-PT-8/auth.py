"""Autentikasi: login (rekursif), register, dan daftar user."""

import getpass

import data
import tampilan
import utils


def login_rekursif(sisa):
    if sisa == 0:
        return None
    user_in = input("Username: ").strip()
    pass_in = getpass.getpass("Password: ").strip()
    if user_in in data.users and data.users[user_in]["password"] == pass_in:
        return user_in
    utils.galat(f"Login gagal! Sisa percobaan: {sisa - 1}")
    return login_rekursif(sisa - 1)


def proses_login():
    """Mengembalikan username jika berhasil, None jika gagal."""
    utils.bersihkan_layar()
    utils.judul("LOGIN")
    username = login_rekursif(3)
    if username is None:
        utils.galat("Terlalu banyak percobaan gagal. Kembali ke menu utama.")
        utils.tunggu()
    return username


def proses_register():
    utils.bersihkan_layar()
    utils.judul("REGISTER")
    user_baru = input("Username baru: ").strip()
    pass_baru = getpass.getpass("Password baru: ").strip()

    sudah_ada = False
    for nama in data.users:
        if nama.lower() == user_baru.lower():
            sudah_ada = True

    if user_baru == "" or pass_baru == "":
        utils.galat("Username dan password tidak boleh kosong!")
    elif len(user_baru) < 3:
        utils.galat("Username minimal 3 karakter!")
    elif len(pass_baru) < 4:
        utils.galat("Password minimal 4 karakter!")
    elif sudah_ada:
        utils.galat("Username sudah dipakai!")
    else:
        data.users[user_baru] = {"password": pass_baru, "role": "user"}
        utils.sukses("Register berhasil! Silakan login.")
    utils.tunggu()


def lihat_daftar_user():
    utils.bersihkan_layar()
    utils.judul("DAFTAR USER")
    tampilan.tampilkan_daftar_user()
    utils.tunggu()
