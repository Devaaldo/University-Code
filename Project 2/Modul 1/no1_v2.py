def luas_lingkaran(r):
    l = 3.14*r*r
    return l

def volume_tabung(l,t):
    v = l*t
    return v

def main():
    r = int(input("Masukkan jari-jari alas tabung : " ))
    t = int(input("Masukkan tinggi tabung : "))
    v = volume_tabung(luas_lingkaran(r),t)
    print("volume tabung adalah {}".format(v))

if __name__ == '__main__':
    main()



