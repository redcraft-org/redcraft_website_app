from flask import Flask

from dynaconf import FlaskDynaconf
from sassutils.wsgi import SassMiddleware


def main():
    app = Flask(__name__)
    FlaskDynaconf(app)

    if app.config.env == 'development':
        app.wsgi_app = SassMiddleware(app.wsgi_app, {
            'app': ('static/sass', 'static/css', '/static/css')
        })

    # TODO: Add dynamic import 
    from views import (
        home
    )
    app.register_blueprint(home.bp)

    return app

app = main()
if __name__ == '__main__':
    app.run()
