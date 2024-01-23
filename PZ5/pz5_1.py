# Найти сумму чисел ряда 1, 2, 3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные
def sum_of_series():
    total_sum = 0
    for i in range(1, 6):
        total_sum += i
    return total_sum


result = sum_of_series()
print("Сумма чисел от 1 до 60: ", result)
