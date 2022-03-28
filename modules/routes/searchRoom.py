#방검색 요청 처리

from flask import request
from flask_restx import Resource, Namespace

searchRoom = Namespace('searchRoom')

@searchRoom.route('')
class searchRoom(Resource):
    def post(self):
        pass