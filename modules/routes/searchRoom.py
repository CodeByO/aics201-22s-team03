

from flask import flash, Blueprint, render_template

#[Function] 검색 요청
#[DESC] 클라이언트로 받은 검색 요청 처리
#[TODO] 기능 작성

blueprint = Blueprint("searchRoom", __name__, url_prefix='/api/searchRoom')


@blueprint.route('/')
def searchRoom():
        return render_template('index.html')
    