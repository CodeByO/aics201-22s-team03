from flask import flash, Blueprint, render_template

#[Function] 보증금 요청
#[DESC] 클라이언트로 받은 보증금 정렬 요청 처리
#[TODO] 현재까지 기능 테스트 및 팀원이 작성한 기능 추가

blueprint = Blueprint("deposit", __name__, url_prefix='/deposit')


@blueprint.route('/<int:sortId>')

def deposit(sortId):
    if sortId == 1:
        pass
    elif sortId == 2:
        pass
    elif sortId == 3:
        pass
    else:
        flash("해당 요청은 존재하지 않습니다.")
    return render_template('sort.html')
