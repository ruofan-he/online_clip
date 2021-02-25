from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    g,
    session,
    current_app,
    abort,
    redirect
)
from ..database.db import Database

bp = Blueprint('api', __name__)

@bp.route('/raw/<int:key>', methods=['GET'])
def get_entry(key):
    db : Database = current_app.db
    entry = db.get_entry(key)
    if entry is None:
        return abort(404)

    if not entry.is_public and session.get('account_key') != entry.account_key:
        return abort(404)
    return entry.text

        
@bp.route('/raw/<int:key>', methods=['POST'])
def update_entry(key):
    db : Database = current_app.db
    entry = db.get_entry(key)
    if entry is None:
        return abort(404)
    
    is_delete = request.headers.get('status') == 'delete'
    if is_delete:
        db.delete_entry(entry)
        return ''

    text = request.headers.get('text')
    is_public = bool(int(request.headers.get('is_public')))
    if session.get('account_key') != entry.account_key:
        return abort(400)
    entry.text = text
    entry.is_public = is_public
    db.update_entry(entry)
    return ''

