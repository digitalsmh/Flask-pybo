# [파일명: projects/myproject/pybo/forms.py]
#  pip install email_validator

# 템플릿에서 사용할 때 자동변환 된다: 
# 예)
#  PasswordField -> <input type="password">
#  EmailField    -> <input type="email">

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# 질문 등록시 사용할 프라스크 폼(Form) 정의
class QuestionForm(FlaskForm): # FlaskForm 클래스를 상속하여 만듬.
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

# 답변 등록시 사용할 프라스크 폼(Form) 정의
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

# 회원 등록시 사용할 프라스크 폼(Form) 정의
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

# 로그인 프라스크 폼(Form) 정의
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])    