falcon-swagger-ui
=================

|nbsp| |pypi-version| |nbsp|

|bmac-button|

Simple Falcon application for adding `Swagger UI`_ to your falcon
application.

Included Swagger UI version: v3.10.0

Installation
------------

``pip install falcon-swagger-ui``

Usage
-----

Example application:

.. code:: python

    import falcon
    from falcon_swagger_ui import register_swaggerui_app

    app = falcon.API()

    SWAGGERUI_URL = '/swagger'  # without trailing slash
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


Running the example application:

.. code:: bash

    pip install falcon gunicorn jinja2
    gunicorn example:app


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

.. |bmac-button| image:: https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png
   :target: https://www.buymeacoffee.com/5xROZDjHE
   :alt: Buy Me A Coffee

.. |pypi-version| image:: https://img.shields.io/pypi/v/falcon-swagger-ui.svg
   :target: https://pypi.org/project/falcon-swagger-ui/
   :alt: PyPI
   
.. |nbsp| unicode:: 0xA0
   :trim:
