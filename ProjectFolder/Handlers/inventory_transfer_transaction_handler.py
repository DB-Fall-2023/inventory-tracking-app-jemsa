from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.connectHeroku import conn

inventory_transfer_transaction_handler = Blueprint('inventory_transfer_transaction_handler', __name__)


@inventory_transfer_transaction_handler.route('/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    part_id = data.get('PartID')
    sourcewarehouse_id = data.get('SourceWarehouseID')
    receivingwarehouse_id = data.get('ReceivingWarehouseID')

    dao_factory = DAOFactory(conn)
    transaction_dao = dao_factory.get_inventory_transfer_transactions_dao()

    try:
        transaction = transaction_dao.create_transactions(part_id, part_id, sourcewarehouse_id, receivingwarehouse_id)
        response = {
            'message': 'Transaction created successfully',
            'Transfer TransactionID': transaction[0]
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@inventory_transfer_transaction_handler.route('/', methods=['GET'])
def get_transactions():
    dao_factory = DAOFactory(conn)
    transactions_dao = dao_factory.get_inventory_transfer_transactions_dao()

    transactions = transactions_dao.get_transactions()

    try:
        response = []
        for transaction in transactions:
            transaction_data = {
                'transaction_id': transaction[0],
                'part_id': transaction[1],
                'source_warehouse_id': transaction[2],
                'receiving_warehouse_id': transaction[3],
            }
            response.append(transaction_data)

        return jsonify(response)

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@inventory_transfer_transaction_handler.route('/<int:transaction_id>', methods=['GET'])
def get_transactions_by_id(transaction_id):
    dao_factory = DAOFactory(conn)
    transactions_dao = dao_factory.get_inventory_transfer_transactions_dao()

    try:
        transaction = transactions_dao.get_transactions_by_id(transaction_id)
        if transaction:
            response = {
                'transaction_id': transaction[0],
                'part_id': transaction[1],
                'source_warehouse_id': transaction[2],
                'receiving_warehouse_id': transaction[3],
            }

            return jsonify(response)
        else:
            return jsonify(error='Transaction not found'), 404

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@inventory_transfer_transaction_handler.route('/<int:transaction_id>', methods=['PUT'])
def update_transactions(transaction_id):
    data = request.get_json()
    part_id = data.get('PartID')
    sourcewarehouse_id = data.get('SourceWarehouseID')
    receivingwarehouse_id = data.get('ReceivingWarehouseID')


    dao_factory = DAOFactory(conn)
    transactions_dao = dao_factory.get_inventory_transfer_transactions_dao()

    try:
        transactions_dao.update_transactions_by_id(transaction_id, part_id, sourcewarehouse_id, receivingwarehouse_id)
        transaction = transactions_dao.get_transactions_by_id(transaction_id)
        if transaction and (
                transaction[1] == part_id and
                transaction[2] == sourcewarehouse_id and
                transaction[3] == receivingwarehouse_id
        ):
            return jsonify(message=f'Transaction {transaction_id} updated successfully')

        else:
            return jsonify(error='Transaction not found'), 404

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500
