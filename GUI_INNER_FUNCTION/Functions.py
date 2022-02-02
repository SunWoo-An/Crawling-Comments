def Blog_Naver(Url, mail, ID, Pwd):  # 1번째 인자 : 맨 끝에 있는 메일주소 , 2번째 인자 : ID , 3번째 인자 : Password
    try:
        global list
        driver.get(url=Url)

        driver.switch_to.frame('mainFrame')

        # 블로그 안에서 바로 로그인 버튼을 누름.
        driver.find_element(By.XPATH, '//*[@id="gnb-area"]/ul/li[4]/a').click()
        
        # ID pwd 카피한 후 자동입력
        pyperclip.copy(ID)
        pyperclip.copy(Pwd)
        driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL + 'v')
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
