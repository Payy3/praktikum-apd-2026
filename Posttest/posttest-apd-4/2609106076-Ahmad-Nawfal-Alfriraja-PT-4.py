# Program ATM
username = "Nawal"
pin = "076"
saldo = 2000000

print("=" * 40)
print("      SELAMAT DATANG DI ATM UNMULS")
print("=" * 40)

login_berhasil = False
for percobaan in range(3):
    input_username = input("Username : ")
    input_pin = input("PIN      : ")
    print("=" * 40)
    if input_username == username and input_pin == pin:
        print("    Login Berhasil!")
        login_berhasil = True
        break
    elif percobaan < 2:
        print(f"    Login Gagal! Sisa percobaan: {2 - percobaan}")
        print("=" * 40)
    else:
        print("    Login Gagal! Sisa percobaan: 0")
        print("    Akun Anda Terblokir!")
        print("=" * 40)

if login_berhasil:
    while True:
        print("=" * 30)
        print("            MENU ATM")
        print("        [1] Cek Saldo")
        print("        [2] Tarik Tunai")
        print("        [3] Setor Tunai")
        print("        [4] Keluar")
        print("=" * 30)

        pilihan = input("Pilihan Menu 1-4 : ")

        if pilihan == "1":
            print("-" * 40)
            print(f"    Saldo Anda saat ini: Rp.{saldo:,}".replace(",", "."))
            print("-" * 40)

        elif pilihan == "2":
            while True:
                nominal = input("Masukan Nominal penarikan :Rp. ")
                if not nominal.isdigit():
                    print("    Input tidak valid!")
                    continue
                elif nominal != "0" and nominal[0] == "0":
                    print("    Masukkan angka tanpa awalan 0!")
                    continue

                nominal = int(nominal)

                if nominal <= 0:
                    print("    Nominal tidak valid!")
                elif nominal > saldo:
                    print("    Saldo tidak mencukupi!")
                else:
                    saldo -= nominal
                    print("-" * 40)
                    print("    Transaksi berhasil!")
                    print(f"    Uang ditarik: Rp.{nominal:,}".replace(",", "."))
                    print(f"    Sisa saldo  : Rp.{saldo:,}".replace(",", "."))
                    print("-" * 40)
                    break

        elif pilihan == "3":
            while True:
                nominal = input("Masukan Nominal setoran :Rp. ")
                if not nominal.isdigit():
                    print("    Input tidak valid!")
                    continue
                elif nominal != "0" and nominal[0] == "0":
                    print("    Masukkan angka tanpa awalan 0!")
                    continue

                nominal = int(nominal)

                if nominal <= 0:
                    print("    Nominal tidak valid!")
                else:
                    saldo += nominal
                    print("-" * 40)
                    print("    Setoran berhasil!")
                    print(f"    Uang disetor: Rp.{nominal:,}".replace(",", "."))
                    print(f"    Total saldo : Rp.{saldo:,}".replace(",", "."))
                    print("-" * 40)
                    break

        elif pilihan == "4":
            print("=" * 40)
            print("    Terima kasih telah menggunakan ATM UNMULS!")
            print("=" * 40)
            break

        else:
            print("=" * 40)
            print("    Pilihan menu tidak valid!")
            print("=" * 40)