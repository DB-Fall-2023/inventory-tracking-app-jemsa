from dao import BaseDAO

class PartsDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_parts(self, part_name, part_type, part_price):
        query = "INSERT INTO Parts (PartName, PartType, PartPrice) VALUES (%s, %i, %f) RETURNING PartID;"
        self.execute_query(query, (part_name, part_type, part_price,))
        self.commit()

    def get_parts(self):
        query = "SELECT * FROM Parts;"
        cur = self.execute_query(query)
        return cur.fetchall()
    
    def get_part_by_id(self, part_id):
        query = "SELECT * FROM Parts WHERE PartID = %s;"
        cur = self.execute_query(query, (part_id,))
        return cur.fetchone()

    def get_part_by_id(self, part_id, part_name, part_type, part_price):
        query = "UPDATE Parts Set PartName = %s, PartType = %s, PartPrice = %s WHERE PartID = %s;"
        self.execute_query(query, (part_name, part_type, part_price, part_id,))
        self.commit()

    def delete_part_by_id(self, part_id):
        query = "DELETE FROM Parts Where PartID = %s;"
        self.execute_query(query, (part_id,))
        self.commit()