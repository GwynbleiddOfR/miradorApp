from app import db

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), unique=True, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id, 
            'numero': self.numero
        }