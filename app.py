# default example for flask

from flask_cors import CORS
from services import create_app

# CORS(app)
app = create_app()
CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
