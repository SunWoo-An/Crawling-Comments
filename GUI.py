from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title('댓글 email 가져오기')
root.geometry('400x700+100+100')
blog_address_label = Label(root,text='블로그 주소')
blog_address_entry = Entry(root)

id_label = Label(root,text='ID')
id_entry = Entry(root)

pwd_label = Label(root,text='PWD')
pwd_entry = Entry(root)

ok_button_1 = Button(root,text='확인')

def ok_button_1_click(string):
    crawling_cmt_label = Label(root,text='해당 포스트의 댓글들을 가져왔습니다!')
    crawling_cmt_label.grid(row=4, column=0, columnspan=3, sticky='ew')

ok_button_1.bind('<Button-1>',ok_button_1_click)

from_email_label = Label(root,text='어떤 email부터 가져올까요?')
from_email_entry = Entry(root)
ok_button_2 = Button(root,text='확인')

def ok_button_2_click(string):
    loading_label = Label(root,text='로딩 중...')
    loading_label.grid(row=7, column=0, columnspan=3, sticky='ew')

ok_button_2.bind('<Button-1>',ok_button_2_click)


blog_address_label.grid(row=0, column=0, sticky='ew')
blog_address_entry.grid(row=0, column=1, sticky='ew')

id_label.grid(row=1, column=0, sticky='ew')
id_entry.grid(row=1, column=1, sticky='ew')

pwd_label.grid(row=2, column=0, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')

ok_button_1.grid(row=1, column=3, rowspan=4, sticky='sn')

from_email_label.grid(row=5, column=0, sticky='ew')
from_email_entry.grid(row=5, column=1, sticky='ew')
ok_button_2.grid(row=6, column=0, columnspan=3, sticky='ew')
root.mainloop()
