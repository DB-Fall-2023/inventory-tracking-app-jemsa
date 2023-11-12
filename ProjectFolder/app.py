from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_cors import CORS, cross_origin
from Handlers.parts_handler import parts_handler
from Handlers.racks_handler import racks_handler
from Handlers.users_handler import user_handler
from Handlers.warehouses_handler import warehouse_handler
from Handlers.suppliers_handler import supplier_handler


app = Flask(__name__)
# Apply CORS to this app
CORS(app)


app.register_blueprint(parts_handler, url_prefix='/jemsa/parts')
app.register_blueprint(racks_handler, url_prefix='/jemsa/racks')
app.register_blueprint(user_handler, url_prefix='/jemsa/users')
app.register_blueprint(warehouse_handler, url_prefix='/jemsa/warehouses')
app.register_blueprint(supplier_handler, url_prefix='/jemsa/suppliers')


if __name__ == '__main__':
    app.run(debug=True)