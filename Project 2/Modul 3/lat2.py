def tampilkan_profil_mahasiswa(**kwargs):
    nama = kwargs.get("nama")
    nim = kwargs.get("nim")
    jurusan = kwargs.get("jurusan")
    ipk = kwargs.get("ipk")


    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Jurusan: {jurusan}")
    print(f"IPK: {ipk}")



nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
jurusan = input("Masukkan jurusan: ")
ipk = float(input("Masukkan IPK: "))

tampilkan_profil_mahasiswa(nama=nama, nim=nim, jurusan=jurusan, ipk=ipk)
