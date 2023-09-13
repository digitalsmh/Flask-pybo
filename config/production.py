# [파일명: projects/myproject/config/production.py]
from logging.config import dictConfig
from config.default import *

from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env.pro'))

# Database to ORM(Object-Relational Mapping)

# 1. SQLite 연동
#  SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))//

# 2. PostgreSQL MySQL연동
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#     user=os.getenv('DB_USER'),
#     pw=os.getenv('DB_PASSWORD'),
#     url=os.getenv('DB_HOST'),
#     db=os.getenv('DB_NAME'))

# 3 .MySQL 연동
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/testdb"


SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'VJ!sA3\xfe\xf5\xc1\xb5\xfec\xc0Y\xd4\x19'

# logging : 파이썬의 기본 logging 모듈
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})