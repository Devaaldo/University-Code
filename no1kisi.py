import numpy as np

x = np.random.random(((3,3,2)))
result = x[0,1,0]
result2 = x[1,1,1]
result3 = x[0,2,1]
print(result)
print(result2)
print(result3)