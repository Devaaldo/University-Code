def test_arguments(tahun, versi, rakitan):
    print("Tahun : {}".format(tahun))
    print("Versi : {}".format(versi))
    print("Rakitan : {}".format(rakitan))

corolla = {'tahun':"1999",'versi':"Cross",'rakitan':"Thailand"}
test_arguments(**corolla)