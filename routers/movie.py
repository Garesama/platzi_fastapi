from fastapi import APIRouter
from fastapi import  Path, Query, status, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer 
from services.movie import MovieService
from schemas.movie import Movie


movie_router = APIRouter()



@movie_router.get('/movies',tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result),status_code=status.HTTP_200_OK)


@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movie)
def get_movie(id:int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(db,id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message':'No encontrado'})
    return JSONResponse(content=jsonable_encoder(result),status_code=status.HTTP_200_OK)


@movie_router.get('/movies/', tags=['movies'], response_model=Movie)
def get_movie_by_category(category:str = Query(max_length=15, min_length=5), year:int = Query(le=2022, ge=1900)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie_by_items(db,year=year,category=category)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message':'No encontrado'})
    return JSONResponse(content=jsonable_encoder(result),status_code=status.HTTP_200_OK)
    # data = [item for item in movies if item["category"] == category and item["year"] == year]
    # return JSONResponse(content=data)


@movie_router.post('/movies', tags=['movies'], response_model=dict,status_code=status.HTTP_201_CREATED)
def create_movie(movie:Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    # new_movie = MovieModel(**movie.dict())
    # db.add(new_movie)
    # db.commit()
    # movies.append(movie) ya no se necesita esta linea porque se guarda directo en la DB el registro
    return JSONResponse(content={'message':'Se registro la pelicula'},status_code=status.HTTP_201_CREATED)

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict,status_code=status.HTTP_200_OK)
def update_movie(id:int,movie:Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message':'No encontrado'})
    # for item in movies:
    #     if item['id'] == id:
    #         item['title'] = movie.title
    #         item['overview'] = movie.overview
    #         item['year'] = movie.year
    #         item['rating'] = movie.rating
    #         item['category'] = movie.category
    MovieService(db).update_movie(id,movie)
    return JSONResponse(content={'message':'Se actualizo la pelicula'},status_code=status.HTTP_200_OK)

@movie_router.delete('/movies/{id}',tags=['movies'], response_model=dict,status_code=status.HTTP_200_OK)
def delete_movie(id:int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message':'No encontrado'})
    MovieService(db).delete_movie(id,result)
    # db.delete(result)
    # db.commit()    
    # for item in movies:
    #     if item['id'] == id:
    #         movies.remove(item)
    return JSONResponse(content={'message':'Se elimino la pelicula'},status_code=status.HTTP_200_OK)
