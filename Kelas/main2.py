total_pembelian = float(input("Masukkan total pembelian (Rp): "))

if total_pembelian > 200000:
	diskon = 0.30
elif total_pembelian > 100000:
	diskon = 0.10
else:
	diskon = 0

jumlah_diskon = total_pembelian * diskon
total_bayar = total_pembelian - jumlah_diskon

print(f"Diskon: {diskon * 100:}%")
print(f"Jumlah diskon: Rp{jumlah_diskon:}")
print(f"Total yang harus dibayar: Rp{total_bayar:}")


