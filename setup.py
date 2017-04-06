import os
from setuptools import setup


def read_requirements(filename):
    """Open a requirements file and return list of its lines."""
    contents = read_file(filename).strip('\n')
    return contents.split('\n') if contents else []


def read_file(filename):
    """Open a file, read it and return its contents."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()

setup(
    name='falcon-swagger-ui',
    version='0.0.1',
    description='Swagger UI Application for Falcon',

    # Get the long description from the README file
    long_description=read_file('README.md'),

    url='https://github.com/rdidyk/falcon-swagger-ui',
    download_url='https://github.com/rdidyk/falcon-swagger-ui/archive/0.0.1.tar.gz',

    author='Ruslan Didyk',
    author_email='rdidyk@tmgtop.com',
    license='MIT',

    classifiers=[
        'Development Status :: 0.0.1 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='falcon swagger',
    packages=['falcon_swagger_ui'],
    include_package_data=True,
    zip_safe=False,

    install_requires=read_requirements('requirements.txt'),

    package_data={
        'falcon_swagger_ui': [
            'README.md',
            'templates/*.html',
            'dist/VERSION',
            'dist/LICENSE',
            'dist/README.md',
            'dist/*.html',
            'dist/*.js',
            'dist/*/*.js',
            'dist/*/*.css',
            'dist/*/*.gif',
            'dist/*/*.png',
            'dist/*/*.ico',
            'dist/*/*.ttf',
        ],
    }
)
