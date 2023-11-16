from DAO.dao import BaseDAO


class MostGlobalStatisticsDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def get_most_rack(self):
        query = '''Select "WarehouseID", "WarehouseName", count("RackID") as count
            From "Warehouses" natural join "Racks"
            GROUP BY "WarehouseID", "WarehouseName"
            ORDER BY count desc
            Limit 10;'''
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()

    def get_most_incoming(self):
        query = '''Select "WarehouseID", "WarehouseName", count("TransactionID") as count
            FROM "Inventory_Incoming_Transactions" natural join "Warehouses"
            Group by "WarehouseID", "WarehouseName"
            Order by count desc
            Limit 5;'''
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()

    def get_most_deliver(self):
        query = '''Select "WarehouseID", "WarehouseName", count("TransactionID") as count
            FROM "Inventory_Transfer_Transactions" join "Warehouses" on "WarehouseID"="SourceWarehouseID"
            Group by "WarehouseID", "WarehouseName"
            Order by count desc
            Limit 5;'''
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()

    def get_most_transactions(self):
        query = '''Select "UserID", "Username", count("TransactionID") as count
            From "Users" natural join "Transactions"
            Group by "UserID", "Username"
            ORDER BY count desc
            Limit 3;'''
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()

    def get_most_city(self):
        query = '''Select "WarehouseCity", count("TransactionID") as count
            From "Warehouses" natural join "Users" natural join "Transactions"
            Group by "WarehouseCity"
            Order by count desc
            limit 3;'''
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()


