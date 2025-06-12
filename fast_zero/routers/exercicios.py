from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import UserPublic

router = APIRouter(prefix='/exercicios', tags=['exercicios'])

# --------------------- exercício 2 ---------------------


@router.get(
    '/ola_mundo', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def ola_mundo():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""


# --------------------- exercício 5 ---------------------


@router.get(
    '/users/encontrar_usuario/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def read_user_id(user_id: int, session=Depends(get_session)):
    user = session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='usuário não encontrado'
        )

    return user
