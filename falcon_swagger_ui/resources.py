import os
import json
import falcon
import jinja2
import mimetypes


class TemplateRenderer(object):

    def __init__(self, templates_path):
        self.tpl_path = templates_path

    def render(self, tpl_name, *args, **kwargs):
        template = self._load_template(tpl_name)
        return template.render(*args, **kwargs)

    def _load_template(self, tpl):

        curr_dir = os.path.dirname(os.path.abspath(__file__))

        path, filename = os.path.split(tpl)

        templates_directory = os.path.join(curr_dir, self.tpl_path)

        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(path, templates_directory)
            )
        ).get_template(filename)


class StaticSinkAdapter(object):

    def __init__(self, static_path):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.static_dir = os.path.join(curr_dir, static_path)

    def __call__(self, req, resp, filepath):
        resp.content_type = mimetypes.guess_type(filepath)[0]
        file_path = os.path.normpath(
            os.path.join(self.static_dir, filepath)
        )
        if not file_path.startswith(self.static_dir + os.sep):
            raise falcon.HTTPNotFound()
        if not os.path.exists(file_path):
            raise falcon.HTTPNotFound()

        stream = open(file_path, 'rb')
        stream_len = os.path.getsize(file_path)
        resp.set_stream(stream, stream_len)


class SwaggerUiResource(object):

    def __init__(self, templates_folder, default_context):
        self.templates = TemplateRenderer(templates_folder)
        self.context = default_context

    def on_get(self, req, resp):
        resp.content_type = 'text/html'
        resp.body = self.templates.render('index.html', **self.context)


def register_swaggerui_app(app, swagger_uri, api_url, page_title='Swagger UI', favicon_url=None, config=None, uri_prefix=""):

    """:type app: falcon.API"""

    templates_folder = 'templates'
    static_folder = 'dist'

    default_config = {
        'client_realm': 'null',
        'client_id': 'null',
        'client_secret': 'null',
        'app_name': 'null',
        'docExpansion': "none",
        'jsonEditor': False,
        'defaultModelRendering': 'schema',
        'showRequestHeaders': False,
        'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch'],
    }

    if config:
        default_config.update(config)

    default_context = {
        'page_title': page_title,
        'favicon_url': favicon_url,
        'base_url': uri_prefix + swagger_uri,
        'api_url': api_url,
        'app_name': default_config.pop('app_name'),
        'client_realm': default_config.pop('client_realm'),
        'client_id': default_config.pop('client_id'),
        'client_secret': default_config.pop('client_secret'),
        # Rest are just serialized into json string
        # for inclusion in the .js file
        'config_json': json.dumps(default_config)
    }

    app.add_sink(
        StaticSinkAdapter(static_folder),
        r'%s/(?P<filepath>.*)\Z' % swagger_uri,
    )

    app.add_route(
        swagger_uri,
        SwaggerUiResource(templates_folder, default_context)
    )
