# Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных запасов на складе.
# БД должна содержать таблицу Товары со следующей структурой записи:
# Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный запас .

import sqlite3 as sq
from data_tovar import info_tovar

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS tovary")

    cur.execute("""CREATE TABLE IF NOT EXISTS tovary(
    tovary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kod_tovara INTEGER,
    marka TEXT NOT NULL,
    type TEXT NOT NULL,
    price INTEGER,
    kolvo INTEGER,
    min_zapas INTEGER 
    )""")

    with sq.connect('tovarny_zapas.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO tovary VALUES (?, ?, ?, ?, ?, ?, ?)", info_tovar)


with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tovary WHERE kolvo > 20 AND min_zapas < 7")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tovary WHERE price > 8000")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM tovary WHERE min_zapas < 4")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE tovary SET price = price+300 WHERE marka LIKE 'A%'")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE tovary SET kolvo = kolvo+3 WHERE type LIKE 'shoes'")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE tovary SET min_zapas = min_zapas+1 WHERE type LIKE 't-shirts'")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tovary WHERE tovary_id = 9")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tovary WHERE marka = 'Puma'")
    result = cur.fetchall()
    print(result)

with sq.connect('tovarny_zapas.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM tovary WHERE kolvo < 9 AND min_zapas < 3")
    result = cur.fetchall()
    print(result)