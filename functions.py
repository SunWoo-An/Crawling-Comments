import re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

Check_Last_Mail = False

# 함수인자로 Chromedriver 위치와 Blog 의 주소를 받아오는 함수
def Naver_Blog(mail, location, url):

    driver.webdriver.chrome(location)
    driver.get(url)
    driver.switch_to.frame('mainFrame')
    count = 0
    while count < 2:
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        comments = soup.find_all('div', {'class' : 'u_cbox_text_wrap'})

        comments = extract_email(comments)
        check_mail(mail, comments)
        if (Check_Last_Mail == True):
            break
        else:
            btn_more = driver.find_element(By.XPATH,'')
            btn_more.click()
            prev = soup.find('strong',{'class' : ''})
            prev_num = int(prev.get_text().strip())

            if(prev_num == 1):
                count += 1

    driver.quit()


# check_mail 함수가 너무 시간상으로 효율적이지 않음 이것을 새롭게 구현해볼 수 있지는 않을까?

# 2번째 이용자일시, 이전에 크롤링해왔던 댓글들을 제외한 새로운 댓글들을 받아오는 함수
# 1번째 이용자여도 이를 실행시킬 수 있도록 하는 것이 포인트이다.
def check_mail(mail, comments):
    Mail_list = []
    if(int(mail) == 0):
        for comment in comments:
            Mail_list.append(comment)
    else:
        # for문이 아닌 자료구조를 통해서 쉽게 search를 먼저 한 뒤에 list 에 넣는 방법을 생각해보자.
        for comment in comments:
            if (comment != mail):
                Mail_list.append(comment)
            else:
                Check_Last_Mail = True
    with open('Defined Lists.txt', 'w', encoding='UTF-8') as f:
        for line in Mail_list:
            f.write(line)

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
