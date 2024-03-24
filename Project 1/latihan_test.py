n = int(input("Berapa jumlah angka dalam deret?"))
min = (int(input("Berapa angka terkecil?")))
max = (int(input("Berapa angka terbesar?")))
divisible = int(input("Berapa angka yang ingin kamu bagi?"))

import random
deret = []
for i in range(0,n):
    deret.append(random.randint(min,max))

result = list(filter(lambda x: (x % divisible == 0), deret))

print(f"Didalam deret {deret} angka yang dapat dibagi dengan {divisible} adalah {result}")