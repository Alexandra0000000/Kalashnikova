# Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг
# (A, B, C) - вещественные параметры, являющиеся входными и выходными одновременно
# С помощью этой функции выполнить правый циклический сдвиг для двух данных наборов из трех чисел
def ShiftRight3(A, B, C):
    temp = A
    A = C
    C = B
    B = temp
    return A, B, C

A1, B1, C1 = 1, 2, 3
A2, B2, C2 = 4, 5, 6

print("Первый набор чисел до циклического сдвига: ", A1, B1, C1)
# применение функции для первого набора
A1, B1, C1 = ShiftRight3(A1, B1, C1)
print("Первый набор чисел после циклического сдвига: ", A1, B1, C1)

print("второй набор чисел до циклического сдвига: ", A2, B2, C2)
# применение функции для второго набора
A2, B2, C2 = ShiftRight3(A2, B2, C2)
print("второй набор чисел после циклического сдвига: ", A2, B2, C2)