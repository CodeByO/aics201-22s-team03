from flask import request
from flask_restx import Resource, Namespace

#[Function] 메인페이지
#[DESC] 클라이언트로 받은 요청 처리
#[TODO] 검증

index = Namespace('index')

@index.route('')
class index(Resource):
    def get(self):
        return render_template('index.html')