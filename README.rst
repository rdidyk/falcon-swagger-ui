falcon-swagger-ui
=================

Simple Falcon application for adding `Swagger UI`_ to your falcon
application.

Included Swagger UI version: 2.2.8.

Installation
------------

``pip install falcon-swagger-ui``

Usage
-----

Example application:

.. code:: python

    import falcon
    from falcon_swagger_ui import register_swaggerui_app

    SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
    API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

    application = falcon.API()

    register_swaggerui_app(application, SWAGGER_URL, API_URL, config={
        'supportedSubmitMethods': ['get'],
    })

Configuration
-------------

The application supports overloading all Swagger UI configuration
options that can be JSON serialized. See
https://github.com/swagger-api/swagger-ui#parameters for options.

In addition, some of the OAuth fields are exposed to special variables
that will be rendered into the relevant function.

Application defaults are listed below (should match SwaggerUI defaults).

.. code:: python

    {
            # OAuth related
            'app_name': 'null',
            'client_realm': 'null',
            'client_id': 'null',
            'client_secret': 'null',

            # SwaggerUI base configuration, see https://github.com/swagger-api/swagger-ui#parameters
            'docExpansion': "none",
            'jsonEditor': False,
            'defaultModelRendering': 'schema',
            'showRequestHeaders': False,
            'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch']
    }

.. _Swagger UI: https://github.com/swagger-api/swagger-ui
