from flask import Blueprint, render_template
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from api import getData
#[Function] 메인페이지
#[DESC] 클라이언트로 받은 요청 처리
#[TODO] 검증

blueprint = Blueprint("index", __name__, url_prefix='/')

data = getData.getData()



@blueprint.route('/')
def index():
    roomList = data.getApi('202203')
    return render_template('index.html',roomList=roomList)
            