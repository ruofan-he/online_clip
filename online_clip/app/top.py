from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    g,
    session
)

bp = Blueprint('top', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('base.html')
