from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Jogo(Base):
    __tablename__ = 'jogo'

    id = Column("pk_jogo", Integer, primary_key=True)
    titulo = Column(String(140), unique=True)
    desenvolvedor = Column(String(140))
    genero = Column(String(140))
    valor = Column(Float)
    data_lancamento = Column(DateTime, default=datetime.now())

    # TODO: Adicionar uma tabela de reviews que contemplem uma classificação
    # podendo ser positiva ou negativa

    def __init__(self, titulo:str, desenvolvedor:str, genero:str, 
                 valor:float, data_lancamento:Union[DateTime, None] = None):
        """
        Lança um jogo na plataforma

        Arguments:
            titulo: nome do jogo.
            desenvolvedor: nome da empresa ou entidade responsável pela criação do jogo.
            genero: gênero de classificação do jogo (ação, terror, etc).
            valor: valor cheio do jogo em reais.
            data_lancamento: data de quando o produto foi lançado
        """
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.genero = genero
        self.valor = valor

        # Se não for informada, será o data exata da inserção no banco
        if data_lancamento:
            self.data_lancamento = data_lancamento