import pytest
from truck_delivery_fernando.db_redis_connector import DBRedisConnector
from truck_delivery_fernando.client_manager import ClientManager


@pytest.fixture
def client_manager(mocker):
    object_to_save = {"Client1": {"name": "test1"}}
    object_to_return = {"Client1": {"name": "test1"}}
    list = [{"Client1": {"name": "test2"}}, {"Client2": {"name": "test2"}}, {"Client3": {"name": "test3"}}]
    mocker.patch("truck_delivery_fernando.client_manager.ClientManager.save_document").return_value = object_to_save
    mocker.patch("truck_delivery_fernando.client_manager.ClientManager.get_document").return_value = object_to_return
    mocker.patch("truck_delivery_fernando.client_manager.ClientManager.get_all").return_value = list
    mocker.patch("truck_delivery_fernando.client_manager.ClientManager.delete").return_value = 1

    return ClientManager()


def test_save_document(client_manager):
    client = {"Client1": {"name": "test1"}}
    actual_result = client_manager.save_document(client)
    expected = {"Client1": {"name": "test1"}}
    assert actual_result == expected


def test_get_document(client_manager):
    client = {"Client1": {"name": "test1"}}
    actual_result = client_manager.save_document(client)
    expected = client_manager.get_document()
    assert actual_result == expected


def test_get_all(client_manager):
    actual_result = client_manager.get_all()
    expected = [{"Client1": {"name": "test2"}}, {"Client2": {"name": "test2"}}, {"Client3": {"name": "test3"}}]
    assert actual_result == expected


def test_delete(client_manager):
    client = {"Client": {"name": "test1", "id": 15}}
    actual_result = client_manager.delete(client.get("Client").get("id"))
    expected = 1
    assert actual_result == expected
