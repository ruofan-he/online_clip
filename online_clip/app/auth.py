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

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET','POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        user_id = request.form.get('user_id', None)
        pw_hash = request.form.get('pw_hash', None)
        first_name = request.form.get('first_name', None)
        last_name = request.form.get('last_name', None)
        db : Database = current_app.db
        success = db.register_user(user_id, pw_hash, first_name, last_name)
        print(success)
        if success:
            session.permanent = True
            session['user_id'] = user_id
            session.modified = True
            return redirect(url_for('top.index'))
        else:
            return redirect(url_for('auth.registration'))
        
    else:
        return abort(400)
        


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user_id = request.form.get('user_id', None)
        pw_hash = request.form.get('pw_hash', None)
        db : Database = current_app.db
        auth_result = db.auth_user(user_id, pw_hash)
    else:
        return abort(400)

    if auth_result:
        session.permanent = True
        session['user_id'] = user_id
        session.modified = True
        return redirect(url_for('top.index'))
    else:
        return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    session.pop('user_id',None)
    session.modified = True
    return redirect(url_for('top.index'))

@bp.route('/userpage')
def userpage():
    return render_template('base.html')
