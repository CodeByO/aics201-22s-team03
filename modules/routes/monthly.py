#월세 요청 처리

from flask import request
from flask_restx import Resource, Namespace

monthly = Namespace('monthly')

@monthly.route('')
class monthly(Resource):
    def post(self):
        pass

@monthly.route('/<int:sortId>')
class SortArea(Resource):
    def post(self,sortId):
        pass


# @monthly.route('/monthlyQuick',methods=['POST'])
# def monthlyQuick():
#     pass

# @monthly.route('/monthlyMerge',methods=['POST'])
# def monthlyMerge():
#     pass

# @monthly.route('/monthlyInsert',methods=['POST'])
# def monthlyInsert():
#     pass