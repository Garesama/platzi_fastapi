from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user:User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token:str = create_token(user.dict())
        return JSONResponse(content=token, status_code=status.HTTP_200_OK)