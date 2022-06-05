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

@blueprint.route('/area/<int:sortId>/<int:listId>')
def area(sortId,listId):
    page = "area"
    
    sorted, time = s.area(sortId,listId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)


@blueprint.route('/charter/<int:sortId>/<int:listId>')
def charter(sortId,listId):
    page = "charter"
    sorted, time = s.charter(sortId,listId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)

@blueprint.route('/monthly/<int:sortId>/<int:listId>')
def monthly(sortId,listId):
    page = "monthly"
    sorted, time = s.monthly(sortId,listId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)

@blueprint.route('/construction/<int:sortId>/<int:listId>')
def construction(sortId,listId):
    page = "construction"
    sorted, time = s.construction(sortId,listId)
    return render_template('sort.html',roomList=sorted, time=time ,page=page)