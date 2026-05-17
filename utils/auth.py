from flask import session, redirect, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        # Si NO existe usuario en sesión
        if 'usuario_id' not in session:
            return redirect(url_for('usuario.login'))

        return f(*args, **kwargs)

    return decorated_function

