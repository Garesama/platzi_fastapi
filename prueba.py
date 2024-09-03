from models.movie import Movie as MovieModel

def get_movie_by_items(title=None,overview=None,year=None,rating=None,category=None):
    valor = []
    clave = []
    keys = {
        'title':title,
        'overview': overview,
        'year':year,
        'rating':rating,
        'category':category,
    }
    for item in keys:
        if keys[item] is not None:
            valor.append(keys[item])
            clave.append(item)
    
    print(clave,valor)


get_movie_by_items(title='str',category='ddd')