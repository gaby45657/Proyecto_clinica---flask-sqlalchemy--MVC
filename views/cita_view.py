from flask import render_template

# Lista de citas
def list(citas):
    return render_template('citas/index.html',citas=citas )

# Formulario para crear cita
def create(medicos, pacientes):
    return render_template('citas/create.html',medicos=medicos,pacientes=pacientes)

# Formulario para editar cita
def edit(cita, medicos, pacientes):
    return render_template('citas/edit.html',cita=cita, medicos=medicos,pacientes=pacientes)