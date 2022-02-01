import re
from tkinter import *
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from Functions import *

   
if __name__ == '__main__':
    Check_Last_Mail = False

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)

    def Blog_Naver():
        try:
            Url = 'https://blog.naver.com/bjdmc4/222616996072'
            mail = 0
            driver.get(url = Url)
            driver.switch_to.frame('mainFrame')
            driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]').click()
            count = 0
            while count < 2:
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                comments = soup.find_all('div', {'class': 'u_cbox_text_wrap'})

                comments = extract_email(comments)
                check_mail(mail, comments)
                if (Check_Last_Mail == True):
                    break
                else:
                    btn_more = driver.find_element(By.XPATH, '//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
                    btn_more.click()
                    prev = soup.find('strong', {'class': '_currentPageNo'})
                    prev_num = int(prev.get_text().strip())

                    if (prev_num == 1):
                        count += 1

            driver.quit()
        except:
            print("Error, Please modify the code!!")


