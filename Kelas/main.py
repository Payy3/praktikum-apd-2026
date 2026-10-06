# =====================================================
#  PROGRAM ATM UNMULS
# =====================================================

# ----- Data Login (untuk pemeriksaan) -----
USERNAME = "Nawal"
PIN      = "076"

# ----- Saldo Awal -----
saldo = 2000000

# ----- Pengaturan Tampilan -----
LEBAR = 46
GARIS_TEBAL = "=" * LEBAR
GARIS_TIPIS = "-" * LEBAR

# =====================================================
#  TAMPILAN PEMBUKA
# =====================================================
print("\n" + GARIS_TEBAL)
print("ATM UNMULS".center(LEBAR))
print("Cepat  |  Aman  |  Terpercaya".center(LEBAR))
print(GARIS_TEBAL)

# =====================================================
#  1. SISTEM LOGIN
# =====================================================
login_berhasil = False

for percobaan in range(3):
    print(f"\n[ LOGIN - Percobaan {percobaan + 1} dari 3 ]")
    print(GARIS_TIPIS)
    input_username = input("  Username : ")
    input_pin      = input("  PIN      : ")
    print(GARIS_TIPIS)

    if input_username == USERNAME and input_pin == PIN:
        print("Login Berhasil!".center(LEBAR))
        print(f"Selamat datang, {input_username}".center(LEBAR))
        print(GARIS_TEBAL)
        login_berhasil = True
        break
    elif percobaan < 2:
        print(f"Login Gagal! Sisa percobaan: {2 - percobaan}".center(LEBAR))
    else:
        print("Login Gagal! Sisa percobaan: 0".center(LEBAR))
        print("Akun Anda Terblokir!".center(LEBAR))
        print(GARIS_TEBAL)

# =====================================================
#  2. MENU UTAMA
# =====================================================
if login_berhasil:
    while True:
        print("\n+" + "-" * (LEBAR - 2) + "+")
        print("|" + "MENU UTAMA ATM".center(LEBAR - 2) + "|")
        print("+" + "-" * (LEBAR - 2) + "+")
        print("|" + "  [1]  Cek Saldo".ljust(LEBAR - 2) + "|")
        print("|" + "  [2]  Tarik Tunai".ljust(LEBAR - 2) + "|")
        print("|" + "  [3]  Setor Tunai".ljust(LEBAR - 2) + "|")
        print("|" + "  [4]  Keluar".ljust(LEBAR - 2) + "|")
        print("+" + "-" * (LEBAR - 2) + "+")

        pilihan = input("  Pilih menu (1-4) : ")
        print()

        # ---------- [1] CEK SALDO ----------
        if pilihan == "1":
            print("[ CEK SALDO ]".center(LEBAR))
            print(GARIS_TIPIS)
            print(f"  Saldo Anda saat ini : Rp {saldo:,}".replace(",", "."))
            print(GARIS_TIPIS)

        # ---------- [2] TARIK TUNAI ----------
        elif pilihan == "2":
            print("[ TARIK TUNAI ]".center(LEBAR))
            print(GARIS_TIPIS)
            nominal = int(input("  Nominal penarikan : Rp "))
            print(GARIS_TIPIS)
            if nominal <= 0:
                print("Nominal tidak valid!".center(LEBAR))
            elif nominal > saldo:
                print("Saldo tidak mencukupi!".center(LEBAR))
            else:
                saldo -= nominal
                print("Transaksi Berhasil!".center(LEBAR))
                print(f"  Uang ditarik : Rp {nominal:,}".replace(",", "."))
                print(f"  Sisa saldo   : Rp {saldo:,}".replace(",", "."))
            print(GARIS_TIPIS)

        # ---------- [3] SETOR TUNAI ----------
        elif pilihan == "3":
            print("[ SETOR TUNAI ]".center(LEBAR))
            print(GARIS_TIPIS)
            nominal = int(input("  Nominal setoran : Rp "))
            print(GARIS_TIPIS)
            if nominal <= 0:
                print("Nominal tidak valid!".center(LEBAR))
            else:
                saldo += nominal
                print("Setoran Berhasil!".center(LEBAR))
                print(f"  Uang disetor : Rp {nominal:,}".replace(",", "."))
                print(f"  Total saldo  : Rp {saldo:,}".replace(",", "."))
            print(GARIS_TIPIS)

        # ---------- [4] KELUAR ----------
        elif pilihan == "4":
            print(GARIS_TEBAL)
            print("Terima kasih telah menggunakan".center(LEBAR))
            print("ATM UNMULS".center(LEBAR))
            print("Sampai jumpa kembali!".center(LEBAR))
            print(GARIS_TEBAL)
            break

        # ---------- PILIHAN TIDAK VALID ----------
        else:
            print(GARIS_TIPIS)
            print("Pilihan menu tidak valid!".center(LEBAR))
            print("Masukkan angka 1 sampai 4.".center(LEBAR))
            print(GARIS_TIPIS)