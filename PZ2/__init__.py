# вывод числа, полученного при перестановке цифр исходного числа
num = int(input('Введите двузначное число: '))
print((num % 10 * 10) + int(num / 10))
