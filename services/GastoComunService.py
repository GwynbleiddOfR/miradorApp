from models.GastoComunModel import GastoComun, db
from models.DepartamentoModel import Departamento
from datetime import datetime

class GastoComunService: 
    @staticmethod
    def crear_gasto_comun(mes, año, monto_base):
        # Crear un gasto común para cada departamento en el mes/año indicado
        departamentos = Departamento.query.all()
        periodo = f"{año}-{mes:02}"
        for dep in departamentos:
            gasto = GastoComun(
                departamento_id=dep.id,
                monto=monto_base,
                periodo=periodo
            )
            db.session.add(gasto)
        db.session.commit()
        return f"Gastos comunes generados para {periodo}"
    
    @staticmethod
    def pagar_gasto_comun(departamento_numero, periodo, fecha_pago):
        # Obtener el gasto común pendiente
        gasto = GastoComun.query.join(Departamento).filter(
            Departamento.numero == departamento_numero,
            GastoComun.periodo == periodo,
            GastoComun.pagado == False
        ).first()

        if gasto:
            gasto.pagado = True
            gasto.fecha_pago = fecha_pago
            db.session.commit()
            return {
                "mensaje": "Pago registrado exitosamente",
                "detalle": gasto.serialize()
            }
        else:
            return {"mensaje": "Pago duplicado o gasto ya registrado como pagado"}

    @staticmethod
    def obtener_gastos_pendientes(hasta_mes, hasta_año):
        periodo_final = f"{hasta_año}-{hasta_mes:02}"
        gastos_pendientes = GastoComun.query.filter(
            GastoComun.pagado == False,
            GastoComun.periodo <= periodo_final
        ).order_by(GastoComun.periodo.asc()).all()

        if not gastos_pendientes:
            return {"mensaje": "Sin montos pendientes"}
        
        return {"pendientes": [gasto.serialize() for gasto in gastos_pendientes]}