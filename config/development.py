# [파일명: projects/myproject/config/development.py]

from config.default import *
from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, '.env.dev'))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"