from app.database import get_connection
import logging

def insert_market_summary(data):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO market_summary (operaciones, titulos_negociados, monto_efectivo, hora_24)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (data["operaciones"], data["titulos_negociados"], data["monto_efectivo"], data["hora_24"]))
    connection.commit()
    cursor.close()
    connection.close()

def insert_stocks(data):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        logging.info("Conexión exitosa a la base de datos.")

        query = """
        INSERT INTO stocks (nombre, simbolo, ultimo_precio, monto_efectivo, variacion, titulos_negociados)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(query, [
            (stock["nombre"], stock["simbolo"], stock["ultimo_precio"], stock["monto_efectivo"], stock["variacion"], stock["titulos_negociados"])
            for stock in data
        ])

        connection.commit()
        cursor.close()
        connection.close()
        logging.info("Datos insertados correctamente.")
    except Exception as e:
        logging.error(f"Error al insertar los datos: {e}")