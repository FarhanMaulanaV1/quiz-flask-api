from flask import *

app = Flask(__name__)

@app.route("/api/kolam", methods=["GET"])
def kolam():
    return jsonify({"kolam": "kolam"})

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    data["nama"] = "success"
    data["ikan"] = "success"
    print(data)
    return jsonify(data)

@app.route("/api/aktifasi", methods=["POST"])
def aktifasi():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route("/api/detailKolam", methods=["POST"])
def detailKolam():
    data = request.get_json()
    print(data)
    return jsonify(data)