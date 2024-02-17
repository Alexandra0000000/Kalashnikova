# Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир'].

# Исходный список
words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
result = []

# Перебираем слова в исходном списке
for word in words:
    consonant_letters = [letter for letter in word if letter.upper() in consonants]
    result.append(''.join(consonant_letters))

print(result)
