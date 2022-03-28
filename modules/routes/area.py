#계약 면적 요청 처리 

from flask import flash
from flask_restx import Resource, Namespace

area = Namespace('area')

@area.route('')
class area(Resource):
    def post(self):
        pass
@area.route('/<int:sortId>')
class sortArea(Resource):
    def post(self,sortId):
        if sortId == 1:
            pass
        elif sortId == 2:
            pass
        elif sortId == 3:
            pass
        else:
            flash("해당 요청은 존재하지 않습니다.")
