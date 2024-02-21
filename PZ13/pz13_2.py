# В матрице найти максимальный положительный элемент, кратный 4.
matrix = [
    [1, 2, 8],
    [-4, 5, 6],
    [7, -8, 12]
]

def is_positive(num):
    return num > 0 and num % 4 == 0

def get_max_positive(matrix):
    max_value = None
    for row in matrix:
        for element in row:
            if is_positive(element):
                if max_value is None or element > max_value:
                    max_value = element
    return max_value

result = get_max_positive(matrix)
print("Максимальный положительный элемент, кратный 4:", result)