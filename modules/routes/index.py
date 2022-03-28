from flask import request
from flask_restx import Resource, Api, Namespace



index = Namespace('index')

@index.route('')
class index(Resource):
    def get(self):
        return render_template('index.html')