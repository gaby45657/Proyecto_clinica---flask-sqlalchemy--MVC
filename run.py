# Aplicación inicial de Flask
from flask import Flask, request, render_template

# Decorador (si lo quieres usar después)
from utils.auth import login_required

# Controladores
from controllers import (
    medico_controller,
    paciente_controller,
    consulta_controller,
    cita_controller,
    usuario_controller
)

# Modelo usuario
from models.usuario_models import Usuario
from utils.auth import login_required

# Base de datos
from database import db


# =========================
# CREAR APP
# =========================
app = Flask(__name__)

app.secret_key = 'clinica123'

# Configuración DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# =========================
# INICIALIZAR DB
# =========================
db.init_app(app)

with app.app_context():
    db.create_all()
    
    # Crear admin si no existe
    admin = Usuario.query.filter_by(username='admin').first()

    if not admin:
        admin = Usuario(
            nombre='Administrador',
            username='admin',
            password='123456',
            rol='admin'
        )
        admin.save()
        print('Administrador creado')


# =========================
# BLUEPRINTS
# =========================
app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(consulta_controller.consulta_bp)
app.register_blueprint(cita_controller.cita_bp)
app.register_blueprint(usuario_controller.usuario_bp)


# =========================
# CONTEXT PROCESSOR
# =========================
@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return dict(is_active=is_active)


# =========================
# RUTA PRINCIPAL (HOME)
# =========================
# TEMPORAL PARA ENTREGA (sin login_required para evitar error 500)
@app.route('/')
@login_required
def home():
    return render_template('inicio.html')


# =========================
# EJECUCIÓN LOCAL
# =========================
if __name__ == '__main__':
    app.run(debug=True)