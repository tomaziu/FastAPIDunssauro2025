from fastapi import FastAPI

from fast_zero.routers import auth, exercicios, read_root, users

app = FastAPI()

# router auth
app.include_router(auth.router)

# router users
app.include_router(users.router)

# router exercicios
app.include_router(exercicios.router)

# router read_root
app.include_router(read_root.router)
