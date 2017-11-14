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

    register_swaggerui_app(app, SWAGGERUI_URL, SCHEMA_URL, config={
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
