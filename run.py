from app import create_app
from views.GastoComunView import gasto_comun_blueprint

app = create_app()
app.register_blueprint(gasto_comun_blueprint)

if __name__ == '__main__':
    app.run(debug=True)