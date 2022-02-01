import re
from tkinter import *
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import Functions
from Functions import *

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe', options = options)

    list = []


    def Blog_Naver():
        try:
            global list
            Url = 'https://blog.naver.com/bjdmc4/222616996072'
            mail = 0
            driver.get(url=Url)


            driver.switch_to.frame('mainFrame')
            com = driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]')
            sleep(2)
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
            driver.quit()
        except:
            print('Error!! Modify the code please...\n')

    root = Tk()
    root.title("Practice")
    # 버튼을 여러번 눌러서 항상 새로운 메일이 들어올 수 있도록 준비를 해놓는 것이 어떤지...
    # 그리고 지금은 끝에 있는 메일을 받아오지만 조금 더 향상시키기 위해서는 Mail들을 리스트로 받아온 다음에 맨 끝 메일을 저장해두는 것이 어떤가 싶다. ( 프로그램이 켜져있는 동안에만 )
    btn = Button(root, text='Please..', command=Blog_Naver)
    btn.pack()


    root.mainloop()
