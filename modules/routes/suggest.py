from flask import Blueprint, render_template
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from api import suggest

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
        
        charterList,charterTime = sug.suggestCharter()
        return render_template('suggest.html',roomList=charterList,time=charterTime)

@blueprint.route('/monthly')
def suggestMonthly():

        monthlyList,charterList,monthlyTime = sug.suggestMonthly()
        return render_template('suggest.html',monthlyList=monthlyList,charterList=charterList,time=monthlyTime)