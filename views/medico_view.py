# Hace las renderizaciones de las plantillas para el usuario
from flask import render_template
# creamos las funciones que se encargan de renderizar las plantillas para el usuario

def list(medicos):
    # se renderiza la plantilla templates/medicos/index.html y se le pasa la lista de medicos
    return render_template('medicos/index.html', medicos=medicos)

# cuando se necesita crear un nuevo registro
def create():
    # se renderiza la plantilla medicos/create.html
    return render_template('medicos/create.html')

# cuando se necesita editar un registro existente
def edit(medico):
    # se renderiza la plantilla usuarios/edit.html y se le pasa el usuario a editar
    return render_template('medicos/edit.html', medico=medico)

#En templates se crea la carpeta usuarios que contendrá los
#  archivos que en usurio_view.py se renderizara
