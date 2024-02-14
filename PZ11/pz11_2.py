# Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.

# Чтение содержимого файла и подсчёт количества символов
f3 = open('text18-13.txt', 'r', encoding='UTF-16LE')
content = f3.read()
char_count = len(content)
print(content)
print(f'Количество символов в тексте: {char_count}')

# Вставка произвольной фразы после строки N и запись в новый файл
N = int(input('Введите номер строки N: '))
phrase = input('Введите произвольную фразу: ')
lines = content.split('\n')
lines.insert(N, phrase)
new_content = '\n'.join(lines)

f3 = open('new_file.txt', 'w', encoding='UTF-16LE')
f3.write(new_content)