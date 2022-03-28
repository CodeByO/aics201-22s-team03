import os
import requests
import sys


from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api

from modules.routes import *
from modules.api import *


app = Flask(__name__)
api = Api(app)

api.add_namespace(index,'/')

api.add_namespace(area,'/area')

api.add_namespace(deposit,'/deposit')

api.add_namespace(monthly,'/monthly')

api.add_namespace(searchRoom,'/searchRoom')

api.add_namespace(suggestRoom,'/suggestRoom')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)