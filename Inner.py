import re
from tkinter import *
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import Functions
from Functions import *

# 클래스 만들기.. 생성자?!

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')

    # url 을 바꿔주셔야합니다!!!!
    driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe', options = options)

    list = []

    def Blog_Naver(mail, ID, Pwd): # 1번째 인자 : 맨 끝에 있는 메일주소 , 2번째 인자 : ID , 3번째 인자 : Password
        try:
            global list
            Url = 'https://blog.naver.com/bjdmc4/222616996072'
            driver.get(url=Url)

            #driver.switch_to.frame('mainFrame')

            # 블로그 안에서 바로 로그인 버튼을 누름.
            #driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
            #sleep(20)


            #driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
            #sleep(10)

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
                    left = driver.find_element(By.XPATH, '//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
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
        label1 = Label(root, text = "추출이 완료되었습니다...")
        label1.pack()

    root = Tk()
    root.title("Practice")

    # 버튼을 여러번 눌러서 항상 새로운 메일이 들어올 수 있도록 준비를 해놓는 것이 어떤지...
    # 그리고 지금은 끝에 있는 메일을 받아오지만 조금 더 향상시키기 위해서는 Mail들을 리스트로 받아온 다음에 맨 끝 메일을 저장해두는 것이 어떤가 싶다. ( 프로그램이 켜져있는 동안에만 )
    def starting():
        Blog_Naver('0','1','1')
    btn = Button(root, text='Please..', command=starting)
    btn.pack()
    root.mainloop()
