#  [파일명: projects/myproject/pybo/views/auth_views.py]

# 회원가입, 로그인, 로그아웃 구현

import functools

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.models import User
from pybo.forms import UserCreateForm, UserLoginForm


bp = Blueprint('auth', __name__, url_prefix='/auth')

# 회원 등록 수행
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit(): # POST : 계정을 저장
        user = User.query.filter_by(username=form.username.data).first()  # "이미 등록된 사용자"인지 확인
        if not user:  # 신규 등록
            user = User(username = form.username.data,
                        password = generate_password_hash(form.password1.data), # 암호화
                        email    = form.email.data)

            db.session.add(user) # db 처리.
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            # flash(), 논리 오류를 발생 함수
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form) #  GET : 계정 등록 화면을 출력

# 로그인 수행
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit(): # POST 요청은 로그인을 수행
        error = None

        # 데이터베이스에 해당 사용자가 있는지를 검사.
        user = User.query.filter_by(username=form.username.data).first()
        
        if not user:
            error = "존재하지 않는 사용자입니다."

        elif not check_password_hash(user.password, form.password.data): # 암호화된 비밀번호 확인
            error = "비밀번호가 올바르지 않습니다."

        if error is None:                # 세션(session)에 사용자 정보를 저장
            session.clear()
            session['user_id'] = user.id
            # 수정
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)  # 로그인시 next 파라미터 값이 있으면 읽어서 로그인 후 해당 페이지 이동
            else:
                return redirect (url_for('main.index') ) # 없으면 메인 페이지로 이동
            # 수정 끝            

        flash(error)

    return render_template('auth/login.html', form=form)    # GET 요청에는 로그인 화면

# 로그인한 사용자 정보 조회/검증 수행
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)    

# 로그아웃 수행
@bp.route('/logout/')
def logout():
    session.clear() # 세션의 모든 값을 삭제
    return redirect(url_for('main.index'))

# 데코레이터 함수: login_required()
def login_required(view):
    @functools.wraps(view) # 데코레이터
    def wrapped_view(*args, **kwargs):
        if g.user is None: # g.user가 있는지를 조사하여 없으면 로그인 URL로 리다이렉트
            _next = request.url if request.method == 'GET' else ''
            return redirect(url_for('auth.login', next=_next))
        return view(*args, **kwargs)
    return wrapped_view