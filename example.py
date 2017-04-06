import falcon
from falcon_swagger_ui import register_swaggerui_app

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

application = falcon.API()

register_swaggerui_app(application, SWAGGER_URL, API_URL, config={
    'supportedSubmitMethods': ['get'],
})

