from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import main

global blog_addres, ids, pwd, from_email, file_place
blog_address, ids, pwd, from_email, file_place = False, False, False, False, False


root = Tk()
root.resizable(False, False)
printed = ''

# 컴포넌트 정의
root.title('댓글 email 가져오기')

blog_address_label = Label(root, text='네이버 블로그 주소')
blog_address_entry = Entry(root)

id_label = Label(root, text='ID')
id_entry = Entry(root)


pwd_label = Label(root, text='PWD')
pwd_entry = Entry(root, show="*")

chrome_driver_place_label = Label(root, text='Chromedriver 위치')
chrome_driver_place_button = Button(root, text='크롬드라이버 선택하기')

null_label1 = Label(root, text='-' * 65)

from_email_label = Label(root, text='어떤 email부터 가져올까요?')
from_email_entry = Entry(root)
ok_button = Button(root, text='확인')

null_label2 = Label(root, text='\n')


def ok_button_click(string):
    global blog_address, ids, pwd, from_email, file_place
    blog_address = blog_address_entry.get()
    ids = id_entry.get()
    pwd = pwd_entry.get()

    from_email = from_email_entry.get()

    if blog_address and ids and pwd and from_email:
        results = main.Blog_Naver(blog_address, from_email, ids, pwd, file_place)
        if results:
            with open('result.txt', 'w') as f:
                for i in results:
                    f.write(i)
            showinfo('확인', '원하시는 이메일들을 성공적으로 가져왔습니다.')

            with open('result.txt', 'r') as f:
                printed = f.read()

            frame = Frame(root)
            scrollbar = Scrollbar(frame)
            scrollbar.pack(side='right', fill='y')
            result_text = Text(frame, yscrollcommand=scrollbar.set)
            result_text.insert(1.0, printed)
            result_text.configure(state='disabled')
            result_text.pack(fill="both", expand=True)
            scrollbar.config(command=result_text.yview)
            frame.grid(row=6, column=0, columnspan=3, sticky='sn')


        else:
            showerror('Error', '입력된 값 중 잘못된 값이 있습니다.\n다시 확인해주세요.')
            return 0

    else:
        showerror('Error', '입력 창에 빈칸이 있습니다.\n입력창을 모두 채워주세요.')
        return 0


def bring_to_me(string):
    global file_place
    root.filename = filedialog.askopenfilename(initialdir="C://", title="파일 열기")
    file_place = root.filename



chrome_driver_place_button.bind('<Button-1>', bring_to_me)

root.bind('<Return>', ok_button_click)

ok_button.bind('<Button-1>', ok_button_click)

# 배치
blog_address_label.grid(row=0, column=0, sticky='ew')
blog_address_entry.grid(row=0, column=1, sticky='ew')

id_label.grid(row=1, column=0, sticky='ew')
id_entry.grid(row=1, column=1, sticky='ew')

pwd_label.grid(row=2, column=0, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')

chrome_driver_place_label.grid(row=3, column=0, sticky='ew')
chrome_driver_place_button.grid(row=3, column=1, sticky='ew')

null_label1.grid(row=4, column=0, columnspan=3, sticky='ew')
from_email_label.grid(row=5, column=0, sticky='ew')
from_email_entry.grid(row=5, column=1, sticky='ew')

ok_button.grid(row=0, column=2, rowspan=6, sticky='sn')
null_label2.grid(row=6, column=0, columnspan=3, sticky='ew')

root.mainloop()
