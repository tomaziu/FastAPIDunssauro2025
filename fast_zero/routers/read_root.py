from http import HTTPStatus

from fastapi import APIRouter

from fast_zero.schemas import Message

router = APIRouter(prefix='/ola_mundo', tags=['ola_mundo'])


@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'msg': 'olá pessoas!'}
