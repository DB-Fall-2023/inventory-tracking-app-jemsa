from .PartsDAO import PartsDAO
from .RacksDAO import RacksDAO 


class DAOFactory:
    def __init__(self, conn):
        self.conn = conn

    def get_parts_dao(self):
        return PartsDAO(self.conn)
    
    def get_racks_dao(self):
        return RacksDAO(self.conn)