# сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого максимального элемента:
# Произведение элементов средней трети:

# создание последовательности из целых положительных и отрицательных чисел
nums = ['32 74 95 7 4 -2 6 13 29']
f1 = open('data_1.txt', 'w')
f1.writelines(nums)
f1.close()

# Исходные данные:
f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(nums)
f2.close()

# Количество элементов:
f1 = open('data_1.txt')
m = f1.read()
m = m.split()
for i in range(len(m)):
    m[i] = int(m[i])
f1.close()

f2 = open('data_2.txt', 'a')
f2.write('\n')
print('Количество элементов: ', len(m), file = f2)
f2.close()

# Индекс первого максимального элемента:
m = list(map(int, nums[0].split()))
max_index = m.index(max(m))
# Запись результатов в файл data_2.txt
f2 = open('data_2.txt', 'a')
f2.write(f'Индекс первого максимального элемента: {max_index}\n')

# Произведение элементов средней трети:
third = len(m) // 3
middle_third = m[third:2*third]
middle_third_product = 1
for num in middle_third:
    middle_third_product *= num

# Запись результатов в файл data_2.txt
f2 = open('data_2.txt', 'a')
f2.write(f'Произведение элементов средней трети: {middle_third_product}\n')

