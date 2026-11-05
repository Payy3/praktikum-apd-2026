"""Semua output tabel menggunakan library prettytable."""

from prettytable import PrettyTable

import data
from utils import format_waktu


def tampilkan_menu_awal():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    tabel.add_row(["1", "Login"])
    tabel.add_row(["2", "Register"])
    tabel.add_row(["3", "Keluar"])
    tabel.align["Menu"] = "l"
    print(tabel)


def tampilkan_menu_pengguna(role):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    tabel.add_row(["1", "Tambah Run"])
    tabel.add_row(["2", "Lihat Ranking"])
    tabel.add_row(["3", "Ubah Run"])
    tabel.add_row(["4", "Hapus Run"])
    if role == "admin":
        tabel.add_row(["5", "Lihat Daftar User"])
        tabel.add_row(["6", "Logout"])
    else:
        tabel.add_row(["5", "Logout"])
    tabel.align["Menu"] = "l"
    print(tabel)


def tampilkan_kategori():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Kategori"]
    for i, nama in enumerate(data.kategori, start=1):
        tabel.add_row([i, nama])
    tabel.align["Kategori"] = "l"
    print(tabel)


def tampilkan_tabel_run(daftar_id):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Pemain", "Kategori", "Waktu", "Pengirim"]
    for id_run in daftar_id:
        r = data.runs[id_run]
        tabel.add_row([id_run, r["pemain"], r["kategori"],
                       format_waktu(r["menit"], r["detik"]), r["pengirim"]])
    tabel.align["Pemain"] = "l"
    tabel.align["Kategori"] = "l"
    tabel.align["Pengirim"] = "l"
    print(tabel)


def tampilkan_ranking(daftar_id):
    tabel = PrettyTable()
    tabel.field_names = ["Rank", "Pemain", "Waktu", "Pengirim"]
    for urutan, id_run in enumerate(daftar_id, start=1):
        r = data.runs[id_run]
        tabel.add_row([urutan, r["pemain"],
                       format_waktu(r["menit"], r["detik"]), r["pengirim"]])
    tabel.align["Pemain"] = "l"
    tabel.align["Pengirim"] = "l"
    print(tabel)


def tampilkan_daftar_user():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Username", "Role"]
    for nomor, nama in enumerate(data.users, start=1):
        tabel.add_row([nomor, nama, data.users[nama]["role"]])
    tabel.align["Username"] = "l"
    tabel.align["Role"] = "l"
    print(tabel)
