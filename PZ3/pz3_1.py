# Данны три целых числа A, B, C.
# Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное"
while True:  # Обработка исключений
    try:
        a = float(input("Введите первое число >> "))
        b = float(input("Введите второе число >> "))
        c = float(input("Введите третье число >> "))

        if (a > 0) or (b > 0) or (c > 0):
            print(True)
        else:
            print(False)
        break

    except ValueError:
        print("Error!!! Введите число")
