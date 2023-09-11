# [파일명: projects/myproject/pybo/views/answer_views.py]

from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

# from pybo import db
from .. import db 
# from pybo.models import Question, Answer
from ..forms import AnswerForm     
from ..models import Question, Answer

from pybo.views.auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')

# 답변 등록시 글쓴이
@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):

    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    
    if form.validate_on_submit():
        # form 'content'의 얻기
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(),   user=g.user)

        question.answer_set.append(answer)
        db.session.commit()
        # return redirect(url_for('question.detail', question_id=question_id))
        # 앵커로 이동 라우팅(앵커 엘리먼트를 포함)
        return redirect('{}#answer_{}'.format(
            url_for('question.detail', question_id=question_id), answer.id))


    return render_template('question/question_detail.html', question=question, form=form)

# 답변 수정 라우팅  함수
@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            # 앵커로 이동 라우팅(앵커 엘리먼트를 포함)
            return redirect('{}#answer_{}'.format(
                url_for('question.detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)

# 답변 삭제 라우팅 함수
@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

#  답변 추천 라우팅 함수
@bp.route('/vote/<int:answer_id>/')
@login_required
def vote(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    if g.user == _answer.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    # return redirect(url_for('question.detail', question_id=_answer.question.id))
    # 앵커로 이동 라우팅(앵커 엘리먼트를 포함)
    # return redirect('{}#answer_{}'.format( url_for('question.detail', question_id=answer.question.id), answer.id))
    return redirect('{}#answer_{}'.format(  url_for('question.detail', question_id=_answer.question.id), _answer.id))