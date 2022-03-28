#방 추천 요청 처리
from flask import request
from flask_restx import Resource, Namespace

suggestRoom = Namespace('suggestRoom')

@suggestRoom.route('')
class suggestRoom(Resource):
    def post(self):

    # if request.method == 'POST':
    #   id = request.form['id']
    # reutnr render_template('test.html',form=form)
        pass