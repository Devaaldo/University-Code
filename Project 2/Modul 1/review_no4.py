def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

def penambahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def stop():
    print("Terima kasih telah menggunakan program ini")
    exit()

if __name__ == '__main__':

    while True:
        print("Pilih operasi yang ingin dilakukan:")
        print("1. Perkalian")
        print("2. Pembagian")
        print("3. Penambahan")
        print("4. Pengurangan")
        print("5. Keluar")

        operasi = int(input("Masukkan operasi yang diminta "))

        if operasi not in range(1, 6):
            print("Pilihan tidak valid!")
            continue
        elif operasi==5:
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            angka1 = float(input("Masukkan angka satu: "))
            angka2 = float(input("Masukkan angka dua: "))

        if operasi == 1:
            hasil = perkalian(angka1, angka2)
            print(f"Hasilnya adalah {hasil}")
        elif operasi == 2:
            hasil = pembagian(angka1, angka2)
            print(f"Hasilnya adalah {hasil}")
        elif operasi == 3:
            hasil = penambahan(angka1, angka2)
            print(f"Hasilnya adalah {hasil}")
        elif operasi == 4:
            hasil = pengurangan(angka1, angka2)
            print(f"Hasilnya adalah {hasil}")
        else:
            stop()