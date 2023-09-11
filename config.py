# myproject/config.py

import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI: 데이터베이스 접속 주소. 
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLALCHEMY_TRACK_MODIFICATIONS : SQLAlchemy의 이벤트를 처리하는 옵션.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-wtf: CSRF(cross-site request forgery)라는 웹 사이트 취약점 공격 방지
SECRET_KEY = "dev_smh_20230907"