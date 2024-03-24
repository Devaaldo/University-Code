def input_nama(pilihan):
    list_nama = []
    while pilihan=="ya":
        pilihan = str(input("Masukkan Nama ? \n ya/tidak :"))
        if pilihan == "ya" :
            nama = (str(input("Nama : ")))
            list_nama.append(nama)
    return list_nama

def print_nama(list_nama):
    print("Beberapa nama yang telah dimasukkan")
    for index, nama in enumerate(list_nama):
        print("Nama {} adalah {}".format(index+1, nama))


if __name__ == '__main__':
    pilihan = "ya"
    list_nama = input_nama(pilihan)
    print_nama(list_nama)    


