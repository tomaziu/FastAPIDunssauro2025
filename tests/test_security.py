from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, SECRET_KEY, create_acess_token


def test_jwt():
    data = {'test': 'test'}

    token = create_acess_token(data)

    decoded = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert decoded['test'] == data['test']
    assert 'exp' in decoded


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {
        'detail': 'Não foi possível validar as credenciais'
    }


# --------------------- exercício 6 ---------------------


def test_get_current_user_not_found(client):
    data = {'no-email': 'test'}
    token = create_acess_token(data)

    respose = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert respose.status_code == HTTPStatus.UNAUTHORIZED
    assert respose.json() == {
        'detail': 'Não foi possível validar as credenciais'
    }


def test_get_current_user_does_not_exists(client):
    data = {'sub': 'test@test.com'}
    token = create_acess_token(data)

    respose = client.delete(
        '/users/1', headers={'Authorization': f'Bearer {token}'}
    )

    assert respose.status_code == HTTPStatus.UNAUTHORIZED
    assert respose.json() == {
        'detail': 'Não foi possível validar as credenciais'
    }
