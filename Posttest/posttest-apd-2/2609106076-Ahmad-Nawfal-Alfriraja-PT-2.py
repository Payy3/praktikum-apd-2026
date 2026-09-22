komponen_1 = 120000 
komponen_2 = 135000 
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000
nota_fisik = 15000

komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]
total_bayar = (komponen[0] + komponen[1] + komponen[2] + komponen[3] + komponen[4] + komponen[5]) + nota_fisik
rata_rata = total_bayar / len(komponen)
nim = 76
boolean = nim != rata_rata
gbp = total_bayar/23.788
komponen_1_sampai_4 = komponen[-6:-2]

print("komponen 1:", komponen_1)
print("komponen 2:", komponen_2)
print("komponen 3:", komponen_3)    
print("komponen 4:", komponen_4)
print("komponen 5:", komponen_5)
print("komponen 6:", komponen_6)
print("Nota fisik:", nota_fisik)
print("Komponen:", komponen)
print("Total bayar:", total_bayar)
print("Rata-rata:", rata_rata)
print("NIM:", nim)
print("Boolean (nim != rata_rata):", boolean)
print("Total dalam GBP:", gbp)
print("Slice komponen_1 s/d komponen_4:", komponen_1_sampai_4)