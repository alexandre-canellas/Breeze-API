from pydantic import BaseModel
from model.videogame import Videogame
from typing import List, Optional

class VideogameSchema(BaseModel):
    """ 
    Define como um novo videogame a ser inserido deve ser representado
    """
    
    title: str = "Super Mario Bros"
    developer: str = "Nintendo"
    category: str = "Plataforma"
    price: float = 300.00
    launch_date: Optional[str] = "1983-09-13"

class AllVideogamesSchema(BaseModel):
    """
    Define como será o retorno da busca por todos os videogames
    """

    videogame_count: int = 1
    videogames: List[VideogameSchema]

class SearchOneGameSchema(BaseModel):
    """
    Define como pesquisar por um videogame específico
    """

    title: str = "Super Mario Bros"

class ProdutoDelSchema(BaseModel):
    """ 
    Define como deve ser a estrutura do dado retornado após uma requisição de remoção
    """

    message: str = "Videogame Super Mario Bros deletado com sucesso!"

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

def show_all_games(videogames: List[Videogame]):
    """
    Retorna a contagem de videogames cadastrados e uma lista com os atributos de cada um
    """

    game_list = []

    for game in videogames:
        game_list.append(
            {
                "title": game.title,
                "developer": game.developer,
                "category": game.category,
                "price": game.price
            }
        )

    return {
        "videogame_count": len(game_list),
        "videogames": game_list
    }