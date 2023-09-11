# [Flask 환경 변수](https://coding-groot.tistory.com/138)

set FLASK_APP=pybo    # 'pybo'    

set FLASK_DEBUG=true

flask run

# 라이브러리 설치  
pip install flask-migrate #  ORM 라이브러리   
pip install flask-wtf   
pip install email_validator   
pip install flask-markdown   

# DB 관련

del pybo.db      # 데이터베이스 파일 삭제    
flask db init    # 데이터베이스 초기화   
flask db migrate # 리비전 파일 생성    
flask db upgrade # 가장 최근 버전(리비전 파일 실행) DB upgrade   
flask db downgrade # 이전 버전으로 DB downgrade   

- [X] DB 리비전 : flask db migrate 
- [X] DB 업그레이드  flask db upgrade 
- [X] DB 최종 리비젼 확인: flask db heads 
- [X] DB 현재 시점의 리비전 : flask db current 

- 현재 리비전을 최종 리비전으로 변경하기 : flask db stamp heads
