def luas_lingkaran(r):
    luas = 3.14*r*r
    return luas


def volume_tabung(r,t):
    volume = luas_lingkaran(r)*t
    return volume

if __name__== '__main__':
    r = int(input("Masukkan jari jari : "))
    t = int(input("Masukkan tinggi : "))
    
    volume = volume_tabung(r,t)
    print("Hasil dari penjumlahannya adalah {} ".format(volume))