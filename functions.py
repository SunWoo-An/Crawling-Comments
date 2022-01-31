import re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# 함수인자로 Chromedriver 위치와 Blog 의 주소를 받아오는 함수
def Blog(location,url):
    driver.webdriver.chrome(location)
    driver.get(url)

    driver.switch_to.frame('mainFrame')



# 2번째 이용자일시, 이전에 크롤링해왔던 댓글들을 제외한 새로운 댓글들을 받아오는 함수
def check_mail(mail):
    Mail_list = []
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    comments = soup.find_all('div', {'class' : 'u_cbox_text_wrap'})

    for comment in comments:
        if(comment != mail):
            Mail_list.append(comment)
        else:
            break
    
