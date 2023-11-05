from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

#apply CORS
CORS(app)

#Work on Racks and Parts
@app.route("/")
def base():
    return "Testing this"


if (__name__ == "__main__"):
    app.run()