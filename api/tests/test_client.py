import json
import pytest

from api.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_save_client(client):
    rv = client.post('/api/v1/client',
                     headers={'Content-Type': 'application/json'},
                     json=json.dumps({
                         "ci": "569874",
                         "name": "Fernando",
                         "email": "fernando@gmail.com",
                         "cellphone": "4444444",
                         "age": "27",
                         "address": "Av Circunvalacion",
                         "nit": "14586"
                     }))
    assert rv.status_code == 200
    # res_get = client.get(f"/api/v1/client/{json.loads(rv.data)['id']}")
    # assert res_get.status_code == 200
    # assert isinstance(res_get.json, str)


def test_delete_client(client):
    rv = client.post('/api/v1/client',
                     headers={'Content-Type': 'application/json'},
                     json=json.dumps({
                         "ci": "5698742",
                         "name": "Fernando2",
                         "email": "fernando@gmail.com2",
                         "cellphone": "44444442",
                         "age": "27",
                         "address": "Av Circunvalacion2",
                         "nit": "145862"
                     }))
    res_del = client.delete(f"/api/v1/client/{json.loads(rv.data)['id']}")
    assert res_del.status_code == 200
    res_del_json = json.loads(res_del.data)
    assert res_del_json['status'] == 'Success'


def test_get_client_by_id(client):
    rv = client.post('/api/v1/client',
                     headers={'Content-Type': 'application/json'},
                     json=json.dumps({
                         "ci": "5698742",
                         "name": "Fernando2",
                         "email": "fernando@gmail.com2",
                         "cellphone": "44444442",
                         "age": "27",
                         "address": "Av Circunvalacion2",
                         "nit": "145862"
                     }))
    res_get = client.get(f"/api/v1/client/{json.loads(rv.data)['id']}")
    assert res_get.status_code == 200
    assert isinstance(res_get.json, str)
