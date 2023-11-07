from PartsDAO import PartsDAO


class DAOFactory:
    def __init__(self, conn):
        self.conn = conn

    def get_parts_dao(self):
        return PartsDAO(self.conn)
    