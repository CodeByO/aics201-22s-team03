from flask import flash, Blueprint, render_template

#[Function] 추천 요청
#[DESC] 클라이언트로 받은 추천 요청 처리
#[TODO] 기능 작성


blueprint = Blueprint("suggestRoom", __name__, url_prefix='/suggestRoom')

@blueprint.route('/')
def suggestRoom():
        print("test")