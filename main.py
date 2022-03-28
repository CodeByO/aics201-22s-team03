from crypt import methods
import os
import requests
import sys


from dotenv import load_dotenv
from flask import *
from flask_restx import Resource, Api

from modules.routes import index

load_dotenv(verbose=True)

api_key = os.getenv('API_KEY')
url = os.getenv('API_URL')

params = {'serviceKey': api_key, 'LAWD_CD' : '11110','DEAL_YMD':'2021312'}

response = requests.get(url,params=params)


app = Flask(__name__)
api = Api(app)

api.add_namespace(index,'/')



@app.route('/suggestRoom',methods=['POST'])
def suggestRoom():
    # if request.method == 'POST':
    #   id = request.form['id']
    # reutnr render_template('test.html',form=form)
    pass

@app.route('/searchRoom',methods=['POST'])
def suggestRoom():
    pass

@app.route('/depositQuick',methods=['POST'])
def depositQuick():
    pass

@app.route('/depositMerge',methods=['POST'])
def depositMerge():
    pass

@app.route('/depositInsert',methods=['POST'])
def depositInsert():
    pass

@app.route('/monthlyQuick',methods=['POST'])
def monthlyQuick():
    pass

@app.route('/monthlyMerge',methods=['POST'])
def monthlyMerge():
    pass

@app.route('/monthlyInsert',methods=['POST'])
def monthlyInsert():
    pass

@app.route('/areaQuick',methods=['POST'])
def monthlyQuick():
    pass

@app.route('/areaMerge',methods=['POST'])
def areaMerge():
    pass

@app.route('/areaInsert',methods=['POST'])
def areaInsert():
    pass


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)