from DAO.dao import BaseDAO


class Inventory_Outgoing_TransactionsDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_transactions(self, part_id, rack_id, receiver_id, warehouse_id):
        query = 'INSERT INTO "Inventory_Outgoing_Transactions" ("PartID", "RackID", "ReceiverID", "WarehouseID") VALUES (%s, %s, %s, %s) RETURNING "TransactionID";'
        cur = self.execute_query(query, (part_id, rack_id, receiver_id, warehouse_id,))
        self.commit()
        return cur.fetchone()

    def get_transactions(self):
        query = 'SELECT * FROM "Inventory_Outgoing_Transactions";'
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_transactions_by_id(self, transaction_id):
        query = 'SELECT * FROM "Inventory_Outgoing_Transactions" WHERE "TransactionID" = %s;'
        cur = self.execute_query(query, (transaction_id,))
        return cur.fetchone()

    def update_transactions_by_id(self, transaction_id, part_id, rack_id, reciever_id, warehouse_id):
        query = 'UPDATE "Inventory_Outgoing_Transactions" Set "PartID" = %s, "RackID" = %s, "RecieverID" = %s, "WarehouseID" = %s WHERE "TransactionID" = %s;'
        self.execute_query(query, (part_id, rack_id, reciever_id, warehouse_id, transaction_id,))
        self.commit()
