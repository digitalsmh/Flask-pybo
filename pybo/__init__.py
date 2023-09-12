# myproject/pybo/__init__py

from flask import Flask
from flask_migrate import Migrate # ORM 적용을 위한 라이즈러리
from flask_sqlalchemy import SQLAlchemy # ORM(object relational mapping)
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}



# ORM(object relational mapping)사용하기 위해 전역 변수 db, migrate 객체 생성.

# db = SQLAlchemy()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # Confugration. 
    app.config.from_object(config)

    # ORM(object relational mapping)
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db) # 전역 변수 등록
    
    from . import models        # 모델 임포트

    # 블루프린트 등록.
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)       # views/main_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(question_views.bp)   # views/question_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(answer_views.bp)     # views/answer_views.py 파일에 생성한 블루프린트 객체 bp를 등록.
    app.register_blueprint(auth_views.bp)       # views/answer_views.py 파일에 생성한 회원 가입용 블루프린트

    # 필터 등록.
    from filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime # 'datetime' 이라는 이름으로 필터를 등록해 주었다.

    # markdown
    #   nl2br: 줄바꿈 문자를 <br>로 바꿔 준다
    #   fenced_code :코드 표시 기능
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    return app
