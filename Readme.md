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
<br>
<br>

# 서버 구축 절차

## 1. 가상환경 구성

sudo apt install python3-venv

mkdir projects
mkdir venvs

cd venvs
python3 -m venv myproject
cd myproject
cd bin
. activate
(myproject) smh@smh-VM62:~/venvs/myproject/bin$

- /home/ubuntu/venvs/myproject/bin 디렉터리로 이동한 다음 . activate 명령을 수행하면 가상 환경으로 진입할 수 있다.
- 만약 가상 환경에서 벗어나려면 아무 곳에서나 deactivate 명령을 수행하면 된다.

## 2. wheel 패키지 설치하기(가상환경에서)

(myproject) smh@smh-VM62:~/venvs/myproject/bin$ 

pip install wheel
pip install flask
pip install flask-migrate
pip install flask-wtf
pip install email_validator
pip install flask-markdown


## 3. 파이보 설치하기 : 깃허브 원격 저장소에서 서버로 내려 받기

cd ~/projects

projects$ git clone https://github.com/digitalsmh/Flask-pybo.git myproject

## 4. 파이보 실행하기

export FLASK_APP=pybo
export FLASK_DEBUG=true
export APP_CONFIG_FILE=/home/smh/projects/myproject/config/production.py

## 5. 데이터베이스 초기화
cd myproject
myproject$ flask db init
myproject$ flask db migrate
myproject$ flask db upgrade

## 6. 플라스크 서버 실행하기

 myproject$ flask run --host=0.0.0.0