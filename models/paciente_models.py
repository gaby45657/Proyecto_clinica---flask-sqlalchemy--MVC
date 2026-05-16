# Modelo para la tabla de pacientes

# creacion de la clase que va a asociar a la tabla de pacientes
from database import db

# creamos la clase que representa a la tabla de usuarios
class Paciente(db.Model):
    #nombre de la tabla en la base de datos
    __tablename__ = 'pacientes'
    #propiedades de la clase que se asocian a las columnas de la tabla
    id_paciente= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(40), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    # Relaciones
    # cada consulta pertenece a un paciente
    # 1:N un paciente puede tener muchas cconsultas
    # consultas = db.relationship('Consulta', back_populates='paciente')
    consultas = db.relationship('Consulta',back_populates='paciente', cascade='all, delete-orphan')
    
    # Un paciente puede tener muchas citas
    #citas = db.relationship( 'Cita',back_populates='paciente')
    citas = db.relationship('Cita', back_populates='paciente',cascade='all, delete-orphan')
    
    # Relaciones
    

    
    
   
    
    
    
    
    
    # metodo constructor para crear un nuevo peciente
    #self hace refereccia a la misma a clase    
    def __init__(self, nombre, edad, direccion, telefono):
        # asociar a cada una de las  propiedades los parametros que 
        # se reciben al crear un nuevo usuario
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    #crearemos un metodo para guardar paciente en la base de datos
    def save(self):
        # se agrega al paciente la sesion de la base de datos
        db.session.add(self)
        # se confirma la transaccion
        db.session.commit()
    
    # metodo que permita devolver todos los pacientes de la tabla de pacientes
    @staticmethod
    def get_all():
        # se utiliza el metodo query.all() para devolver todos los pacientes
        return Paciente.query.all()
    
    # devulve un paciente por su id
    @staticmethod
    def get_by_id(id_paciente):
        # se utiliza el metodo query.get() para devolver un usuario por su id
        return Paciente.query.get(id_paciente)
    
    # Funcion para actualizar
    def update(self, nombre=None, edad=None, direccion=None, telefono=None):
        # verificamos si se recibieron nuevos valores para cada uno de los campos 
        # y se actualizan
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
        # se confirma la transaccion
        db.session.commit()

    def delete(self):
        # se elimina el paciente de la sesion de la base de datos
        db.session.delete(self)
        # se confirma la transaccion
        db.session.commit()