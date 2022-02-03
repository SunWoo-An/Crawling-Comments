from tkinter import *
from tkinter.messagebox import *
import main
global blog_addres, ids, pwd
blog_address, ids, pwd, from_email = False, False, False, False

root = Tk()
root.resizable(False, False)
email_string = 'eunj0407@naver.com,sunkung0118@naver.com,sion011218@naver.com,sumsum3_@naver.com,hhyowon020304@gmail.com,eh040117@gmail.com,only4352@naver.com,thdnjs9853@naver.com,cmcm0722@gmail.com,softy05@naver.com,choco119600@gmail.com,sonchaeyeon1234@naver.com,v_mins2@naver.com,ohdayoung01@naver.com,seojin0441@naver.com,yeonsue05@naver.com,ccuuss04@gmail.com,wave04300@naver.com,emdeo203917@gmail.com,irin5501@gmail.com,emart8282@naver.com,lencoa24@naver.com,77greenb@naver.com,mjh2600@naver.com,dldlfdyd1119@naver.com,1028msj@naver.com,aa01037999435@gmail.com,jsoyoung05@gmail.com,ebmhk@naver.com,zziczzic94@gmail.com,ham2992@naver.com,soyeon4e9@naver.com,singsing1209@naver.com,yejunchae9156@gmail.com,ukfydu6850@naver.com,wintersnow13579@naver.com,yewon050705@naver.com,cats1030905@gmail.com,psy050622@naver.com,pinkyena1565@naver.com,aureve2587@naver.com,happykuna@naver.com,sungil0238@gmail.com,forkhm05@naver.com,dongdong9830@gmail.com,erikarina8075@gmail.com,yjyun011@naver.com,smj050228@naver.com,loveyys96@naver.com,vhffns@naver.com,ywseo0510@gmail.com,jby0324@naver.com,lunajo1009@naver.com,dayeon932@naver.com,yerin060301@naver.com,chngh1507@naver.com,eriel7754@naver.com,ijisu020@naver.com,sarangbaek0315@naver.com,eungyo9159@hanmail.net,okuk1226@naver.com,hyebin0704@naver.com,alsrud4359@naver.com,s1930332@naver.com,sp382150@dwfl.hs,saebomyoon07@naver.com,gmldnjsdl1223@naver.com,khb060306@naver.com,frontks0509@naver.com,svtcarat0814@naver.com,a7397425@gmail.com,gayeonii0930@naver.com,kimmijin6911@gmail.com,skaco544@gmail.com,raini0221@naver.com,ldr4671@naver.com,crom3946@gmail.com,kimyoubin4953@gmail.com,lucy5305@naver.com,jcan2424@gmail.com,kim0928naye@icloud.com,sonsy1209@icloud.com,kyaamy@naver.com,dogyung234@naver.com,wjdtmddbs1023@naver.com,haseon0102@gmail.com,byeonmingdo@naver.com,ksh060705@naver.com,koomj06200@naver.com,hjo04@naver.com,kaylucyer@naver.com,hyungyu_lee@naver.com,junnysweb@naver.com,minsung05k@gmail.com,gwen061004@naver.com,wjswl716@naver.com,yejin-9100@naver.com,eunsungpari@gmail.com,loveluv1312@naver.com,chaeming1026@gmail.com,mintsh333@naver.com,lucy08270@naver.com,jiminkyung38@gmail.com,peacholivia@naver.com,eunchaeh2014@naver.com,free01222@naver.com,seohee0227@naver.com,lilly3987@naver.com,mynation3@naver.com,choihwanse71@naver.com,dlcodus521@naver.com,kmckmc1304@naver.com,whitejoomi@naver.com,dlys_019@naver.com,buup13@naver.com,tkdhs0821@naver.com,parkny570450@gmail.com,a34607211@gmail.com,luna2491@naver.com,mj060907@naver.com,tlswltn0524@naver.com,10dbswls@naver.com,heysaysuji@naver.com,jhplus07@naver.com,a01054529663@gmail.com,agavond04@gmail.com,angeldudu@hanmail.net,hyes0000@naver.com,qhruddl0702@naver.com,hyojin1239@naver.com,tony5240@naver.com,seoyoung119@naver.com,hyunwoo2113@naver.com,gwon3288@naver.com,olivia625@naver.com,eunseo4215@naver.com,gksrkdus03@naver.com,wnehdgus0426@naver.com,yoon_2008@naver.com,2005dltkddnjs@naver.com,rigyeong6292@naver.com,sy_3117@naver.com,07eunseo0302@naver.com,ukiteim@gmail.com,leeyubin0413@gmail.com,1004_suyeon@naver.com,hpply5420@naver.com,as050419@naver.com,jisu6712@naver.com,i_believe33@naver.com,gmltmd123444@gmail.com'

email_lists = email_string.split(',')

printed = ''

# 컴포넌트 정의
root.title('댓글 email 가져오기')

blog_address_label = Label(root, text='네이버 블로그 주소')
blog_address_entry = Entry(root)

id_label = Label(root, text='ID')
id_entry = Entry(root)

pwd_label = Label(root, text='PWD')
pwd_entry = Entry(root)

null_label1 = Label(root, text='-'*65)

from_email_label = Label(root, text='어떤 email부터 가져올까요?')
from_email_entry = Entry(root)
ok_button = Button(root, text='확인')

null_label2 = Label(root, text='\n')


def ok_button_click(string):
    global blog_address, ids, pwd, from_email
    blog_address = blog_address_entry.get()
    ids = id_entry.get()
    pwd = pwd_entry.get()
    from_email = from_email_entry.get()

    if blog_address and ids and pwd and from_email:
        results = main.Blog_Naver(blog_address,from_email,ids,pwd)
        if results:
            with open('result.txt', 'w') as f:
                for i in result_list:
                    f.write(i)
            showinfo('확인','원하시는 이메일들을 성공적으로 가져왔습니다.')

            with open('result.txt', 'r') as f:
                printed = f.read()

            frame = Frame(root)
            scrollbar = Scrollbar(frame)
            scrollbar.pack(side='right', fill='y')
            result_text = Text(frame, yscrollcommand=scrollbar.set)
            result_text.insert(1.0, printed)
            result_text.configure(state='disabled')
            result_text.pack(fill="both", expand=True)
            scrollbar.config(command=result_text.yview)
            frame.grid(row=6, column=0, columnspan=3, sticky='sn')


        else:
            showerror('Error','입력된 값 중 잘못된 값이 있습니다.\n다시 확인해주세요.')
            return 0

    else:
        showerror('Error','입력 창에 빈칸이 있습니다.\n입력창을 모두 채워주세요.')
        return 0



ok_button.bind('<Button-1>',ok_button_click)

# 배치
blog_address_label.grid(row=0, column=0, sticky='ew')
blog_address_entry.grid(row=0, column=1, sticky='ew')

id_label.grid(row=1, column=0, sticky='ew')
id_entry.grid(row=1, column=1, sticky='ew')

pwd_label.grid(row=2, column=0, sticky='ew')
pwd_entry.grid(row=2, column=1, sticky='ew')


null_label1.grid(row=3, column=0, columnspan=3, sticky='ew')
from_email_label.grid(row=4, column=0, sticky='ew')
from_email_entry.grid(row=4, column=1, sticky='ew')

ok_button.grid(row=0, column=2, rowspan=5, sticky='sn')
null_label2.grid(row=5, column=0, columnspan=3, sticky='ew')

root.mainloop()
