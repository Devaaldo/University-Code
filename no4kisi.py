from functools import reduce

numbers = list(range(1,11))
mapping = map(lambda x:x+3, numbers)
filterring = filter(lambda x:x % 2 == 0, mapping)
product = reduce((lambda x,y : x + y), filterring)

# print(list(mapping))
# print(list(filterring))
print(product)

