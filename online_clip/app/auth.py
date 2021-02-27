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
import functools

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
        success, detail = db.register_user(user_id, pw_hash, first_name, last_name)
        print(success)
        if success:
            session.permanent = True
            session['user_id'] = user_id
            session['account_key'] = detail.get('account_key')
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
        auth_result, detail = db.auth_user(user_id, pw_hash)
    else:
        return abort(400)

    if auth_result:
        session.permanent = True
        session['user_id'] = user_id
        session['account_key'] = detail.get('account_key')
        session.modified = True
        return redirect(url_for('top.index'))
    else:
        return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    session.pop('user_id',None)
    session.modified = True
    return redirect(url_for('top.index'))



# register function that run before the view function, nomatter what url
@bp.before_app_request
def before():
    print('before_app_request')
    pass
    # g.user = ~~~~
    # db.~~(~~)
    # etc.


# decorator, it can be used to decorate vue_func if needed
def login_required(view_func):
    @functools.wraps(view_func) # this is needed in order to move view_func.__name__ to wrapped_view_func.__name__
    def wrapped_view_func(*args, **kwargs):
        # login process etc.
        # if not is_login:
        # return redirect(url_for('auth.login'))
        return view_func(*args, **kwargs)
    return wrapped_view_func