# PROTOTIPO FUNCIONAL PARA ASIGNATURA DE ARQUITECTURA

## Instrucciones

1. **Eliminar la base de datos existente:**
   - Borrar el archivo `gastos_comunes.db` ubicado en la carpeta `instance`.

2. **Ejecutar el servidor:**
   ```bash
   python run.py
   
3. **Abrir la base de datos en SQLite:**

Presionar `Ctrl + Shift + P`.
Buscar `SQLite: Open Database`, hacer clic y seleccionar `instance\gastos_comunes.db`.

4. **Insertar departamentos:**

Abrir el archivo `insertsdepartamento.sql` ubicado en la carpeta `instance`.
Hacer clic derecho y seleccionar `Run Query`.
En caso de que no funcione:
Seleccionar todos los inserts manualmente y hacer clic en `Run Selected Query`.
Si aparece el error **UNIQUE constraint failed: departamentos.id**, consulta la tabla departamentos para verificar si ya hay datos insertados.

## Probar APP con Postman

1. **GENERAR GASTOS COMUNES**

POST http://127.0.0.1:5000/gastos/generar

{
  "mes": 10,
  "año": 2024,
  "monto_base": 50000
}

2. **PAGAR GASTO COMÚN**

POST http://127.0.0.1:5000/gastos/pagar

{
  "departamento": "100",
  "periodo": "2024-10",
  "fecha_pago": "2024-11-03"
}

3. **OBTENER GASTOS PENDIENTES**

GET http://127.0.0.1:5000/gastos/pendientes?mes=10&año=2024