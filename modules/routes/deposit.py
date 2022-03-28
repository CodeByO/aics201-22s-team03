#보증금 요청 처리

from flask import flash
from flask_restx import Resource, Namespace

deposit = Namespace('deposit')

@deposit.route('')
class deposit(Resource):
    def post(self):
        pass

@deposit.route('/<int:sortId>')
class sortDeposit(Resource):
    def post(self,sortId):
        if sortId == 1:
            pass
        elif sortId == 2:
            pass
        elif sortId == 3:
            pass
        else:
            flash("해당 요청은 존재하지 않습니다.")

