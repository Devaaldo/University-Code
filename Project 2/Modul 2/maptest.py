def pangkat(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(pangkat, numbers)
print(result)

print(list(result))