from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retornar_ola_pessoas():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'msg': 'olá pessoas!'}
    assert response.status_code == HTTPStatus.OK
