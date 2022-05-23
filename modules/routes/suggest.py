from flask import Blueprint, render_template
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from package import suggest

#[Function] 추천 요청
#[DESC] 클라이언트로 받은 추천 요청 처리
#[TODO] 기능 작성


blueprint = Blueprint("suggest", __name__, url_prefix='/suggest')
sug = suggest.suggest()
@blueprint.route('/')
def index():
        return render_template('suggest.html')

@blueprint.route('/charter')
def suggestCharter():
        page = "charter"
        charterList,charterTime = sug.suggestCharter()
        return render_template('suggest.html',roomList=charterList,time=charterTime, page = page)

@blueprint.route('/monthly')
def suggestMonthly():
        page = "monthly"
        monthlyList,charterList,monthlyTime = sug.suggestMonthly()
        roomList = []
        roomList.append(monthlyList)
        roomList.append(charterList)
        return render_template('suggest.html',monthlyList=roomList,time=monthlyTime, page=page)