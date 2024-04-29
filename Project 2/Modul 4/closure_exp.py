def penjelasan(pesan):
    def isi_pesan():
        print(pesan)
    return isi_pesan

hasil_pesan = penjelasan("Saya orang Palembang")
hasil_pesan()