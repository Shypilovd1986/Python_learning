# for running app   uvicorn app.main:app --reload
# --reload    every time reload server, when some changes were made
# uvicorn  - server
# asgi - Asynchronous Server Gateway Interface) — клиент-серверный протокол взаимодействия веб-сервера и приложения,
# дальнейшее развитие технологии WSGI.
#
# If you are curious about how the raw OpenAPI schema looks like, FastAPI automatically generates a JSON (schema) with
# the descriptions of all your API.
#
# You can see it directly at: http://127.0.0.1:8000/openapi.json


#                                   CORS
# Cross-Origin Resource Sharing (CORS) — механизм, использующий дополнительные HTTP-заголовки, чтобы дать возможность
# агенту пользователя получать разрешения на доступ к выбранным ресурсам с сервера на источнике (домене), отличном от
# того, что сайт использует в данный момент. Говорят, что агент пользователя делает запрос с другого источника
# (cross-origin HTTP request), если источник текущего документа отличается от запрашиваемого ресурса доменом,
# протоколом или портом.
# https://developer.mozilla.org/ru/docs/Web/HTTP/CORS

# https://fastapi.tiangolo.com/tutorial/cors/
#https://fastapi.tiangolo.com/advanced/middleware/      about advanced middleware

#                     connect database
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import DeclarativeBase
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
# postgres_password = os.environ.get('POSTGRES_PASSWORD')
# database_url = f"postgresql+asyncpg://postgres:{postgres_password}@localhost:5432/asyncalchemy"
#
# engine = create_async_engine(database_url, echo=True)
# # echo=True , during initialization lets us see SQL generated queries in console
#
# Base = DeclarativeBase()
# async_session = async_sessionmaker(
#     engine, class_=AsyncSession, expire_on_commit=False
# )
# Указание echo=True при инициализации движка позволит нам увидеть сгенерированные SQL-запросы в консоли. Мы должны
# отключить поведение "expire on commit (завершить при фиксации)" для сессий с expire_on_commit=False. Это связано с
# тем, что в настройках async мы не хотим, чтобы SQLAlchemy выдавал новые SQL-запросы к базе данных при обращении к уже
# закоммиченным объектам.

# docker exec -it 2bd  psql -U postgres
#  http://localhost:8000/openapi.json     return response in json format

#
# @pytest.mark.parametrize(
#     "x, y, res",
#     [
#         (1, 2, 3),
#         (2, 3, 5)
#     ]
# )
# def test_simple(x, y, res):
#     assert x + y == res
#
# pytest tests/test_main.py::test_simple

# pytest --env .test.env        use pytest using .test.env   file

#                   example of parametrize test
# @pytest.mark.parametrize(
#     "x, y, res",
#     [
#         (1, 2, 3),
#         (2, 3, 5)
#     ]
# )
# def test_simple(x, y, res):
#     assert x + y == res

# alembic init -t async <script_directory_here>
# docker rmi $(docker images -a -q)   for deleting all images

# https://habr.com/ru/articles/580866/   about fastapi alembic docker compose


# docker-compose up -d --build
# docker-compose exec web alembic init -t async migrations
# docker-compose exec web alembic revision --autogenerate -m "init"
# docker-compose exec web alembic upgrade head

#                     Email validation
# for email validation
# from pydantic import EmailStr, Body
#
# pip install "pydantic[email]"

# def send_email(email: EmailStr = Body())    body says that we should type email in body of request
#     pass

# if we use Basemodel we write without Body

#                     poetry
# pip install poetry    will install poetry  to environment
# poetry new <project name>    will create project in current folder
# poetry init    will initialize poetry for project
# poetry install    will install all packages from poetry list
# poetry add <library>      will add library to poetry list     -> poetry install
# poetry lock --no-update      will not update version only freezing it
# poetry show --tree    show all packages and dependencies
# poetry install --sync    synchronize env with install package and remove extra packages
# which poetry   show is it global poetry or local

# poetry.lock and pyproject.toml     like requirements and always must be added to git

# option + enter   import im pycharm
#

