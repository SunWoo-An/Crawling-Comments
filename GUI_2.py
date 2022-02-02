
import re
from tkinter import *
from time import sleep
import os

root = Tk()
root.title('Crawling')
root.geometry('240x240')
root.resizable(False,False)

filename = 'Defined Lists.txt'

def open():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            txt.insert(END, file.read())

def save():
    with open(filename, 'w', encoding= 'UTF-8') as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = 'open', command = open)
menu_file.add_command(label = 'save', command= save)
menu_file.add_separator()
menu_file.add_command(label = 'Exit', command = root.quit)
menu.add_cascade(label='파일', menu = menu_file)


#
Iframe = Frame(root)
Iframe.pack()


#
frame = Frame(Iframe)
frame.pack(side = 'top')

label1 = Label(frame, text="Blog_url")
label1.pack(side='left')
blog_txt = Entry(frame)
blog_txt.pack(side = 'right')

#
frame2 = Frame(Iframe)
frame2.pack(side = 'top')

label2 = Label(frame2, text = "ID")
label2.pack(side='left')
ID_txt = Entry(frame2)
ID_txt.pack(side = 'right')

#
frame3 = Frame(Iframe)
frame3.pack(side = 'top')

label3 = Label(frame3, text = "PWD")
label3.pack(side='left')
PWD_text = Entry(frame3)
PWD_text.pack(side = 'right')

#
frame4 = LabelFrame(Iframe, text='Last Email')
frame4.pack(pady = 5, side = 'top')

label4 = Label(frame4, text = "Email")
label4.pack(side='left')
Email_text = Entry(frame4)
Email_text.pack(side= 'right')

def Enter():
    url = blog_txt.get()
    ID = ID_txt.get()
    PWD = PWD_text.get()
    Email = Email_text.get()

btn1 = Button(Iframe,text="Enter",command=Enter)
btn1.pack(side='right')

# 스크롤바
frame5 = Frame(root)
frame5.pack()

scrollbar = Scrollbar(frame5)
scrollbar.pack(side="right", fill="y")

# 보여주는 영역
txt = Text(frame5, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill = "both", expand = True)
scrollbar.config(command=txt.yview)


root.config(menu = menu)
root.mainloop()
