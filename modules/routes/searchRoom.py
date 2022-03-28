

from flask import request
from flask_restx import Resource, Namespace

#[Function] 검색 요청
#[DESC] 클라이언트로 받은 검색 요청 처리
#[TODO] 기능 작성

searchRoom = Namespace('searchRoom')

@searchRoom.route('')
class searchRoom(Resource):
    def post(self):
        pass