from flask import Flask
from ..database.db import Database

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    from .top import bp as bp_top
    app.register_blueprint(bp_top)
    from .auth import bp as bp_auth
    app.register_blueprint(bp_auth)
    from .api import bp as bp_api
    app.register_blueprint(bp_api)

    # app.add_url_rule('/', endpoint='this_is_top')
    # this make url_for('this_is_top') refer to '/'

    from . import error_handle
    app.register_error_handler(404, error_handle.error_404)
    app.register_error_handler(400, error_handle.error_400)

    app.db = Database()

    return app
