#  Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

average = lambda row: sum(row) / len(row)

result = list(map(average, filter(lambda x: matrix.index(x) % 2 - 1 != 0, matrix)))

print("Средние значения для строк с нечетным номером:")
for index, value in enumerate(result, start=1):
    print(f"Строка {index * 2 - 1 }: {value}")
