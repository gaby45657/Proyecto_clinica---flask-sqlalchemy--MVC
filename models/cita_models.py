from database import db


class Cita(db.Model):

    __tablename__ = 'citas'
    id_cita = db.Column( db.Integer, primary_key=True )
    fecha_hora = db.Column(db.DateTime,nullable=False)
    motivo = db.Column(db.String(150),nullable=False)
    estado = db.Column( db.String(20),nullable=False,default='Pendiente')
    id_medico = db.Column(db.Integer,db.ForeignKey('medicos.id_medico'),nullable=False)
    id_paciente = db.Column(db.Integer,db.ForeignKey('pacientes.id_paciente'),nullable=False)

    # Relaciones
    medico = db.relationship('Medico', back_populates='citas')
    paciente = db.relationship( 'Paciente', back_populates='citas' )
    
    

    def __init__(self,fecha_hora, motivo,id_medico,id_paciente,estado='Pendiente'):

        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.estado = estado
        self.id_medico = id_medico
        self.id_paciente = id_paciente

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cita.query.all()

    @staticmethod
    def get_by_id(id_cita):
        return Cita.query.get(id_cita)

    def update(
        self,
        fecha_hora=None,
        motivo=None,
        estado=None,
        id_medico=None,
        id_paciente=None
    ):

        if fecha_hora:
            self.fecha_hora = fecha_hora

        if motivo:
            self.motivo = motivo

        if estado:
            self.estado = estado

        if id_medico:
            self.id_medico = id_medico

        if id_paciente:
            self.id_paciente = id_paciente

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()