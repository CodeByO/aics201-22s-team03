from flask import Blueprint, render_template
import sys,os
from package import sort
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#[Function] 추천 요청
#[DESC] 클라이언트로 받은 추천 요청 처리
#[TODO] 기능 작성



blueprint = Blueprint("sort", __name__, url_prefix='/sort')

@blueprint.route('/')
def index():
        return render_template('sort.html')

@blueprint.route('/area/<int:sortId>')
def area(sortId):
    page = "area"
    s = sort.sort()
    sorted, time = s.area(sortId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)


@blueprint.route('/charter/<int:sortId>')
def charter(sortId):
    page = "charter"
    if sortId == 1:
        pass
    elif sortId == 2:
        pass
    elif sortId == 3:
        pass
    else:
        pass
    return render_template('sort.html')

@blueprint.route('/monthly/<int:sortId>')
def monthly(sortId):
    page = "monthly"
    if sortId == 1:
        pass
    elif sortId == 2:
        pass
    elif sortId == 3:
        pass
    else:
        pass
    return render_template('sort.html')