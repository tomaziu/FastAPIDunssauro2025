from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retornar_ola_pessoas():
    client = TestClient(app)

    response = client.get('/')
    assert response.json() == {'msg': 'olá pessoas!'}
    assert response.status_code == HTTPStatus.OK


# --------------------- exercício 2 ---------------------


def test_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/ola-mundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
