import numpy as np

# Array 2D dengan nilai yang diberikan
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
])

print(array)
# Mengambil elemen array di baris 4 dan kolom 1 dan 2
block_array = array[4, 1:3]

print(block_array)
