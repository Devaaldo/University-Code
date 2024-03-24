nama = ""
while nama!="python":
	nama = str(input("Masukan nama : "))
	print("Nama saya {}".format(nama))
	if nama.lower() =="python":
		print("Goodbye {}".format(nama))