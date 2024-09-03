from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
from jwt_manager import create_token
from config.database import  engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = 'Mi Aplicación con FastAPI'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'], status_code=status.HTTP_200_OK)
def message():
    return HTMLResponse('<h1>Hello World</h1>',status_code=status.HTTP_200_OK)


