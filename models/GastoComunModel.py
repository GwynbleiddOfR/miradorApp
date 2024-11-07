from app import db

class GastoComun(db.Model):
    __tablename__ = 'gastos_comunes'

    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False)
    periodo = db.Column(db.String(7), nullable=False)  # Formato 'YYYY-MM'
    pagado = db.Column(db.Boolean, default=False)
    fecha_pago = db.Column(db.Date, nullable=True)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)

    departamento = db.relationship('Departamento', backref='gastos_comunes', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'departamento': self.departamento.numero,
            'monto': self.monto,
            'periodo': self.periodo,
            'pagado': self.pagado,
            'fecha_pago': self.fecha_pago.strftime('%Y-%m-%d') if self.fecha_pago else None
        }