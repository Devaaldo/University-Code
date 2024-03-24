pastel_pertama = ["merah", "kuning", "hijau", "biru"]
pastel_kedua = ["kuning", "coklat", "ungu"]

pastel_kedua += ["merah"]
pastel_pertama += ["jingga"]

warna_berbeda = set(pastel_pertama) - set(pastel_kedua)

print("Warna yang berbeda adalah : {}".format(warna_berbeda))

# warna_sama = set(pastel_pertama) & set(pastel_kedua)




# print("Warna yang sama adalah : {}".format(warna_sama))

# print(pastel_pertama)
# print(pastel_kedua)
