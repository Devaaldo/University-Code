def perkalian(x, y):
    return x*y

def pembagian(x,y):
    return x/y

def penambahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def stop ():
    print("Terimakasih telah menggunakan program ini")

if __name__ == '__main__':
    while True :
        print("1. Operasi yang diminta")
        print("2. Perkalian")
        print("3. Pembagian")
        print("4. Penambahan")
        print("5. Pengurangan")
        print("6. Stop")

    operasi = int(input("Masukkan pilihan"))

    angka1 = float(input("Masukkan angka1 = "))
    angka2 = float(input("Masukkan angka2 = "))

    if operasi == 1:
        hasil = perkalian(bilangan1, bilangan2)
        print(f"Hasilnya adalah {hasil}")
    
    if operasi == 2:
        hasil = pembagian(bilangan1, bilangan2)
        print(f"Hasilnya adalah {hasil}")
    
    if operasi == 3:
        hasil = penambahan(bilangan1, bilangan2)
    
    if operasi == 4:
        hasil = pengurangan(bilangan1, bilangan2)
    else:
        stop()

