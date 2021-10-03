import json

import redis
from redis import TimeoutError, ConnectionError

from truck_delivery_fernando.db_connector import DBConnector
from truck_delivery_fernando.util.json import validate_json


class DBRedisConnector(DBConnector):
    def __init__(self):
        super(DBRedisConnector, self).__init__()
        self.connection = None
        self.get_connection()

    def get_connection(self):
        try:
            if self.connection is None:
                self.connection = redis.Redis(host='192.168.5.129', port=6379)
            self.connection.ping()
        except(TimeoutError, ConnectionError) as redis_exc:
            raise Exception(f"The Redis database is not available. Details: [ {redis_exc} ]")
        else:
            return self.connection

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encode_data)
        return result_save, json.loads(encode_data)

    def get_by_id(self, id):
        result_get = self.connection.get(id)
        decode_data = json.loads(result_get) if validate_json(result_get) else '{}'
        return decode_data

    def get_all(self):
        obj_list = []
        id_list = [id for id in self.connection.scan_iter(count=50)]
        if len(id_list) > 0:
            all_obj = self.connection.mget(id_list)
            obj_list = [json.loads(obj) for obj in all_obj if validate_json(obj)]
        return obj_list

    def delete(self, id):
        return self.connection.delete(id)
