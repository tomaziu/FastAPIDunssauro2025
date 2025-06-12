from http import HTTPStatus


def test_root_retornar_ola_pessoas(client):
    response = client.get('/ola_mundo')

    assert response.json() == {'msg': 'olá pessoas!'}
    assert response.status_code == HTTPStatus.OK
