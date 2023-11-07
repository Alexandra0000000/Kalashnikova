# Дано целое число N(>1). Вывести наименьшее из целых чисел K, для которых сумма 1+2+...+K будет больше или равна N
# вывести саму эту сумму
while True: # Обработка исключений
    try:
        N = int(input("Введите целое число N(>1): "))
        if N > 1:
            K = 1
            total_sum = 0

            while total_sum < N:
                total_sum += K
                K += 1

            print("Наименьшее число K:", K)
            print("Сумма 1+2+...+K= ", total_sum)
            break
        else:
            print("Число N должно быть больше 1.")

    except ValueError:
        print("Ошибка: вы ввели не число", )
