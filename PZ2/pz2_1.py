# вывод числа, полученного при перестановке цифр исходного числа
while True:  # обработка исключений
    try:
        num = int(input('Введите двузначное число: '))
        if num <= 9 or num > 99:
            print("Ошибка! Введите двузначное число")
            continue
        break
    except ValueError:
        print("Вы ввели не число")
print((num % 10 * 10) + int(num / 10))  # вывод значения
