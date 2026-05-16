# Controlador para las operaciones relacionadas con los usuarios
# se importan las funciones necesarias para manejar las solicitudes HTTP, redireccionar y generar URLs
from flask import request, redirect, url_for, Blueprint
from datetime import datetime
from models.medico_models import Medico
from models.paciente_models import Paciente
from models.consulta_models import Consulta
from utils.auth import login_required
from views import consulta_view

consulta_bp = Blueprint('consulta', __name__,url_prefix='/consultas')

@consulta_bp.route('/')
@login_required
def index():
    consultas = Consulta.get_all()
    return consulta_view.list(consultas)

@consulta_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        fecha = datetime.strptime(fecha_str,'%Y-%m-%dT%H:%M')
        consulta = Consulta(fecha=fecha,diagnostico=diagnostico, tratamiento=tratamiento,id_medico=id_medico, id_paciente=id_paciente)
        consulta.save()
        return redirect(url_for('consulta.index'))
    # Si no es post si es get
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return consulta_view.create(medicos, pacientes)

@consulta_bp.route('/edit/<int:id_consulta>', methods=['GET', 'POST'])
@login_required
def edit(id_consulta):
    consulta = Consulta.get_by_id(id_consulta)
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        #fecha = datetime.strptime(fecha_str,'%Y-%m-%d').date()
        fecha = datetime.strptime(fecha_str,'%Y-%m-%dT%H:%M')
        # actualizar
        consulta.update(fecha=fecha,diagnostico=diagnostico, tratamiento=tratamiento,id_medico=id_medico, id_paciente=id_paciente)
        return redirect(url_for('consulta.index'))
    # si es get
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return consulta_view.edit(consulta, medicos, pacientes)

@consulta_bp.route('/delete/<int:id_consulta>')
@login_required
def delete(id_consulta):
    consulta = Consulta.get_by_id(id_consulta)
    consulta.delete()
    return redirect(url_for('consulta.index'))


