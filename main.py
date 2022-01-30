# !/usr/bin/env python
# Backup File

# 최근에 사용되는 Selenium 패키지 같은 경우 Find_element_by_XPATH 가 아닌
# find_element(By.XPATH, {'클래스' : '클래스 이름'}) 과 같은 형태를 띄워야함
# 그러므로 improt By 를 해줘야한다.

import re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


# 로그인의 경우 pyperclip 을 사용하지 않았을 경우
# 봇으로 인식해 네이버의 클린봇에게 걸려 수동으로 작성하였다.


# 메일 주소 담는 리스트
Mail_Address = []

# 블로그 url
url = 'https://blog.naver.com/bjdmc4/222616996072'

# 크롬 드라이버를 실행하는 과정
# 크롬 드라이버를 실행할 때에 위치를 적어주는 경우 \\ 로 메꿔야함
driver = webdriver.Chrome('C:\\Users\\CKIRUser\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get(url)

# 블로그의 경우 HTMl 에서 frame 이 나눠져있어 frame Name 을 잘보고 Frame 을 바꿔줘야함
# 그래서 아래와 같은 작업을 하였음
driver.switch_to.frame('mainFrame')

# 블로그 안에서 바로 로그인 버튼을 누름.
driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
sleep(20)
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
sleep(10)

# 로그인을 한 뒤에 프레임을 바꿈
driver.switch_to.frame('mainFrame')

# 댓글창을 클릭하는 Part
driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]').click()
driver.implicitly_wait(10)

# 맨 끝에 도달하였을 때 1인 페이지들을 가져와야하므로 count 를 넣어주었음
count = 0

# 1인 페이지를 크롤링 해온 후 종료를 해야하므로 종료 조건을 넣어주었음
while count < 2:

    # 페이지 구성요소 크롤링 해오는 부분
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    comments = soup.find_all('div', {'class': 'u_cbox_text_wrap'})

    # 댓글을 크롤링 해오는 부분 (텍스트만)
    for comment in comments:
        Mail_Address.append(comment.get_text().strip())

    # 댓글 페이지 버튼을 옮기는 부분
    btn_more = driver.find_element(By.XPATH, '//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
    btn_more.click()

    prev = soup.find('strong', {'class' : '_currentPageNo'})
    prev_num = int(prev.get_text().strip())

    if(prev_num == 1): # 댓글페이지 수가 1 이 될 경우 count를 올림.
        count+= 1

# 가져온 댓글리스트를 메모장으로 옮기는 과정
with open('test2.txt', 'w', encoding='UTF-8') as f:
    for line in Mail_Address:
        f.write(line)
sleep(10)

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

email_list = extract_email(Mail_Address)
email_list = list(map(lambda x: x + ',', email_list))
print(email_list)

with open('test1.txt', 'w', encoding='UTF-8') as f:
    for line in email_list:
        f.write(line)

#크롬드라이버를 종료해주었다.
driver.quit()
