# Проверить есть ли в последовательности целых N чисел число K
def is_k_in_sequence(sequence, k):
    return any(map(lambda x: x == k, sequence))
sequence = [1, 2, 3, 4, 5]
k = 3
if is_k_in_sequence(sequence, k):
    print(f"{k} есть в последовательности")
else:
    print(f"{k} нет в последовательности")