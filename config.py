class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gastos_comunes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False