#Buat array numpy 1 dimensi dengan nilai secara urut dari 0 (nol) sampai dengan 20, 
#kemudian tampilkan nilai mulai dari index ke 3 sampai ke 15 dengan step kelipatan 3

import numpy as np

x = np.arange(20)
result = x[3:15:3]
print(result)