# check_mail 함수가 너무 시간상으로 효율적이지 않음 이것을 새롭게 구현해볼 수 있지는 않을까?
# 2번째 이용자일시, 이전에 크롤링해왔던 댓글들을 제외한 새로운 댓글들을 받아오는 함수
# 1번째 이용자여도 이를 실행시킬 수 있도록 하는 것이 포인트이다.

import re
import os
from tkinter import *
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    Check_Last_Mail = False
    Final_list = []

    filename_txt = 'Defined Lists.txt'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')

    # url 을 바꿔주셔야합니다!!!!
    driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32\\chromedriver.exe', options = options)

    list = []
    
    root = Tk()
    root.title('Crawling')
    root.geometry('240x240')
    root.resizable(False, False)

    

    filename_txt = 'Defined Lists.txt'
    def open_txt():
        if os.path.isfile(filename_txt):
            txt.delete("1.0", END)
            with open(filename_txt, 'r', encoding='utf8') as file:
                txt.insert(END, file.read())

    def save():
        with open(filename_txt, 'w') as file:
            file.write(txt.get("1.0", END))

    menu = Menu(root)
    menu_file = Menu(menu, tearoff = 0)
    menu_file.add_command(label = 'open', command = open_txt)
    menu_file.add_command(label = 'save', command= save)
    menu_file.add_separator()
    menu_file.add_command(label = 'Exit', command = root.quit)
    menu.add_cascade(label='파일', menu = menu_file)



    # 사용자 정보를 받아오는 Frame
    Iframe = Frame(root)
    Iframe.pack()


    # Blog_url 을 받아오는 Frame
    frame = Frame(Iframe)
    frame.pack(side = 'top')

    label1 = Label(frame, text="Blog_url")
    label1.pack(side='left')
    blog_txt = Entry(frame)
    blog_txt.pack(side = 'right')

    # ID 를 받아오는 Frame
    frame2 = Frame(Iframe)
    frame2.pack(side = 'top')

    label2 = Label(frame2, text = "ID")
    label2.pack(side='left')
    ID_txt = Entry(frame2)
    ID_txt.pack(side = 'right')

    # PWD 를 받아오는 Frame
    frame3 = Frame(Iframe)
    frame3.pack(side = 'top')

    label3 = Label(frame3, text = "PWD")
    label3.pack(side='left')
    PWD_text = Entry(frame3)
    PWD_text.pack(side = 'right')

    # 마지막 Email 주소를 받아오는 Frame
    frame4 = LabelFrame(Iframe, text='Last Email')
    frame4.pack(pady = 5, side = 'top')

    label4 = Label(frame4, text = "Email")
    label4.pack(side='left')
    Email_text = Entry(frame4)
    Email_text.pack(side= 'right')


    def check_mail(mail, comments):
        i = 0
        global Final_list
        global Check_Last_Mail
        if (int(mail) == 0):
            for comment in comments:
                Final_list.append(comment)
        else:
            # for문이 아닌 자료구조를 통해서 쉽게 search를 먼저 한 뒤에 list 에 넣는 방법을 생각해보자.
            for comment in comments:
                if (comment != mail):
                    Final_list.append(comment)
                else:
                    Check_Last_Mail = True
                    break
        return Check_Last_Mail


    def insert_txt():
        global Final_list
        with open('Defined Lists.txt', 'w', encoding='UTF-8') as f:
            for line in Final_list:
                f.writelines(line)


    def email_preprocessing(string):
        valid_email = re.compile('[A-Za-z0-9-_+]+@[a-z]+[.]+[a-z]+')
        result = valid_email.search(string)

        if result:
            return result.group()

        else:
            return result


    def extract_email(comment):
        result = []

        for each_comment in comment:
            comment_token = each_comment.split(' ')
            if email_preprocessing(comment_token[0]):
                preclean = email_preprocessing(comment_token[0])
                result.append(preclean)

            elif email_preprocessing(comment_token[-1]):
                preclean = email_preprocessing(comment_token[-1])
                result.append(preclean)

            else:
                for tokens in comment_token:
                    if email_preprocessing(tokens):
                        preclean = email_preprocessing(tokens)
                        result.append(preclean)
                        break

        return result


    def Blog_Naver(self, mail, ID, Pwd):  # 1번째 인자 : 맨 끝에 있는 메일주소 , 2번째 인자 : ID , 3번째 인자 : Password
        try:
            global list
            Url = 'https://blog.naver.com/bjdmc4/222616996072'
            driver.get(url=Url)

            # driver.switch_to.frame('mainFrame')

            # 블로그 안에서 바로 로그인 버튼을 누름.
            # driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
            # sleep(20)

            # driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
            # sleep(10)

            driver.switch_to.frame('mainFrame')
            com = driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]')

            sleep(1)
            com.click()

            count = 0
            while count < 2:
                list = []
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                comments = soup.find_all('div', {'class': 'u_cbox_text_wrap'})

                for comment in comments:
                    list.append(comment.get_text().strip())
                list = extract_email(list)
                Check = check_mail(mail, list)

                if (Check == True):
                    break
                else:
                    driver.implicitly_wait(5)
                    left = driver.find_element(By.XPATH,
                                               '//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
                    left.click()
                    prev = soup.find('strong', {'class': '_currentPageNo'})
                    prev_num = int(prev.get_text().strip())
                    print(prev_num)
                if (prev_num == 1):
                    count += 1
            insert_txt()
            driver.quit()
        except:
            print('Error!! Modify the code please...\n')
        label1 = Label(root, text="추출이 완료되었습니다...")
        label1.pack()

    def Enter():
        url = blog_txt.get()
        ID = ID_txt.get()
        PWD = PWD_text.get()
        Email = Email_text.get()
        Blog_Naver(Email, ID, PWD)

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
