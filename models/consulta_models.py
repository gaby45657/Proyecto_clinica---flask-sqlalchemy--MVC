
from database import db

# creamos la clase que representa a la tabla de consultas
class Consulta(db.Model):
    #nombre de la tabla en la base de datos
    __tablename__ = 'consultas'
    #propiedades de la clase que se asocian a las columnas de la tabla
    id_consulta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    diagnostico = db.Column(db.String(150), nullable=False)
    tratamiento = db.Column(db.String(150), nullable=False)
    id_medico= db.Column(db.Integer,db.ForeignKey('medicos.id_medico'), nullable=False)
    id_paciente = db.Column(db.Integer,db.ForeignKey('pacientes.id_paciente'), nullable=False)
  
    # Relaciones
    # Un medico puede tener muchas consultas 1:N
    medico = db.relationship('Medico', back_populates='consultas')
    # Un paciente puede tener muchas consultas
    paciente = db.relationship('Paciente', back_populates='consultas')
    
    

    
  
    def __init__(self, fecha,diagnostico, tratamiento, id_medico, id_paciente):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        

   
    #crearemos un metodo para guardar el usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    
    # METODOS
    @staticmethod
    def get_all():
        # se utiliza el metodo query.all() para devolver todos los usuarios
        return Consulta.query.all()
       
    
    # devulve un usuario por su id
    @staticmethod
    def get_by_id(id_consulta):
        return Consulta.query.get(id_consulta)

    def update(self, fecha=None,diagnostico=None, tratamiento=None, id_medico=None, id_paciente=None):
        if  fecha and diagnostico and tratamiento and id_medico and id_paciente:
            self.fecha = fecha
            self.diagnostico = diagnostico
            self.tratamiento = tratamiento
            self.id_medico = id_medico
            self.id_paciente = id_paciente
        # se confirma la transaccion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()