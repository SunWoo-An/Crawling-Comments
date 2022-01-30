import re


# 댓글 중 이메일 문자열 추출

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

# comment list exapmle

cmlist=['정말 감사합니다! sion011218@naver.com'
       ,'한번 해보겠습니다!aefwe34_..??@daum.net입니당']

email_list = extract_email(cmlist)

email_list = list(map(lambda x:x+',',email_list))

with open('email_lists.txt', 'w', encoding='UTF-8') as f:
    for line in email_list:
        f.write(line)
        
