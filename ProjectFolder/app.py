from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from Handlers.parts_handler import parts_handler
from Handlers.racks_handler import racks_handler


app = Flask(__name__)
# Apply CORS to this app
CORS(app)


app.register_blueprint(parts_handler, url_prefix='/jemsa/parts')
app.register_blueprint(racks_handler, url_prefix='/jemsa/racks')


if __name__ == '__main__':
    app.run(debug=True)