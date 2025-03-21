from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Videogame
from schemas import VideogameSchema

info = Info(title="Breeze API", version="1.0.0", description="Uma API voltada para plataforma de jogos eletrônicos")
app = OpenAPI(__name__, info=info)

@app.get('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/videogame')
def add_videogame(form: VideogameSchema):
    """
    Cadastra um videogame novo na base com seus atributos
    Retorna o videogame cadastrado para confirmação
    """

    try:
        
        videogame = Videogame(
        title = form.title,
        price = form.price
        )

        session = Session()
        session.add(videogame)
        session.commit()

        return f"{videogame.title} cadastrado com sucesso!", 200
    
    except IntegrityError:
        
        return "Videogame já cadastrado na base, tente outro titulo!", 409

    except Exception as e:

        return "Erro ao cadastrar item", 400

if __name__ == '__main__':
    app.run(debug=True)