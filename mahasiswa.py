def tampilkan_profil_mahasiswa(**kwargs):
    print("Profile Mahasiswa UNJANI Yogyakarta")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    print(f"Mahasiswa Prodi {kwargs['Prodi']} UNJANI Yogyakarta")
    print(f"Dengan nama {kwargs['Nama']}")
    print(f"Mempunyai NIM {kwargs['NIM']}")
    print(f"Memiliki Hobi {kwargs['Hobi']}")

def main():
    nama = input("Nama : ")
    nim = input("NIM : ")
    prodi = input("Prodi : ")
    hobi = input("Hobi : ")

    tampilkan_profil_mahasiswa(Nama=nama, NIM=nim, Prodi=prodi, Hobi=hobi)

if __name__ == "__main__":
    main()
