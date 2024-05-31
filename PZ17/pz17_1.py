from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title('Registration')
root.geometry('500x600')
root.configure(bg='#2e2c2c')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 440
window_height = 580

position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

def on_entry_click(event):
    if reg_entry.get() == 'Username':
        reg_entry.delete(0, "end")
        reg_entry.insert(0, '')
        reg_entry.config(fg='#2e2c2c')

def on_focusout(event):
    if reg_entry.get() == '':
        reg_entry.insert(0, '')
        reg_entry.config(fg='#2e2c2c')

# Style
style = ttk.Style()
style.configure('TEntry', fieldbackground='#2e2c2c', foreground='white', relief='flat', height=2, borderradius=5)

# FRAME TEXT
frame_text = Frame(root, bg='#2e2c2c', relief=SUNKEN)
frame_text.place(x=0, y=0, anchor='nw', width=440, height=100)

reg_text = Label(frame_text, text="Sign Up", font='arial 14', fg='#aba2a2', background='#545151', width='60', height=2)
reg_text.pack(anchor='nw', padx=25, pady=(25, 0))

# FRAME FORM
frame_form = Frame(root, bg='#171616', relief=SUNKEN)
frame_form.place(x=25, y=71, width=390, height=480)

# Field registration
reg_label = Label(frame_form, text="Username", fg='#aba2a2', font='arial 12 bold', background='#171616')
reg_label.grid(row=0, column=0, padx=29, pady=(15, 3), sticky='nw')
reg_entry = ttk.Entry(frame_form, width=40, style="TEntry")
reg_entry.insert(0, 'Username')
reg_entry.bind('<FocusIn>', on_entry_click)
reg_entry.bind('<FocusOut>', on_focusout)
reg_entry.grid(row=1, column=0, padx=30, pady=(0, 3))

# Field email
email_label = Label(frame_form, text="Email", fg='#aba2a2', font='arial 12 bold', background='#171616')
email_label.grid(row=3, column=0, padx=29, pady=(15, 3), sticky='nw')
email_entry = ttk.Entry(frame_form, width=40, style="TEntry")
email_entry.insert(0, 'Email')
email_entry.bind('<FocusIn>', on_entry_click)
email_entry.bind('<FocusOut>', on_focusout)
email_entry.grid(row=4, column=0, padx=30, pady=(0, 3))

# Field password
password_label = Label(frame_form, text="Password", fg='#aba2a2', font='arial 12 bold', background='#171616')
password_label.grid(row=6, column=0, padx=29, pady=(15, 3), sticky='nw')
password_entry = ttk.Entry(frame_form, width=40, style="TEntry")
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', on_entry_click)
password_entry.bind('<FocusOut>', on_focusout)
password_entry.grid(row=7, column=0, padx=30, pady=(0, 3))

# Field retype password
retype_password_label = Label(frame_form, text="Retype password", fg='#aba2a2', font='arial 12 bold', background='#171616')
retype_password_label.grid(row=9, column=0, padx=29, pady=(15, 3), sticky='nw')
retype_password_entry = ttk.Entry(frame_form, width=40, style="TEntry")
retype_password_entry.insert(0, 'Retype password')
retype_password_entry.bind('<FocusIn>', on_entry_click)
retype_password_entry.bind('<FocusOut>', on_focusout)
retype_password_entry.grid(row=10, column=0, padx=30, pady=(0, 3))

# Field check language
frame_accept = Frame(root, bg='#171616', relief=SUNKEN)
frame_accept.place(x=46, y=355, width=340, height=80)
accept_var1 = StringVar()

accept_check1 = Checkbutton(frame_accept, variable=accept_var1, offvalue='', font='arial 11', bg='#171616')
accept_check1.grid(row=0, column=0, padx=10, pady=(0, 3))

language_label = Label(frame_accept, text="Accept the terms and policies", font='arial 11', fg='#aba2a2', background='#171616')
language_label.grid(row=0, column=1, pady=(0, 3))

btn_lab = Button(root, text='SIGN UP', width=8, height=1, font='arial 13 bold', bg='#00b3ff', fg='white')
btn_lab.place(x=56, y=400)

text_lab = Label(root, text='Already have an account?', width=40, height=1, font='arial 11', bg='#171616', fg='white')
text_lab.place(x=56, y=450)

btn_signin = Button(root, text='SIGN IN', width=33, height=1, font='arial 13 bold', bg='#636769', fg='white')
btn_signin.place(x=56, y=480)






root.mainloop()