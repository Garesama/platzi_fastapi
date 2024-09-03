
from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id:Optional[int] = None
    title:str = Field(max_length=15, min_length=5) # Este es una forma de agregar validaciones adicionales a las que ofrece FastAPI
    overview:str = Field(max_length=50, min_length=15)
    year:int = Field(le=2022)
    rating:float = Field(le=10, ge=1) # ge es mayor e igual y le es menor o igual
    category:str = Field(max_length=15, min_length=5)

    # De este se agrega caracteristicas por default FastAPI
    class Config:
        schema_extra = {
            'example':{
                'id':1,
                'title':'Mi Pelicula',
                'overview':'Descripción de la Pelicula',
                'year':2022,
                'rating':9.8,
                'category':'Acción'
            }
        }