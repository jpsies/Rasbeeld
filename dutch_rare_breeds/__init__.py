from configparser import ConfigParser
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .routes import setup_routes
from .lib.db.model.meta import Base


def main(global_config, **settings):
    config = Configurator(settings=settings)

    project_settings = ConfigParser()
    project_settings.read((global_config['__file__'],))

    engine = engine_from_config(project_settings['alembic'], 'sqlalchemy.')
    Base.metadata.bind = engine

    setup_routes(config)
    config.scan('dutch_rare_breeds.handlers')

    config.add_static_view(name='stylesheets', path='dutch_rare_breeds:static/css')
    config.add_static_view(name='javascript', path='dutch_rare_breeds:static/js')
    config.add_static_view(name='images', path='dutch_rare_breeds:static/images')

    return config.make_wsgi_app()
