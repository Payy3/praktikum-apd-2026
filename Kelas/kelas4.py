"""Program ATM sederhana dengan login dan validasi transaksi."""

# Kredensial contoh untuk pemeriksaan program.
USERNAME_BENAR = "maha"
PIN_BENAR = "1"  # Ganti dengan 3 digit terakhir NIM bila diperlukan.
saldo = 1_000_000

print("=" * 38)
print("       SELAMAT DATANG DI ATM")
print("=" * 38)

login_berhasil = False
for percobaan in range(1, 4):
	username = input("Username: ").strip()
	pin = input("PIN / Password (3 digit): ").strip()

	if username == USERNAME_BENAR and pin == PIN_BENAR:
		print("Login Berhasil!")
		login_berhasil = True
		break

	print(f"Login Gagal! Sisa percobaan: {3 - percobaan}")

if not login_berhasil:
	print("Akun Anda Terblokir!")
else:
	while True:
		print("\n" + "=" * 38)
		print("             MENU UTAMA")
		print("=" * 38)
		print("[1] Cek Saldo")
		print("[2] Tarik Tunai")
		print("[3] Setor Tunai")
		print("[4] Keluar")
		pilihan = input("Pilih menu (1-4): ").strip()

		if pilihan == "1":
			print(f"Saldo Anda: Rp{saldo:,}".replace(",", "."))
		elif pilihan in ("2", "3"):
			aksi = "ditarik" if pilihan == "2" else "disetor"
			try:
				nominal = int(input(f"Masukkan nominal yang ingin {aksi}: Rp"))
			except ValueError:
				print("Input tidak valid. Masukkan nominal berupa angka.")
				continue

			if nominal <= 0:
				print("Nominal harus lebih dari 0.")
			elif nominal % 50_000 != 0:
				print("Nominal harus kelipatan Rp 50.000")
			elif pilihan == "2":
				if nominal > saldo:
					print("Saldo tidak mencukupi!")
				else:
					saldo -= nominal
					print(f"Transaksi berhasil. Nominal ditarik: Rp{nominal:,}".replace(",", "."))
					print(f"Sisa saldo: Rp{saldo:,}".replace(",", "."))
			else:
				saldo += nominal
				print(f"Setor tunai berhasil. Nominal disetor: Rp{nominal:,}".replace(",", "."))
				print(f"Total saldo: Rp{saldo:,}".replace(",", "."))
		elif pilihan == "4":
			print("Terima kasih telah menggunakan layanan ATM.")
			break
		else:
			print("Pilihan tidak valid. Silakan pilih menu 1-4.")
