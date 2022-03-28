from flask import flash
from flask_restx import Resource, Namespace

#[Function] 월세 요청
#[DESC] 클라이언트로 받은 월세 정렬 요청 처리
#[TODO] 현재까지 기능 테스트 및 팀원이 작성한 기능 추가


monthly = Namespace('monthly')

@monthly.route('')
class monthly(Resource):
    def post(self):
        pass

@monthly.route('/<int:sortId>')
class sortMonthly(Resource):
    def post(self,sortId):
        if sortId == 1:
            pass
        elif sortId == 2:
            pass
        elif sortId == 3:
            pass
        else:
            flash("해당 요청은 존재하지 않습니다.")


