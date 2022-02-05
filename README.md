# Crawling-Comments




                                                             Crawling-Comments Info
                                              
                                              
                                              
                                   Crawling Comments in Naver Blog ( in terms of Root User for collecting mails ) 




블로그에서 무료 자료를 배포할 시에 댓글에서 이메일을 적는 경우가 많습니다.

이러한 상황에서 댓글 개수가 수동으로 받아오기에 힘들 경우, 이 Crawling-Comments 를 이용하여 추출해 낼 수 있습니다.


                                                                   Caution Points
                                                                  
                                                     이 프로그램은 Chrome 브라우저를 이용한 Crawler 입니다.
                                                     
                                     혹여나 Chrome 사이트가 없으신 분들은 Chrome 을 다운받아주셔야 프로그램이 실행이 됩니다.



* 사용법 instructions

1) Chrome 상단 오른편에 있는 Menu아이콘( three points . . .)을 클릭해주고, 도움말(Help) 에 들어가신 뒤 Chrome 정보( Chrome info )를 클릭하여 버전을 확인합니다. 

2) Chromedriver 메인 주소 : https://chromedriver.chromium.org/downloads 홈페이지에 들어가서 자신의 크롬 버젼에 맞는 chromedriver를 다운해줍니다. 이때 자신의 크롬이 93버젼일 경우, 93버젼 chromedriver들 중 제일 최신의 드라이버를 다운받아 주셔야합니다.

3) Window 의 경우 window_32.zip 을 MacOS의 경우 MAC 버젼으로 다운받아야합니다. ( 저희가 작성한 프로그램은 Window 버젼을 중심으로 돌아가는 프로그램입니다. 혹여나 예외가 생길 수 있으므로 이에 대해서 추후 개발해나갈 예정입니다. ) 

4) 압축을 푼 뒤, Window 파일 탐색기에서 chrome 드라이버가 있는 위치를 복사합니다... ( 파일 모양 옆 "내 PC > 다운로드 > chromedriver_win32" 이 부분을 클릭하시면 원하는 위치가 나옵니다.

5) 이를 프로그램 내의 Blog_url 이 아닌 chromedriver_url 에 넣어줍니다!!!!

6) 자신이 이 프로그램을 처음 사용할 경우 : 어떤 Email 부터 가져올까요? 질문에서 0 을 누르시고 "확인"버튼을 눌러주시길 바라겠습니다.

7) 자신이 이 프로그램을 N번째 사용할 경우 : 어떤 Email 부터 가져올까요? 질문에서 이전 txt 파일에서 맨 끝에 있는 Email 한개를 넣어주시면 그 이메일을 포함하지 않고,
이전에 받지 않았던 새로운 메일들을 받아 올 수 있습니다. -> 추후에 더 발전할 예정.




*보완점이자 참고사항
1) 딥러닝의 자연어처리를 통해 메일주소가 잘못된 경우를 Collecting 하는 모델을 구현해보고싶음.
2) 프로그램의 효율성을 신경쓰지 않은 채 코드를 짜 코드의 효율성이 떨어짐. -> 이를 보완하고자 수정할 예정이다.
