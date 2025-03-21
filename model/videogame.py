from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Videogame(Base):
    __tablename__ = 'videogames'

    id = Column("pk_videogame", Integer, primary_key=True)
    title = Column(String(140), unique=True)
    # desenvolvedor = Column(String(140))
    # genero = Column(String(140))
    price = Column(Float)
    # data_lancamento = Column(DateTime, default=datetime.now())

    # TODO: Adicionar uma tabela de reviews que contemplem uma classificação
    # podendo ser positiva ou negativa

    def __init__(self, title:str, price:float):
        """
        Lança um jogo na plataforma

        Argumentos:
            title: nome do jogo.
            desenvolvedor: nome da empresa ou entidade responsável pela criação do jogo.
            genero: gênero de classificação do jogo (ação, terror, etc).
            price: valor cheio do jogo em reais.
            data_lancamento: data de quando o produto foi lançado
        """
        self.title = title
        # self.desenvolvedor = desenvolvedor
        # self.genero = genero
        self.price = price

        # Se não for informada, será o data exata da inserção no banco
        # if data_lancamento:
        #     self.data_lancamento = data_lancamento