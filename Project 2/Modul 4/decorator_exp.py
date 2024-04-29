def makanan(func):
    def nama_makanan():
        print("Nama makanan ini adalah pempek")
        func()
    return nama_makanan

def bumbu():
    print("Makan pempek harus diiringi dengan cuko")

kegiatan = makanan(bumbu)
kegiatan()