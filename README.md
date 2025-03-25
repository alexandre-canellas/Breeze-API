# Breeze-API
API para funcionamento de uma plataforma de jogos eletrônicos, incluindo adição, remoção e buscas por videogames.

---
## Instalação

1. Crie e inicie um ambiente virtual:

python -m venv venv
source venv/bin/activate

2. Clone o repositório em uma pasta de projetos:

(venv)$ gh repo clone alexandre-canellas/Breeze-API

3. Navegue até a pasta do repositório:

(venv)$ cd Breeze-API/

4. Instale as dependências:

(venv)$ pip install -r requirements.txt

5. Execute localmente o hosting da API:

(venv)$ python app.py

Abra o [http://127.0.0.1:5000/](http://127.0.0.1:5000/) no navegador para verificar o status da API em execução.

---
## Documentação API
Documentação em Swagger está disponível no link principal da API

---
## Endpoints disponíveis

| Status Code | Descrição                       |
|-------------|---------------------------------|
| 200 OK      | Requisição bem sucedida         |
| 404 Not Found | Recurso não encontrado        |
| 409 Conflict | Conflito na requisição         |
| 500 Internal Server Error | Erro inesperado   |