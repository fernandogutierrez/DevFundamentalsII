import redis
import json


class DBConnector:
    def __init__(self):
        self.connection = self.get_connection()

    def get_connection(self):
        return redis.Redis(host='192.168.5.129', port=6379)

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encode_data)
        return result_save

    def get_by_id(self, id):
        result_get = self.connection.get(id)
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        obj_list = []
        id_list = [id for id in self.connection.scan_iter(count=50)]
        if len(id_list) > 0:
            all_obj = self.connection.mget(id_list)
            obj_list = [json.loads(obj) for obj in all_obj]
        return obj_list

    def delete(self, id):
        return self.connection.delete(id)
