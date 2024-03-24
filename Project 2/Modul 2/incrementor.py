def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print(make_incrementor(22)(33))