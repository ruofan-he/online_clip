from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    g,
    session,
    current_app
)
from ..database.db import Database

bp = Blueprint('top', __name__)

@bp.route('/index')     # multiple routing
@bp.route('/')          # url_for('top.index') refer to '/', e.g. the last bp.route('some_url')
def index():            # url_for('top.this_func_name') this_func_name = index
    db : Database = current_app.db
    entry_list = db.get_entry(3)
    return render_template('index.html', entry_list=entry_list)
