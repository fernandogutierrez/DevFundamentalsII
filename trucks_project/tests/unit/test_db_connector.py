import pytest
import json
from truck_delivery_fernando.db_connector import DBConnector


@pytest.fixture
def fixture_db_connector(mocker):
    object_to_save = {"123": {"name": "test1"}}
    object_list = [{"ID1": {"name": "test1"}}, {"ID2": {"name": "test2"}}, {"ID3": {"name": "test2"}}]
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    mocker.patch("redis.Redis.mget").return_value = [json.dumps(obj) for obj in object_list]
    mocker.patch("redis.Redis.delete").return_value = 1
    db_conn = DBConnector()
    return db_conn


def test_save_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"name": "test1"}}

    result_save = fixture_db_connector.save(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(fixture_db_connector):
    id_test = "123"
    object_to_save = {"123": {"name": "test1"}}
    fixture_db_connector.save(id_test, object_to_save)
    result = fixture_db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_gell_all_mock(fixture_db_connector):
    actual_list = fixture_db_connector.get_all()
    expected_list = [{"ID1": {"name": "test1"}}, {"ID2": {"name": "test2"}}, {"ID3": {"name": "test2"}}]
    assert actual_list == expected_list


def test_delete_mock(fixture_db_connector):
    id_to_delete = "123"
    actual_res = fixture_db_connector.delete(id_to_delete)
    expected_res = 1
    assert actual_res == expected_res


def test_get_by_id_mock_as_context_manager(mocker):
    id_test = "123"
    object_to_save = {"123": {"name": "test1"}}
    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)

    result = None
    with DBConnector() as db_connector:
        db_connector.save(id_test, object_to_save)
        result = db_connector.get_by_id(id_test)
    assert result
