hari_pertama_membeli = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua_membeli = {"garam", "gula", "coklat", "kecap"}

barang2 = hari_kedua_membeli.difference(hari_pertama_membeli)

print("Barang yang dibeli di hari kedua saja:", barang2)
