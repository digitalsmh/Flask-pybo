# myproject/pybo/__init__py

from flask import Flask

from flask_migrate import Migrate # ORM 적용을 위한 라이즈러리
from flask_sqlalchemy import SQLAlchemy # ORM(object relational mapping)
from sqlalchemy import MetaData

import config
# SQLite 사용을 위해...
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


# ORM(object relational mapping)사용하기 위해 전역 변수 db, migrate 객체 생성.
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Confugration. 
    app.config.from_object(config)

    # ORM(object relational mapping)
    db.init_app(app) # 전역 변수 등록

    migrate.init_app(app, db)  # 기존. 전역 변수 등록    
    # if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    #     migrate.init_app(app, db, render_as_batch=True)  # 전역 변수 등록
    # else:
    #     migrate.init_app(app, db)  # 기존. 전역 변수 등록
    
    from . import models        # 모델(db table) 임포트

    # 블루프린트 등록.
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)       # views/main_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(question_views.bp)   # views/question_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(answer_views.bp)     # views/answer_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(auth_views.bp)       # views/answer_views.py 파일에 생성한 회원 가입용 블루프린트

    # 필터 등록.
    from filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime # 'datetime' 이라는 이름으로 필터를 등록해 주었다.

    return app

'''
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app
''' 

''' finel backup
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app
'''    