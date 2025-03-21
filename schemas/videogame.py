from pydantic import BaseModel

class VideogameSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    title: str = "Super Mario Bros"
    price: float = 300.00