import pytest
from truck_delivery_fernando.db_redis_connector import DBRedisConnector
from truck_delivery_fernando.client_manager import ClientManager
from truck_delivery_fernando.util.constants import UID


@pytest.fixture
def client_manager(mocker):
    obj_to_return = {"Client1": {"name": "test1"}}
    list = [{"Client1": {"name": "test2"}}, {"Client2": {"name": "test2"}}, {"Client3": {"name": "test3"}}]
    db_connector = DBRedisConnector()
    mocker.patch("truck_delivery_fernando.db_redis_connector.DBRedisConnector.save").return_value = True
    mocker.patch("truck_delivery_fernando.db_redis_connector.DBRedisConnector.get_all").return_value = list
    mocker.patch("truck_delivery_fernando.db_redis_connector.DBRedisConnector.get_by_id").return_value = obj_to_return
    mocker.patch("truck_delivery_fernando.db_redis_connector.DBRedisConnector.delete").return_value = 1
    return ClientManager()


def test_save_document(client_manager):
    client = {"Client1": {"name": "test1"}}
    actual_result = client_manager.save_document(UID, client)
    assert actual_result


def test_get_document(client_manager):
    actual_result = client_manager.get_document(UID)
    expected = {"Client1": {"name": "test1"}}
    assert actual_result == expected


def test_get_all(client_manager):
    actual_result = client_manager.get_all()
    expected = [{"Client1": {"name": "test2"}}, {"Client2": {"name": "test2"}}, {"Client3": {"name": "test3"}}]
    assert actual_result == expected


def test_delete(client_manager):
    actual_result = client_manager.delete(UID)
    expected = 1
    assert actual_result == expected
