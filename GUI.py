from tkinter import *
from tkinter.messagebox import *
from time import sleep
root = Tk()

email_string = 'sion011218@naver.com,qwfasdf34@naver.com,23q2erfqwd@daum.net,asfgqwerg2342@gmail.com'

email_lists = email_string.split(',')


# 컴포넌트 정의
root.title('댓글 email 가져오기')
root.geometry('340x500+200+200')

blog_address_label = Label(root, text='네이버 블로그 주소\n')
blog_address_entry = Entry(root)

id_label = Label(root, text='ID\n')
id_entry = Entry(root)

pwd_label = Label(root, text='PWD')
pwd_entry = Entry(root)

ok_button_1 = Button(root, text='확인')

from_email_label = Label(root, text='어떤 email부터 가져올까요?')
from_email_entry = Entry(root)
ok_button_2 = Button(root, text='확인')

unvalid_email_label = Label(root, text='의심되는 이메일들')

# 배치
blog_address_label.grid(row=0, column=0, sticky='ew')
blog_address_entry.grid(row=0, column=1, sticky='ew')

id_label.grid(row=1, column=0, sticky='ew')
id_entry.grid(row=1, column=1, sticky='ew')

pwd_label.grid(row=2, column=0, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')

ok_button_1.grid(row=0, column=3, rowspan=3, sticky='sn')


def ok_button_1_click(string):
    crawling_cmt_label = Label(root, text='해당 포스트의 댓글에 달린 이메일들을 가져왔습니다!')
    crawling_cmt_label.grid(row=4, column=0, columnspan=3, sticky='ew')

    blog_address = blog_address_entry.get()
    ids = id_entry.get()
    pwd = pwd_entry.get()

    print(blog_address, ids, pwd)


ok_button_1.bind('<Button-1>', ok_button_1_click)

null_label = Label(root, text='''


''')
null_label.grid(row=4, column=0, columnspan=3, sticky='ew')

from_email_label.grid(row=5, column=0, sticky='ew')
from_email_entry.grid(row=5, column=1, sticky='ew')
ok_button_2.grid(row=6, column=0, columnspan=4, sticky='ew')


def ok_button_2_click(string):
    # 이메일들을 정상적으로 가져왔을 때만 실행, 아니면 except
    #ending_email = from_email_entry.get()
    #print(ending_email)
    loading_label = Label(root, text='로딩 중...')
    loading_label.grid(row=7, column=0, columnspan=3, sticky='ew')

ok_button_2.bind('<Button-1>', ok_button_2_click)

sleep(3)



if True:
    loading_label.config(text='성공적으로 불러왔습니다! 이메일 리스트가 적힌 메모장 파일을 저장하세요.')
    
    see_result_button = Button(root,text='이메일 리스트 보기')
    see_result_button.grid()
    def see_result_button_click(string):


result_label = Label(root,text=str(email_lists))
result_label.grid(row=8, column=0, columnspan=3, sticky='ew')

root.mainloop()

