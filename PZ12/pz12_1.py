# Проверить есть ли в последовательности целых N чисел число K
def check_number(sequence, k):
    if k in sequence:
        return True
    else:
        return False

N = int(input('Введите количество чисел последовательности >>> '))
sequence = list(range(1, N+1))
K = int(input('Введите число K>>> '))

if check_number(sequence, K):
    print(f"Число {K} есть в последовательности {sequence}")
else:
    print(f"Числа {K} нет в последовательности {sequence}")