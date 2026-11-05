import os
from colorama import Fore, Style, init

init(autoreset=True)


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def ke_detik(menit, detik):
    return menit * 60 + detik


def format_waktu(menit, detik):
    return f"{menit:02d}:{detik:02d}"


def judul(teks):
    garis = "=" * 45
    print(Fore.CYAN + Style.BRIGHT + garis)
    print(Fore.CYAN + Style.BRIGHT + teks.center(45))
    print(Fore.CYAN + Style.BRIGHT + garis)


def sukses(teks):
    print(Fore.GREEN + teks)


def galat(teks):
    print(Fore.RED + teks)


def peringatan(teks):
    print(Fore.YELLOW + teks)


def tunggu():
    input("Tekan Enter untuk lanjut...")
