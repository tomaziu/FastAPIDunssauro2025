# --------------------- exercício 2 ---------------------

from http import HTTPStatus


def test_retornar_ola_mundo(client):
    response = client.get('/exercicios/ola_mundo')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


# --------------------- exercício 3 ---------------------


def test_update_user_nao_existente(client, token):
    response = client.put(
        '/users/100',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'não é possível atualizar'}


def test_delete_user_nao_existente(client, token):
    response = client.delete(
        '/users/100',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'não é possível deletar'}


def test_get_user_nao_existente(client):
    response = client.get('exercicios/users/100')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not Found'}


# --------------------- exercício 5 ---------------------


def test_create_user_erro_404_username(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'usuário já cadastrado'}


def test_create_user_erro_404_email(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'bob',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'email já cadastrado'}


def test_get_user_id(client, user):
    response = client.get('/exercicios/users/encontrar_usuario/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_user_id_nao_existente(client):
    response = client.get('exercicios/users/100')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Not Found'}


def test_user_not_found(client, user):
    response = client.get('/exercicios/users/encontrar_usuario/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'usuário não encontrado'}
