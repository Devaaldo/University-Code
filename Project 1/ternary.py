# x=3
# print("Bilangan Ganjil" if((x%2)==1) else "Bilangan Genap")

#tuple
# x=3
# print(("Bilangan genap", "Bilangan ganjil")[((x%2)==1)])

#dictionary
# x=3
# print({True:"Bilangan ganjil", False:"Bilangan genap"}[((x%2)==1)])

#lambda function
x=3
print((lambda:"Bilangan genap",lambda:"Bilangan ganjil")[(x%2)==1]())