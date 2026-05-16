# Modelo para la tabla de usuarios
# creacion de la clase que va a asociar a la tabla de usuarios
from database import db

# creamos la clase que representa a la tabla de usuarios
class Medico(db.Model):
    #nombre de la tabla en la base de datos
    __tablename__ = 'medicos'
    #propiedades de la clase que se asocian a las columnas de la tabla
    id_medico = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especialidad = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(40), nullable=False)
    # Relaciones
    # Cada consulta pertenece  a un medico 
    # 1:N Un medico pude hacer muchas consultas
    consultas = db.relationship('Consulta', back_populates='medico')
    
    # Un médico puede tener muchas citas
     #citas = db.relationship('Cita', back_populates='medico')
    citas = db.relationship('Cita',back_populates='medico',cascade='all, delete-orphan')
    # nuevo
    consultas = db.relationship('Consulta',back_populates='medico',cascade='all, delete-orphan')
    
    
    
    
    
    # metodo constructor para crear un nuevo usuario
    #self hace refereccia a la misma a clase    
    def __init__(self, nombre, especialidad, telefono, correo):
        # asociar a cada una de las  propiedades los parametros que 
        # se reciben al crear un nuevo usuario
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo

    #crearemos un metodo para guardar medico en la base de datos
    def save(self):
        # se agrega el medico a la sesion de la base de datos
        db.session.add(self)
        # se confirma la transaccion
        db.session.commit()
    
    # metodo que permita devolver todos los medicos de la tabla de medicos
    @staticmethod
    def get_all():
        # se utiliza el metodo query.all() para devolver todos los medicos
        return Medico.query.all()
    
    # devulve un medico por su id
    @staticmethod
    def get_by_id(id_medico):
        # se utiliza el metodo query.get() para devolver un usuario por su id
        return Medico.query.get(id_medico)
    
    # Funcion para actualizar
    def update(self, nombre=None, especialidad=None, telefono=None, correo=None):
        # verificamos si se recibieron nuevos valores para cada uno de los campos 
        # y se actualizan
        if nombre:
            self.nombre = nombre
        if especialidad:
            self.especialidad = especialidad
        if telefono:
            self.telefono = telefono
        if correo:
            self.correo = correo
        # se confirma la transaccion
        db.session.commit()

    def delete(self):
        # se elimina el usuario de la sesion de la base de datos
        db.session.delete(self)
        # se confirma la transaccion
        db.session.commit()