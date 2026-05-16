

# Aplicacion inicial de Flask
from flask import Flask, request, render_template,session
from utils.auth import login_required


# Controladores
from controllers import medico_controller
from controllers import paciente_controller
from controllers import consulta_controller
from controllers import cita_controller
from controllers import usuario_controller

# Modelo usuario
from models.usuario_models import Usuario

# Base de datos
from database import db

# Crear aplicación
app = Flask(__name__)

app.secret_key = 'clinica123'

# Configuración DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB
db.init_app(app)

# Registrar blueprints
app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(consulta_controller.consulta_bp)
app.register_blueprint(cita_controller.cita_bp)
app.register_blueprint(usuario_controller.usuario_bp)


# Context processor navbar activo
@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return dict(is_active=is_active)


# Ruta inicio
@app.route('/')
@login_required
def home():
    return render_template('inicio.html')


# Ejecutar aplicación
if __name__ == '__main__':

    with app.app_context():

        # Crear tablas
        db.create_all()

        # Crear admin si no existe
        admin = Usuario.query.filter_by(
            username='admin'
        ).first()

        if not admin:
            admin = Usuario(
                nombre='Administrador',
                username='admin',
                password='123456',
                rol='admin'
            )

            admin.save()
            print('Administrador creado')

    app.run(debug=True)