"""
Дано число R и список размера N. Найти два соседних элемента списка, сумма
которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
которого величина |AK - R| является минимальной).
"""
import random


def find_closest_elements(R, arr):
    min_diff = float('inf')
    res = None
    for i in range(len(arr) - 1):
        diff = abs(arr[i] + arr[i+1] - R)
        if diff < min_diff:
            min_diff = diff
            res = (i, i+1)
    return res


R = int(input('Введите число >>> '))
arr = [random.randint(-10, 50) for _ in range(int(input('Введите количество элементов списка >>> ')))]
print(arr)
result = find_closest_elements(R, arr)
if result:
    print("Ближайшие соседние элементы списка >>> ", arr[result[0]], arr[result[1]])