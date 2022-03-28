import os
import requests
import sys


from dotenv import load_dotenv
from flask import Flask

from modules.routes import index
from modules.routes import area
from modules.routes import deposit
from modules.routes import monthly
from modules.routes import searchRoom
from modules.routes import suggestRoom


app = Flask(__name__)

app.register_blueprint(index.blueprint)

app.register_blueprint(area.blueprint)

app.register_blueprint(deposit.blueprint)

app.register_blueprint(monthly.blueprint)

app.register_blueprint(searchRoom.blueprint)

app.register_blueprint(suggestRoom.blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)