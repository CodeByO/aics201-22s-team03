#계약 면적 요청 처리 

from flask import request
from flask_restx import Resource, Namespace

area = Namespace('area')

@area.route('')
class area(Resource):
    def post(self):
        pass
@area.route('/<int:sortId>')
class SortArea(Resource):
    def post(self,sortId):
        pass
# @area.route('/areaQuick',methods=['POST'])
# def monthlyQuick():
#     pass

# @area.route('/areaMerge',methods=['POST'])
# def areaMerge():
#     pass

# @area.route('/areaInsert',methods=['POST'])
# def areaInsert():
#     pass