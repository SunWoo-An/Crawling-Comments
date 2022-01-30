# Crawling-Comments




                                                             Crawling-Comments Info
                                              
                                              
                                              
                                   Crawling Comments in Naver Blog ( in terms of Root User for collecting mails ) 




블로그에서 무료 자료를 배포할 시에 댓글에서 이메일을 적는 경우가 많습니다.

이러한 상황에서 댓글 개수가 수동으로 받아오기에 힘들 경우, 이 Crawling-Comments 를 이용하여 추출해 낼 수 있습니다.


*보완점이자 참고사항

비밀댓글까지 크롤링하기위해 네이버에 로그인하는 과정이 필요했고, 아이디와 패스워드는 selenium으로 연 네이버 로그인창에서 '직접' 입력해야합니다.
네이버 로그인 봇 감지 로직에 감지되기 때문에 그렇습니다.

또한 이메일 뒷주소를 잘못 쓴 경우도 꽤 있었는데, 예를 들면 naver.com을 never.com, naver.comps, nvear.com 등으로 댓글을 단 경우가 있었습니다. 
이같은 경우는 수작업으로 수정해야할 수 밖에 없지만, 기회가 된다면 딥러닝의 자연어처리를 공부해 위와 같이 잘못된 이메일 뒷주소도 바르게 정정해주는 모델도 구현해보겠습니다.

