from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

def create_app():
    app = 

    from . import auth
    app.register_blueprint(auth.bp)

    return app
