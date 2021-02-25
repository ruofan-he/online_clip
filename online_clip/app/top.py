from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    g,
    session,
    current_app,
    redirect,
    abort
)
from ..database.db import Database

bp = Blueprint('top', __name__)

@bp.route('/index')     # multiple routing
@bp.route('/')          # url_for('top.index') refer to '/', e.g. the last bp.route('some_url')
def index():            # url_for('top.this_func_name') this_func_name = index
    db : Database = current_app.db
    account_key = None
    if session.get('user_id') and session.get('account_key'):
        account_key = int(session.get('account_key'))
    entry_list = db.get_recent_entry(10, public=True, account_key=account_key)
    return render_template('index.html', entry_list=entry_list)

@bp.route('/userpage', methods=['GET','POST'])
def userpage():
    if session.get('account_key') is None:
        return redirect(url_for('auth.login'))

    db : Database = current_app.db
    account_key = session.get('account_key')

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        db.append_entry(account_key)
    else:
        return abort(404)

    entry_list = db.get_recent_entry(100, public=False, account_key=account_key)
    return render_template('userpage.html', entry_list=entry_list)
