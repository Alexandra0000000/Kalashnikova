"""
Дана строка. Подсчитать количество содержащихся в ней цифр
"""
s = '345 ujdji 3126hidk 9jkjk'
summa = sum([1 for i in s if i.isdigit()])
print(summa)