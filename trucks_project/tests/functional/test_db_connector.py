import pytest
from truck_delivery_fernando.db_connector import DBConnector


def test_save():
    id_test = "123"
    object_to_save = {"123": {"name": "a"}}

    db_connector = DBConnector()
    result = db_connector.save(id_test, object_to_save)
    assert result


def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"name": "a"}}

    db_connector = DBConnector()
    db_connector.save(id_test, object_to_save)
    result = db_connector.get_by_id(id_test)
    assert result == object_to_save

