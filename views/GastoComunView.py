from flask import Blueprint, request, jsonify
from controllers.GastoComunController import GastoComunController
from datetime import datetime

gasto_comun_blueprint = Blueprint('gasto_comun_blueprint', __name__)

@gasto_comun_blueprint.route('/gastos/generar', methods=['POST'])
def crear_gasto_comun():
    data = request.get_json()
    mes = data.get('mes')
    año = data.get('año')
    monto_base = data.get('monto_base')
    mensaje = GastoComunController.crear_gasto_comun_controller(mes, año, monto_base)
    return jsonify({"mensaje": mensaje}), 201

@gasto_comun_blueprint.route('/gastos/pagar', methods=['POST'])
def pagar_gasto_comun():
    data = request.get_json()
    departamento_numero = data.get('departamento')
    periodo = data.get('periodo')
    fecha_pago = datetime.strptime(data.get('fecha_pago'), '%Y-%m-%d')
    resultado = GastoComunController.pagar_gasto_comun_controller(departamento_numero, periodo, fecha_pago)
    return jsonify(resultado), 200

@gasto_comun_blueprint.route('/gastos/pendientes', methods=['GET'])
def obtener_gastos_pendientes():
    hasta_mes = int(request.args.get('mes'))
    hasta_año = int(request.args.get('año'))
    resultado = GastoComunController.obtener_gastos_pendientes_controller(hasta_mes, hasta_año)
    return jsonify(resultado), 200