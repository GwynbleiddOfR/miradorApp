from services.GastoComunService import GastoComunService

class GastoComunController:
    @staticmethod
    def crear_gasto_comun_controller(mes, año, monto_base):
        return GastoComunService.crear_gasto_comun(mes, año, monto_base)

    @staticmethod
    def pagar_gasto_comun_controller(departamento_numero, periodo, fecha_pago):
        return GastoComunService.pagar_gasto_comun(departamento_numero, periodo, fecha_pago)

    @staticmethod
    def obtener_gastos_pendientes_controller(hasta_mes, hasta_año):
        return GastoComunService.obtener_gastos_pendientes(hasta_mes, hasta_año)