def option():
	print("Pilih salah satu dari tiga fungsionalitas berikut :")
	print("1. Mencari Luas Persegi Panjang")
	print("2. Mencari Keliling Persegi Panjang")
	print("3. Keluar dari Program")
	pilihan = int(input("Masukkan pilihan anda : "))
	return pilihan

def luas_persegi_panjang(panjang,lebar):
	luas = panjang*lebar
	return luas

def keliling_persegi_panjang(panjang,lebar):
	keliling = 2*(panjang+lebar)
	return keliling

pilihan = 0

while pilihan < 3:
	pilihan = option()
	if pilihan == 3 or pilihan == 0 :
		break
	else:
		panjang = int(input("Masukkan Panjang : "))
		lebar = int(input("Masukkan Lebar : "))
		if pilihan == 1:
			luas = luas_persegi_panjang(panjang,lebar)
			print("Luas Persegi Panjang adalah : {}".format(luas_persegi_panjang(panjang,lebar)))
		else:
			keliling = keliling_persegi_panjang(panjang,lebar)
			print("Keliling Persegi Panjang adalah : {}".format(keliling_persegi_panjang(panjang,lebar)))
