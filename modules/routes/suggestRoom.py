from flask import request
from flask_restx import Resource, Namespace

#[Function] 추천 요청
#[DESC] 클라이언트로 받은 추천 요청 처리
#[TODO] 기능 작성


suggestRoom = Namespace('suggestRoom')

@suggestRoom.route('')
class suggestRoom(Resource):
    def post(self):

    # if request.method == 'POST':
    #   id = request.form['id']
    # reutnr render_template('test.html',form=form)
        pass