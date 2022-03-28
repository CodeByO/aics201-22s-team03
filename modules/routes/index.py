from flask import Blueprint, render_template

#[Function] 메인페이지
#[DESC] 클라이언트로 받은 요청 처리
#[TODO] 검증

blueprint = Blueprint("index", __name__, url_prefix='/')

@blueprint.route('/')
def index():
    return render_template('index.html')
            