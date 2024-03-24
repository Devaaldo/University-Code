import numpy as np
# x = np.random.random((2,3)) #dua dimensi

# x = np.random.random((2,3,3)) #menciptakan array dengan panjang z =2, x=3, y=3
#tiga dimensi

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
result = x[1:7:2]
print(result)