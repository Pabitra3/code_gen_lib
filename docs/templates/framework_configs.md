# Framework Configuration Templates

This document describes the framework configuration templates available in the Code Generation Library. These templates are used to generate configuration files for various web frameworks.

## Supported Frameworks

Currently, the library supports configuration generation for the following frameworks:

1. Flask
2. Django
3. FastAPI

## Usage

To generate framework configurations, use the `configure_framework` method of the `CodeGenerator` class:

```python
from code_gen_lib import CodeGenerator

generator = CodeGenerator('path/to/config.yaml')

framework_config = {
    # Framework-specific configuration options
}

generator.configure_framework('framework_name', framework_config, 'output/directory')

Replace 'framework_name' with one of the supported frameworks (e.g., 'flask', 'django', 'fastapi').
Flask Configuration
Template Location
       templates/framework/flask/

Files Generated

app.py: Main application file
config.py: Configuration settings
requirements.txt: Project dependencies

Example Usage
     flask_config = {
    'secret_key': 'my_secret_key',
    'debug': True,
    'port': 5000,
    'database_uri': 'sqlite:///site.db'
}

generator.configure_framework('flask', flask_config, 'output/flask_app')

Template Content Examples
app.py
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])

config.py
class Config:
    SECRET_KEY = '{{ secret_key }}'
    DEBUG = {{ debug }}
    PORT = {{ port }}
    SQLALCHEMY_DATABASE_URI = '{{ database_uri }}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Django Configuration
Template Location
     templates/framework/django/

Files Generated

settings.py: Project settings
urls.py: URL configuration
wsgi.py: WSGI application
manage.py: Django management script
requirements.txt: Project dependencies

Example Usage
     django_config = {
    'secret_key': 'my_secret_key',
    'debug': True,
    'allowed_hosts': ['localhost', '127.0.0.1'],
    'database': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

generator.configure_framework('django', django_config, 'output/django_project')

Template Content Examples
settings.py
  import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '{{ secret_key }}'

DEBUG = {{ debug }}

ALLOWED_HOSTS = {{ allowed_hosts }}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {{ database }}
}

FastAPI Configuration
Template Location
      templates/framework/fastapi/

Files Generated

main.py: Main application file
config.py: Configuration settings
requirements.txt: Project dependencies

Example Usage
     fastapi_config = {
    'debug': True,
    'port': 8000,
    'host': '0.0.0.0',
    'database_url': 'sqlite:///./test.db'
}

generator.configure_framework('fastapi', fastapi_config, 'output/fastapi_app')


Template Content Examples
main.py
    from fastapi import FastAPI
from config import settings

app = FastAPI(debug=settings.DEBUG)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)

config.py
     from pydantic import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = {{ debug }}
    PORT: int = {{ port }}
    HOST: str = '{{ host }}'
    DATABASE_URL: str = '{{ database_url }}'

settings = Settings()

