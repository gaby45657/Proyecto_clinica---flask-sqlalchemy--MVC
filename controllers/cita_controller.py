# Controlador para las operaciones relacionadas con las citas

from flask import request, redirect, url_for, Blueprint
from datetime import datetime
from views import paciente_view
from utils.auth import login_required





# Modelos
from models.medico_models import Medico
from models.paciente_models import Paciente
from models.cita_models import Cita

# Vista
from views import cita_view

# Blueprint
cita_bp = Blueprint('cita',__name__, url_prefix='/citas')


# LISTAR CITAS
@cita_bp.route('/')
@login_required
def index():
    citas = Cita.get_all()
    return cita_view.list(citas)


# CREAR CITA
@cita_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():

    if request.method == 'POST':

        fecha_hora_str = request.form['fecha_hora']
        motivo = request.form['motivo']
        estado = request.form['estado']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        # Convertir string a datetime
        fecha_hora = datetime.strptime(
            fecha_hora_str,
            '%Y-%m-%dT%H:%M'
        )

        # Crear cita
        cita = Cita(
            fecha_hora=fecha_hora,
            motivo=motivo,
            estado=estado,
            id_medico=id_medico,
            id_paciente=id_paciente
        )

        cita.save()

        return redirect(url_for('cita.index'))

    # GET
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    return cita_view.create(
        medicos,
        pacientes
    )


# EDITAR CITA
@cita_bp.route('/edit/<int:id_cita>', methods=['GET', 'POST'])
@login_required
def edit(id_cita):

    cita = Cita.get_by_id(id_cita)

    if request.method == 'POST':

        fecha_hora_str = request.form['fecha_hora']
        motivo = request.form['motivo']
        estado = request.form['estado']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        # Convertir string a datetime
        fecha_hora = datetime.strptime(
            fecha_hora_str,
            '%Y-%m-%dT%H:%M'
        )

        # Actualizar cita
        cita.update(
            fecha_hora=fecha_hora,
            motivo=motivo,
            estado=estado,
            id_medico=id_medico,
            id_paciente=id_paciente
        )

        return redirect(url_for('cita.index'))

    # GET
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    return cita_view.edit(
        cita,
        medicos,
        pacientes
    )


# ELIMINAR CITA
@cita_bp.route('/delete/<int:id_cita>')
@login_required
def delete(id_cita):
    cita = Cita.get_by_id(id_cita)
    cita.delete()
    return redirect(url_for('cita.index') )