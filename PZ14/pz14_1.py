# В строках исходного текстового файла (dates1.txt) все даты представить в виде
# подстроки. Поместить в новый текстовый файл все даты февраля в формате
# ДД/ММ/ГГГГ.
import re

with open('dates1.txt', 'r') as file:
    content = file.read()

feb_dates = re.findall(r'\b(0[1-9]|1\d|2[0-8])\.02\.2022\b', content)

with open('february_dates_regex.txt', 'w') as new_file:
    for date in feb_dates:
        day = date.split('.')[0]
        formatted_date = f'{day}/02/2022'
        new_file.write(formatted_date + '\n')