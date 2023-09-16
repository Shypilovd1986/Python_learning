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