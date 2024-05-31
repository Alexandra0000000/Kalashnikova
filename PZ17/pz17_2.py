#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.

# Данны три целых числа A, B, C.
# Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное"

import tkinter as tk

def check_numbers():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())

        if (a > 0) or (b > 0) or (c > 0):
            result_label.config(text="True")
        else:
            result_label.config(text="False")
    except ValueError:
        result_label.config(text="Error!!! Введите число")

root = tk.Tk()
root.title("Проверка чисел")

a_label = tk.Label(root, text="Введите первое число:")
a_label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Введите второе число:")
b_label.pack()
b_entry = tk.Entry(root)
b_entry.pack()

c_label = tk.Label(root, text="Введите третье число:")
c_label.pack()
c_entry = tk.Entry(root)
c_entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_numbers)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()