from tkinter import *
from tkinter.messagebox import *
from time import sleep
import os

root = Tk()
root.resizable(False,False)
email_string = 'sion011218@naver.com,qwfasdf34@naver.com,23q2erfqwd@daum.net,asfgqwerg2342@gmail.com,wqff32@hanmail.net,423dfw@hkd.hs'

email_lists = email_string.split(',')

# 컴포넌트 정의
root.title('댓글 email 가져오기')
#root.geometry('400x500')

blog_address_label = Label(root, text='네이버 블로그 주소')
blog_address_entry = Entry(root)

id_label = Label(root, text='ID')
id_entry = Entry(root)

pwd_label = Label(root, text='PWD')
pwd_entry = Entry(root)

ok_button_1 = Button(root, text='확인')

null_label1 = Label(root,text='''
 ''')
def ok_button_1_click(string):

    global crawling_cmt_label
    crawling_cmt_label = Label(root, text='해당 포스트의 댓글에 달린 이메일들을 가져왔습니다!')
    crawling_cmt_label.grid(row=4, column=0, columnspan=3, sticky='ew')

    blog_address = blog_address_entry.get()
    ids = id_entry.get()
    pwd = pwd_entry.get()

    print(blog_address, ids, pwd)

ok_button_1.bind('<Button-1>', ok_button_1_click)

null_label2 = Label(root,text='''
''')

from_email_label = Label(root, text='어떤 email부터 가져올까요?')
from_email_entry = Entry(root)
ok_button_2 = Button(root,text='확인')

def ok_button_2_click(string):
    std_email = from_email_entry.get()
    # std_email = asfgqwerg2342@gmail.com
    idx = email_lists.index(std_email)
    result_list = email_lists[:idx+1]
    print(result_list)
    print_clear_label = Label(root,text='이메일을 모두 가져왔습니다!')
    print_clear_label.grid(row=7, column=0, sticky='ew')
    with open('result.txt','w') as f:
        for i in result_list:
            f.write(i)

    view_file_button = Button(root,text='결과 파일 보기')
    view_file_button.grid(row=7, column=1, columnspan=2, sticky='ew')

    def view_file_button_click(string):
        os.system('C:\\Users\\CKIRUser\\PycharmProjects\\pythonProject\\result.txt')

    view_file_button.bind('<Button-1>', view_file_button_click)

ok_button_2.bind('<Button-1>', ok_button_2_click)




# 배치
blog_address_label.grid(row=0, column=0, sticky='ew')
blog_address_entry.grid(row=0, column=1, sticky='ew')

id_label.grid(row=1, column=0, sticky='ew')
id_entry.grid(row=1, column=1, sticky='ew')

pwd_label.grid(row=2, column=0, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')

ok_button_1.grid(row=0, column=3, rowspan=3, sticky='sn')

null_label1.grid(row=3, column=0, columnspan=3, sticky='ew')

null_label2.grid(row=5, column=0, columnspan=3, sticky='ew')

from_email_label.grid(row=6, column=0, sticky='ew')
from_email_entry.grid(row=6, column=1, sticky='ew')

ok_button_2.grid(row=6, column=2, sticky='ew')




root.mainloop()

