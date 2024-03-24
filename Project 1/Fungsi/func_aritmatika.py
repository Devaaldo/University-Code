def luas_persegi_penjang(panjang,lebar):
	#Fungsi rumus hitung luas persegi panjang
	luas = panjang*lebar
	return luas

def volume_balok(panjang,lebar,tinggi):
	#Fungsi rumus hitung volume balok
	volume = luas_persegi_penjang(panjang,lebar)*tinggi
	return volume


if __name__ == "__main__":
	#program utama
	panjang = int(input("Masukkan panjang balok : "))
	lebar = int(input("Masukkan tinggi balok : "))
	tinggi = int(input("Masukkan tinggi balok : "))
	print("Volume balok adalah {}".format(volume_balok(panjang,lebar,tinggi)))