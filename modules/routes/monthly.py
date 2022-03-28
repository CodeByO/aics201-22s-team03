from flask import flash, Blueprint, render_template

#[Function] 월세 요청
#[DESC] 클라이언트로 받은 월세 정렬 요청 처리
#[TODO] 현재까지 기능 테스트 및 팀원이 작성한 기능 추가


blueprint = Blueprint("monthly", __name__, url_prefix='/monthly')


@blueprint.route('/<int:sortId>')
def monthly(sortId):
    print(sortId)
    if sortId == 1:
        pass
    elif sortId == 2:
        pass
    elif sortId == 3:
        pass
    else:
        return render_template('index.html')


