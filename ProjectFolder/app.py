from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_cors import CORS, cross_origin
from Handlers.parts_handler import parts_handler
from Handlers.racks_handler import racks_handler
from Handlers.users_handler import user_handler
from Handlers.warehouses_handler import warehouse_handler
from Handlers.suppliers_handler import supplier_handler
from Handlers.transactions_handler import transaction_handler
from Handlers.inventory_incoming_transactions_handler import inventory_incoming_transaction_handler
from Handlers.inventory_outgoing_transactions_handler import inventory_outgoing_transaction_handler
from Handlers.inventory_transfer_transaction_handler import inventory_transfer_transaction_handler
from Handlers.outgoing_transaction_reciever_handler import outgoing_transaction_receiver_handler


app = Flask(__name__)
# Apply CORS to this app
CORS(app)


app.register_blueprint(parts_handler, url_prefix='/jemsa/parts')
app.register_blueprint(racks_handler, url_prefix='/jemsa/racks')
app.register_blueprint(user_handler, url_prefix='/jemsa/users')
app.register_blueprint(warehouse_handler, url_prefix='/jemsa/warehouses')
app.register_blueprint(supplier_handler, url_prefix='/jemsa/suppliers')
app.register_blueprint(transaction_handler, url_prefix='/jemsa/transactions')
app.register_blueprint(inventory_incoming_transaction_handler, url_prefix='/jemsa/incoming_transactions')
app.register_blueprint(inventory_outgoing_transaction_handler, url_prefix='/jemsa/outgoing_transactions')
app.register_blueprint(inventory_transfer_transaction_handler, url_prefix='/jemsa/transfer_transactions')
app.register_blueprint(outgoing_transaction_receiver_handler, url_prefix='/jemsa/receivers')



if __name__ == '__main__':
    app.run(debug=True)