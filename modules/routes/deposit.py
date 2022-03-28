#보증금 요청 처리

from flask import request
from flask_restx import Resource, Namespace

deposit = Namespace('deposit')

@deposit.route('')
class deposit(Resource):
    def post(self):
        pass

@deposit.route('/<int:sortId>')
class SortArea(Resource):
    def post(self,sortId):
        pass

# @deposit.route('/depositQuick',methods=['POST'])
# def depositQuick():
#     pass

# @deposit.route('/depositMerge',methods=['POST'])
# def depositMerge():
#     pass

# @deposit.route('/depositInsert',methods=['POST'])
# def depositInsert():
#     pass