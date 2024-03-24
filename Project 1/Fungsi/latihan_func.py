def luas_alas(sisi):
    luas = sisi*sisi
    return luas

def volume_limas(sisi,tinggi):
    volume = luas_alas(sisi)*1/3*tinggi
    return volume

sisi = int(input("Masukkan sisi limas :  "))
tinggi = int(input("Masukkan tinggi limas : "))
print("volume limas segi empat adalah : {}".format(volume_limas(sisi,tinggi)))
