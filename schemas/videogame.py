from pydantic import BaseModel

class VideogameSchema(BaseModel):
    """ 
    Define como um novo videogame a ser inserido deve ser representado.
    """
    
    title: str = "Super Mario Bros"
    developer: str = "Nintendo"
    category: str = "Plataforma"
    price: float = 300.00
    launch_date: str = "1983-09-13"

class SearchOneGameSchema(BaseModel):
    """
    Define como pesquisar por um videogame específico.
    """

    title: str = "Super Mario Bros"