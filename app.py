from flask import Flask

from modules.routes import index
from modules.routes import sort
from modules.routes import search
from modules.routes import suggest


app = Flask(__name__)

app.register_blueprint(index.blueprint)

app.register_blueprint(sort.blueprint)

app.register_blueprint(search.blueprint)

app.register_blueprint(suggest.blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)