from sqlalchemy import Column, String, Integer, Date, Float
from datetime import datetime
from typing import Union

from  model import Base


class Videogame(Base):
    __tablename__ = 'videogames'

    id = Column("pk_videogame", Integer, primary_key=True)
    title = Column(String(140), unique=True)
    developer = Column(String(140))
    category = Column(String(140))
    price = Column(Float)
    launch_date = Column(String, default=str(datetime.today()))

    # TODO: Adicionar uma tabela de reviews que contemplem uma classificação
    # podendo ser positiva ou negativa

    def __init__(self, title:str, developer:str, category:str, price:float, launch_date:str):
        """
        Lança um jogo na plataforma

        Argumentos:
            title: nome do jogo.
            desenvolvedor: nome da empresa ou entidade responsável pela criação do jogo.
            genero: gênero de classificação do jogo (ação, terror, etc).
            price: valor cheio do jogo em reais.
            data_lancamento: data de quando o produto foi ou será lançado no formato %Y-%m-%d.
        """
        self.title = title
        self.developer = developer
        self.category = category
        self.price = price

        # Se não for informada, será o data exata da inserção no banco.
        # É possível declarar uma data futura para lançamento planejado.
        if launch_date:
            self.launch_date = launch_date