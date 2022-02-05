import re
import pyperclip
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

check_mail = False
mail_index = 0

def Blog_Naver(Url, mail, ID, Pwd, driver_place):  # 1번째 인자 : 맨 끝에 있는 메일주소 , 2번째 인자 : ID , 3번째 인자 : Password
    Defined_list = []
    driver_place = driver_place.replace("\\","\\\\")
    driver = webdriver.Chrome(driver_place)
    global check_mail
    global mail_index
    global is_error
    is_error = False
    try:
        driver.get(url=Url)
        driver.switch_to.frame('mainFrame')
        # 블로그 안에서 바로 로그인 버튼을 누름.
        driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
        # ID pwd 카피한 후 자동입력
        pyperclip.copy(ID)
        driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL + 'v')
        sleep(1)
        pyperclip.copy(Pwd)
        driver.find_element(By.ID, 'pw').send_keys(Keys.CONTROL + 'v')
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
        driver.implicitly_wait(3)

        driver.switch_to.frame('mainFrame')
        com = driver.find_element(By.XPATH, '//*[@id="Comi222616996072"]')

        sleep(1)
        com.click()
        count = 0
        while count < 2:
            lists = []
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            comments = soup.find_all('div', {'class': 'u_cbox_text_wrap'})
            for comment in comments:
                lists.append(comment.get_text().strip())
            lists = extract_email(lists)
            scrattered_list = check_mails(mail, lists)
            if (check_mail == True):
                Defined_list.extend(scrattered_list[mail_index:])
                break
            else:
                Defined_list.extend(scrattered_list)
                driver.implicitly_wait(5)
                left = driver.find_element(By.XPATH,'//*[@id="naverComment_201_222616996072_ct"]/div[1]/div/div[2]/a[1]')
                left.click()
                prev = soup.find('strong', {'class': '_currentPageNo'})
                prev_num = int(prev.get_text().strip())
                print(prev_num)
            if (prev_num == 1):
                count += 1
        insert_txt(Defined_list)
        driver.quit()

        Defined_list = list(map(lambda x: x + ',', Defined_list))
        return Defined_list

    except:
        is_error = True
        return False


def check_mails(mail, comments):
    i = 0
    global check_mail
    global mail_index
    last_list = []
    if (str(mail) == '0'):
        for comment in comments:
            last_list.append(comment)
    else:
        # for문이 아닌 자료구조를 통해서 쉽게 search를 먼저 한 뒤에 list 에 넣는 방법을 생각해보자.
        for comment in comments:
            if (comment != mail):
                last_list.append(comment)
            else:
                last_list.append(comment)
                check_mail = True
                mail_index = i
            i += 1
    return last_list


def insert_txt(list_name):
    with open('Defined Lists.txt', 'w', encoding='UTF-8') as f:
        for line in list_name:
            f.writelines(line)


def email_preprocessing(string):
    valid_email = re.compile('[A-Za-z0-9]+[A-Za-z0-9-_+.]+@[a-z]+[.]+[a-z]+')
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
