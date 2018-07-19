import falcon
from falcon_swagger_ui import register_swaggerui_app

SWAGGERUI_URL = '/swagger'  # without trailing '/'
SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'
"""
# For developer environment you can expose a static endpoint like:
from falcon_swagger_ui import StaticSinkAdapter

SCHEMA_URL = '/v2/swagger.json'

app.add_sink(
    StaticSinkAdapter('path/to/your/swagger/schema.json'), SCHEMA_URL
)

"""

app = falcon.API()

page_title = 'Falcon Swagger Doc'
favicon_url = 'https://falconframework.org/favicon-32x32.png'
register_swaggerui_app(app, SWAGGERUI_URL, SCHEMA_URL, page_title, favicon_url, config={
    'supportedSubmitMethods': ['get'],
})

