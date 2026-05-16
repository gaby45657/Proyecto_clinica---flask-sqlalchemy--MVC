# Controlador para las operaciones relacionadas con los medicos
# se importan las funciones necesarias para manejar las solicitudes HTTP, redireccionar y generar URLs
from flask import request, redirect, url_for, Blueprint
from models.medico_models import Medico
from views import medico_view
from utils.auth import login_required
medico_bp = Blueprint('medico', __name__,url_prefix='/medicos')

@medico_bp.route('/')
@login_required
def index():
    medicos = Medico.get_all()
    return medico_view.list(medicos)

@medico_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']
        medico = Medico(nombre, especialidad, telefono, correo)
        medico.save()
        return redirect(url_for('medico.index'))
    return medico_view.create()

@medico_bp.route('/edit/<int:id_medico>', methods=['GET', 'POST'])
@login_required
def edit(id_medico):
    medico = Medico.get_by_id(id_medico)
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']
        medico.update(nombre=nombre, especialidad=especialidad, telefono=telefono, correo=correo)
        return redirect(url_for('medico.index'))
    # si es get
    return medico_view.edit(medico)

@medico_bp.route('/delete/<int:id_medico>')
@login_required
def delete(id_medico):
    medico = Medico.get_by_id(id_medico)
    medico.delete()
    return redirect(url_for('medico.index'))


