from .PartsDAO import PartsDAO
from .RacksDAO import RacksDAO
from .UsersDAO import UsersDAO
from .WarehousesDAO import WarehousesDAO
from .SuppliersDAO import SuppliersDAO


class DAOFactory:
    def __init__(self, conn):
        self.conn = conn

    def get_parts_dao(self):
        return PartsDAO(self.conn)

    def get_racks_dao(self):
        return RacksDAO(self.conn)

    def get_users_dao(self):
        return UsersDAO(self.conn)

    def get_warehouses_dao(self):
        return WarehousesDAO(self.conn)

    def get_suppliers_dao(self):
        return SuppliersDAO(self.conn)