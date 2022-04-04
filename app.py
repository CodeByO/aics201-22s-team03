from flask import Flask

from modules.routes import index
from modules.routes import area
from modules.routes import deposit
from modules.routes import monthly
from modules.routes import search
from modules.routes import suggest


app = Flask(__name__)

app.register_blueprint(index.blueprint)

app.register_blueprint(area.blueprint)

app.register_blueprint(deposit.blueprint)

app.register_blueprint(monthly.blueprint)

app.register_blueprint(search.blueprint)

app.register_blueprint(suggest.blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)