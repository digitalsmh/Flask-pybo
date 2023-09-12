# [파일명: projects/myproject/config/production.py]

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'VJ!sA3\xfe\xf5\xc1\xb5\xfec\xc0Y\xd4\x19'