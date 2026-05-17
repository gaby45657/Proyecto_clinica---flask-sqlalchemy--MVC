from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from models.usuario_models import Usuario

usuario_bp = Blueprint(
    'usuario',
    __name__,
    url_prefix='/usuarios'
)


# LOGIN
@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.query.filter_by( username=username ).first()

        if usuario and usuario.verify_password(password):

            session['usuario_id'] = usuario.id_usuario
            session['nombre'] = usuario.nombre
            session['rol'] = usuario.rol

            return redirect(url_for('home'))

        flash('Usuario o contraseña incorrectos')

    return render_template('usuarios/login.html')


# LOGOUT
@usuario_bp.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('usuario.login'))


