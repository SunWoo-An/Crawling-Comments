#!/usr/bin/env python

import pyperclip
import re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request as req

#로그인 파트

#메일 주소 담는 리스트
Mail_Address = []

# 블로그 url
url = 'https://blog.naver.com/bjdmc4/222616996072'

# 네이버 홈화면에서 로그인하는 Part
driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
driver.get(url)
driver.switch_to.frame('mainFrame')

driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
sleep(20)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

# 댓글창을 클릭
sleep(10)
driver.switch_to.frame('mainFrame')
driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]').click()
driver.implicitly_wait(10)

while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    comments = soup.find_all('div', {'class': 'u_cbox_text_wrap'})
    for comment in comments:
        Mail_Address.append(comment.get_text().strip())
    try:
        btn_more = driver.find_element(By.XPATH, '//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
        btn_more.click()
        driver.implicitly_wait(10)

    except:
        break


#for i in Mail_Address:
#    print(i + '\n')


def email_preprocessing(string):
    valid_email = re.compile('[A-Za-z0-9]+@[a-z]+[.]+[a-z]+')

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


# email저장


email_list = extract_email(Mail_Address)

email_list = list(map(lambda x: x + ',', email_list))

print(email_list)

with open('test.txt', 'w') as f:
    for line in email_list:
        f.write(line)



driver.quit()