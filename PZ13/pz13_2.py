# В матрице найти максимальный положительный элемент, кратный 4.
import numpy as np

matrix = [[1, 2, 8],
          [-4, 5, 6],
          [7, -8, 12]]

def max_poz(matrix):
    filtered_matrix = list(filter(lambda x: x > 0 and x % 4 == 0, np.array(matrix).ravel()))
    max_value = max(filtered_matrix, key=abs, default=None)
    return max_value

print(max_poz(matrix))