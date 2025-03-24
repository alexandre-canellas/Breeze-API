from pydantic import BaseModel
from model.videogame import Videogame

class VideogameSchema(BaseModel):
    """ 
    Define como um novo videogame a ser inserido deve ser representado
    """
    
    title: str = "Super Mario Bros"
    developer: str = "Nintendo"
    category: str = "Plataforma"
    price: float = 300.00
    launch_date: str = "1983-09-13"

class SearchOneGameSchema(BaseModel):
    """
    Define como pesquisar por um videogame específico
    """

    title: str = "Super Mario Bros"

def show_searched_game(videogame: Videogame):
    """
    Retorna os atributos de um videogame pesquisado
    """

    return {
        "title": videogame.title,
        "developer": videogame.developer,
        "category": videogame.category,
        "price": videogame.price,
        "launch_date": videogame.launch_date
    }