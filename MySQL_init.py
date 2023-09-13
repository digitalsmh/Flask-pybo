# 
# https://parkjju.github.io/vue-TIL/python/2021-03-08-sqlAlchemy.html

# [라이브러리 설치]  

# pip install sqlalchemy
# pip install flask-migrate   #  ORM 라이브러리   
# pip install flask-wtf   
# pip install email_validator   
# pip install flask-markdown  #  Markdown 라이브러리    
# pip install python-dotenv
# pip install pymysql         #  MySQL 데이터베이스 커넥터 라이브러리  

import pymysql

# mysql db 와의 호환을 위해 아래 함수 호출
pymysql.install_as_MySQLdb()
 
# [create_engine import]
# SQLAlchemy가 DB에 접근하려면, DB 접속 정보를 알아야함.
# 이러한 접속 정보를 받아서 연결을 관리하는 객체가 Engine
# 파이썬을 통한 mysql 접근을 하기 위해 진행하는 데이터베이스 설정은 다음과 같다.

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://" + db_id + ":" + db_passwd + "@"
                                        + db_ip + ":" + db_port + "/" + db_name, encoding='utf-8')

mysql+pymysql://&lt;username>:&lt;password>@&lt;host>/&lt;dbname>[?&lt;options>]
 

collector.py 파일 실행 시 데이터 베이스의 연결 정보를 저장할 내용 만들기 name="main"기반
db = {
    db_name = 'database_name'
    db_id = 'mysql id'
    db_ip = 'localhost' # 자신의 로컬컴퓨터
    db_password = 'mysql password'
    db_port = '3306'
}


 result = engine.execute("select * from test1.class1;").fetchall()
  