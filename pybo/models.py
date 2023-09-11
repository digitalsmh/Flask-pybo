# myproject/pybo/models.py

from pybo import db

# DB에 행당 Table 생성한다

# 질문 모델 클래스들을 정의
# Question & Answer 모델에 voter 속성을 추가

#  SQLAlchemy에서 Question 모델에 'ManyToMany' 관계를 적용
question_voter = db.Table( 'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id          = db.Column(db.Integer,     primary_key=True)
    subject     = db.Column(db.String(200), nullable=False) # 주제
    content     = db.Column(db.Text(),      nullable=False) # 콘텐츠
    create_date = db.Column(db.DateTime(),  nullable=False) # 날짜,.시간

    # 글쓴이 정보
    # user_id    = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user_id    = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user        = db.relationship('User', backref=db.backref('question_set'))

    modify_date = db.Column(db.DateTime(), nullable=True)
    # Question 모델에 voter 속성 추가하기
    voter       = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))              


# 답변 모델 클래스들을 정의
# SQLAlchemy에서 Answer 모델에 'ManyToMany' 관계를 적용
answer_voter = db.Table( 'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Answer(db.Model):
    id          = db.Column(db.Integer,         primary_key=True)
    question_id = db.Column(db.Integer,         db.ForeignKey('question.id', ondelete='CASCADE'))
    question    = db.relationship('Question',   backref=db.backref('answer_set')) # 역참조 설정
    content     = db.Column(db.Text(),          nullable=False)
    create_date = db.Column(db.DateTime(),      nullable=False)    

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

    # Answer 모델에 voter 속성 추가하기
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))    

# 회원등록 모델 클래스들을 정의
class User(db.Model):
    id          = db.Column(db.Integer,     primary_key=True)
    username    = db.Column(db.String(150), unique=True, nullable=False)
    password    = db.Column(db.String(200),              nullable=False)
    email       = db.Column(db.String(120), unique=True, nullable=False)
