from functools import reduce

numbers = list(range(5,21))
mapping = map(lambda x:x*2, numbers)
filterring = filter(lambda x:x % 4 == 0, mapping)
product = reduce((lambda x,y : x + y), filterring)

# print(list(mapping))
# print(list(filterring))
print(product)

