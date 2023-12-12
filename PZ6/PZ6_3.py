"""
Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
списка влево на K позиций (при этом AN перейдет в AN-K , AN-1 — в AN-K-1, ..AK+1 — в
A1, а исходное значение K первых элементов будет потеряно). Последние K
элементов полученного списка положить равными 0.
"""
def shift_and_zero(lst, k):
    new_lst = [0] * len(lst)
    for i in range(len(lst) - k):
        new_lst[i - k] = lst[i]
    return new_lst

lst = [1,3,5,6,7,4,9]
k = 2
if k < 1 or k >= len(lst):
    print('Ошибка! Введено неверное число k')
else:
    print(shift_and_zero(lst, k))