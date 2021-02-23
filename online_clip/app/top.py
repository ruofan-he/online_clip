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

from ..database import read_element

bp = Blueprint('top', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    db : Database = current_app.db
    entry = db.get_entry(3)
    return render_template('base.html', entry=entry)
