# Controlador para las operaciones relacionadas con los pacientes
# se importan las funciones necesarias para manejar las solicitudes HTTP, redireccionar y generar URLs
from flask import request, redirect, url_for, Blueprint,render_template
from models.paciente_models import Paciente
from views import paciente_view
from utils.auth import login_required
paciente_bp = Blueprint('paciente', __name__,url_prefix='/pacientes')

@paciente_bp.route('/')
@login_required
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        paciente = Paciente(nombre, edad, direccion, telefono)
        paciente.save()
        return redirect(url_for('paciente.index'))
    return paciente_view.create()

@paciente_bp.route('/edit/<int:id_paciente>', methods=['GET', 'POST'])
@login_required
def edit(id_paciente):
    paciente = Paciente.get_by_id(id_paciente)
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        paciente.update(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)
        return redirect(url_for('paciente.index'))
    # si es get
    return paciente_view.edit(paciente)

@paciente_bp.route('/delete/<int:id_paciente>')
@login_required
def delete(id_paciente):
    paciente = Paciente.get_by_id(id_paciente)
    paciente.delete()
    return redirect(url_for('paciente.index'))

# HISTORIAL MEDICO
@paciente_bp.route('/historial/<int:id_paciente>')
@login_required
def historial(id_paciente):
    paciente = Paciente.get_by_id(id_paciente)
    return render_template(
        'pacientes/historial.html',
        paciente=paciente
    )

