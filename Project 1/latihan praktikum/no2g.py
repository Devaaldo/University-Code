hari_pertama_membeli = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua_membeli = {"garam", "gula", "coklat", "kecap"}

barang_tidak_kedua = hari_pertama_membeli.symmetric_difference(hari_kedua_membeli)

print("Barang yang tidak sama pada pembelian hari pertama dan pembelian hari kedua : ", barang_tidak_kedua)
