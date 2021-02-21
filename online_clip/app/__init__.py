import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    from . import top
    app.register_blueprint(top.bp)
    # app.add_url_rule('/', endpoint='this_is_top')


    from . import error_handle
    app.register_error_handler(404, error_handle.error_404)


    return app
