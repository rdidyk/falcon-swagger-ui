import os
from setuptools import setup

CURRENT_VERSION = '0.0.8'


def read_file(filename):
    """Open a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()

setup(
    name='falcon-swagger-ui',
    version=CURRENT_VERSION,
    description='Swagger UI Application for Falcon',

    # Get the long description from the README file
    long_description=read_file('README.rst'),

    url='https://github.com/rdidyk/falcon-swagger-ui',
    download_url='https://github.com/rdidyk/falcon-swagger-ui'
                 '/archive/{}.tar.gz'.format(CURRENT_VERSION),

    author='Ruslan Didyk',
    author_email='rdidyk@tmgtop.com',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='falcon swagger',
    packages=['falcon_swagger_ui'],

    install_requires=[
        'falcon',
        'Jinja2',
    ],

    package_data={
        'falcon_swagger_ui': [
            'README.rst',
            'setup.cfg',
            'LICENSE',
            'templates/*',
            'dist/*',
            'dist/*/*',
        ],
    }
)
