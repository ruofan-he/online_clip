from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    g,
    session,
    current_app,
    redirect,
    abort)
import os


bp = Blueprint('spa', __name__,static_url_path='/spa', static_folder='./dist')

@bp.route('/spa')
def return_app():
    return redirect(url_for('spa.static', filename='index.html'))

