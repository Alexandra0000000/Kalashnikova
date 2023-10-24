# Дан номер года.
# Определить количество дней в году
# Если год високосный, то вывести 366
# Если год обычный, то вывести 365
while True:
    try:
        year = int(input("Введите номер года: "))

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days = 366
            print("Количество дней в году: ", days)
        else:
             days = 365
             print("Количесво дней в году: ", days)

        break

    except ValueError:
        print("Error!!! Введите год")
