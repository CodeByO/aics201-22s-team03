from flask import Blueprint, render_template

#[Function] 검색 요청
#[DESC] 클라이언트로 받은 검색 요청 처리
#[TODO] 기능 작성

blueprint = Blueprint("search", __name__, url_prefix='/search')


@blueprint.route('/')
def search():
        return render_template('search.html')
    