"""
Дан список A размера N. Вывести вначале его элементы с четными номерами (в
порядке возрастания номеров), а затем — элементы с нечетными номерами (также в
порядке возрастания номеров): A2, A4, А6, . . ., A1, A3, A5, ... . Условный оператор не
использовать.
"""
while True:
    try:
        A = int(input('Введите число >>> '))
        list = []
        for i in range(1, A + 1):
            list.append(i)

        print("Четные числа: ", list[1::2])
        print("Нечетные числа: ", list[::2])
        break

    except ValueError:
        print("Вы ввели не число")