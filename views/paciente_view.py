
# CLIENTE_VIEW.PY

# Hace las renderizaciones de las plantillas para el paciente
from flask import render_template

# creamos las funciones que se encargan de renderizar las plantillas para el usuario

def list(pacientes):
    # se renderiza la plantilla templates/medicos/index.html y se le pasa la lista de medicos
    return render_template('pacientes/index.html', pacientes=pacientes)

# cuando se necesita crear un nuevo registro
def create():
    # se renderiza la plantilla pacientes/create.html
    return render_template('pacientes/create.html')

# cuando se necesita editar un registro existente
def edit(paciente):
    # se renderiza la plantilla usuarios/edit.html y se le pasa el usuario a editar
    return render_template('pacientes/edit.html', paciente=paciente)

#En templates se crea la carpeta usuarios que contendrá los
#  archivos que en usurio_view.py se renderizara
