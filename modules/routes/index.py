from flask import Blueprint, render_template
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from roominpy import getData
#[Function] 메인페이지
#[DESC] 클라이언트로 받은 요청 처리
#[TODO] 검증

blueprint = Blueprint("index", __name__, url_prefix='/')

data = getData.getData()

date = ['202112','202201','202202','202203','202204','202205']
locate = ['36110','11110']

@blueprint.route('/')
def index():
    roomList = data.roomList(date,locate)
    return render_template('index.html',roomList=roomList)
            