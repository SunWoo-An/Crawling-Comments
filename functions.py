import re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By




# 함수인자로 Chromedriver 위치와 Blog 의 주소를 받아오는 함수
def Naver_Blog(mail,location,url):
    driver.webdriver.chrome(location)
    driver.get(url)
    driver.switch_to.frame('mainFrame')


    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    comments = soup.find_all('div', {'class' : 'u_cbox_text_wrap'})

    check_mail(mail, comments)


    driver.quit()

# 2번째 이용자일시, 이전에 크롤링해왔던 댓글들을 제외한 새로운 댓글들을 받아오는 함수
# 1번째 이용자여도 이를 실행시킬 수 있도록 하는 것이 포인트이다.
def check_mail(mail, comments):
    Mail_list = []

    # for문이 아닌 자료구조를 통해서 쉽게 search를 먼저 한 뒤에 list 에 넣는 방법을 생각해보자.
    for comment in comments:
        if(comment != mail):
            Mail_list.append(comment)
        else:
            break

    with open('Defined Lists.txt', 'w', encoding='UTF-8') as f:
        for line in Mail_list:
            f.write(line)
