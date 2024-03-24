def pempek(*args):
    buah = int(input("Masukkan buah yang dibeli : "))

    for i in range(buah):
        buah = input(f"Buah {i+1}: ")
        args += (buah,)
        
    print("Buah yang anda beli adalah  ")
    for i, buah in enumerate (args):
        print(f"{i+1}. {buah}")
        
    print("Terima Kasih")
pempek()