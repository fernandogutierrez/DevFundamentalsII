from truck_delivery_fernando.content_manager import ContentManager
from truck_delivery_fernando.db_redis_connector import DBRedisConnector


class ClientManager(ContentManager):
    def __init__(self):
        super(ClientManager, self).__init__()
        self.db_connector = DBRedisConnector()

    def save_document(self, id, client):
        return self.db_connector.save(id, client)

    def get_document(self, obj_id):
        return self.db_connector.get_by_id(obj_id)

    def get_all(self):
        return self.db_connector.get_all()

    def delete(self, obj_id):
        return self.db_connector.delete(obj_id)
