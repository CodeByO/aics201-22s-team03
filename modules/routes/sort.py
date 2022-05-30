from flask import Blueprint, render_template
import sys,os
from package import sort
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#[Function] 추천 요청
#[DESC] 클라이언트로 받은 추천 요청 처리
#[TODO] 기능 작성



date = ['202112','202201','202202','202203','202204','202205']
locate = ['36110','11110']
s = sort.sort(date,locate)
blueprint = Blueprint("sort", __name__, url_prefix='/sort')

@blueprint.route('/')
def index():
        return render_template('sort.html')

@blueprint.route('/area/<int:sortId>')
def area(sortId):
    page = "area"
    
    sorted, time = s.area(sortId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)


@blueprint.route('/charter/<int:sortId>')
def charter(sortId):
    page = "charter"
    sorted, time = s.charter(sortId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)

@blueprint.route('/monthly/<int:sortId>')
def monthly(sortId):
    page = "monthly"
    sorted, time = s.monthly(sortId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)