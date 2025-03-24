from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Videogame
from schemas import VideogameSchema, SearchOneGameSchema, ErrorSchema, show_searched_game

info = Info(title="Breeze API", version="1.0.1", description="Uma API voltada para plataforma de jogos eletrônicos")
app = OpenAPI(__name__, info=info)

@app.get('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/videogame', 
          responses={"200": VideogameSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_videogame(form: VideogameSchema):
    """
    Cadastra um videogame novo na base com seus atributos
    Retorna o videogame cadastrado para confirmação
    """

    try:
        
        videogame = Videogame(
        title = form.title,
        developer=form.developer,
        category=form.category,
        price = form.price,
        launch_date=form.launch_date # Opcional, podendo ser omitido
        )

        # Inicia a sessão para adicionar o novo item na base
        session = Session()
        session.add(videogame)
        session.commit()

        return f"{videogame.title} cadastrado com sucesso!", 200
    
    except IntegrityError:
        
        return "Videogame já cadastrado na base, tente outro titulo!", 409

    except Exception as e:

        return "Erro ao cadastrar item", 400
    
@app.get('/videogame',
         responses={"200": VideogameSchema, "404": ErrorSchema})
def search_videogame(query: SearchOneGameSchema):
    """
    Procura um videogame específico na base de acordo com o seu título
    Retorna todos os atributos acessíveis do videogame pesquisado
    """

    try:

        # Coleta o videogame a ser buscado
        searched_game = query.title

        # Inicia a sessão para busca do item
        session = Session()
        game = session.query(Videogame).filter(Videogame.title == searched_game).first()
        
        if game:
            # Videogame encontrado
            
            return show_searched_game(game), 200
        
        else:

            return "Videogame não encontrado, tente outro!", 404
        
    except Exception as e:

        return "Erro de servidor", 500

if __name__ == '__main__':
    app.run(debug=True)