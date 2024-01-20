" Организовать словарь 10 русско-английских слов, обеспечивающий перевод русского слова на английского."
def translate(dict, word):
    return dict.get(word, "Слово не найдено. Повторите попытку")

transletion = {"машина": "car", "мама": "mother", "брат": "brother", "сестра": "sister", "кровать": "bed",
               "шкаф": "closet", "медведь": "bear", "окно": "window", "стул": "chair", "чай": "tea"}

print(transletion)
while True:
    word = input('Введите слово на русском из предложенного словаря для перевода на английский >> ')
    print(translate(transletion, word))

