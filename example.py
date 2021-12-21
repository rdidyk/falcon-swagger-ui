import falcon.asgi
from falcon_swagger_ui.asynchronous import register_swaggerui_app

app = falcon.asgi.App()

SWAGGERUI_URL = '/swagger'  # without trailing '/'
SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'

### For developer environment you can expose a static endpoint like:
# import pathlib
#
# SCHEMA_URL = '/static/v1/swagger.json'
# STATIC_PATH = pathlib.Path(__file__).parent / 'static'
#
# @see: http://falcon.readthedocs.io/en/stable/api/api.html#falcon.API.add_static_route
# app.add_static_route('/static', str(STATIC_PATH))
#

page_title = 'Falcon Swagger Doc'
favicon_url = 'https://falconframework.org/favicon-32x32.png'

register_swaggerui_app(
    app, SWAGGERUI_URL, SCHEMA_URL,
    page_title=page_title,
    favicon_url=favicon_url,
    config={'supportedSubmitMethods': ['get'], }
)

