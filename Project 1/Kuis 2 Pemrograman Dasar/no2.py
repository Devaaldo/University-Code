def luas_alas_segiempat(panjang, lebar):
  luas = panjang * lebar
  return luas

def volume_prisma_segiempat(panjang, lebar, tinggi):
  volume = luas_alas_segiempat(panjang, lebar) * tinggi
  return volume

panjang = int(input("Masukkan panjang : "))
lebar = int(input("Masukkan lebar : "))
tinggi = int(input("Masukkan tinggi : "))

luas_alas = luas_alas_segiempat(panjang, lebar)
volume = volume_prisma_segiempat(panjang, lebar, tinggi)

print(f"Volume prisma segi empat adalah : {volume}")

# Buatlah program dengan fungsi untuk menghitung volume prisma segi empat. dengan tahapan ada 2 fungsi. fungsi luas alas dan fungsi hitung volume