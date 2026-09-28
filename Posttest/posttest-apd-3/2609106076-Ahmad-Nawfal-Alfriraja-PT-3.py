# Program Top Up Game
print("Selamat datang di top up game termurah di Samarinda!")
nama = input("Masukkan nama Anda: ")
password = int(input("Masukkan password Anda : "))

if nama == "Nawal" and password == 76:
    print("Login berhasil!")
    id = int(input("Masukkan ID Anda : "))
    print("ID Anda valid!")

    nama_game = input("Mau top up game apa? (Genshin Impact / Minecraft / Mobile Legends) : ")
    kategori_topup = input("Mau top up kategori apa? (Kecil / Menengah / Besar) : ")
    if kategori_topup == "Kecil":
        harga_topup = 15000
    elif kategori_topup == "Menengah":
        harga_topup = 50000
    elif kategori_topup == "Besar":
        harga_topup = 150000

    metode_pembayaran = input("Mau bayar pakai apa? (Pulsa / E-Wallet) : ")
    biaya_admin = 2500 if metode_pembayaran == "Pulsa" else 500
    total_pembayaran = harga_topup + biaya_admin

    print("----- STRUK PEMBELIAN -----")
    print(f"ID               : {id}")
    print(f"Nama             : {nama}")
    print(f"Game             : {nama_game}")
    print(f"Kategori         : {kategori_topup}")
    print(f"Metode Pembayaran: {metode_pembayaran}")
    print(f"Total Pembayaran : Rp.{total_pembayaran}")
    print("-----------------------------")
    print("Terima kasih telah top up bersama kami!")
else:
    print("Login gagal! nama atau password kamu salah.")