import mysql.connector
import logging
from mysql.connector import pooling

DATABASE_CONFIG = {
    "host": "localhost",
    "user": "mapinedad",
    "password": "RRHHS3n1a72024*-2",
    "database": "bcv_market",
    "charset": "utf8mb4",  # Charset compatible
    "collation": "utf8mb4_general_ci",  # Forzar la collation
}

connection_pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                              pool_size=5,
                                              **DATABASE_CONFIG)

def get_connection():
    return connection_pool.get_connection()

def execute_query(query, params=None, many=False):
    """
    Ejecuta una consulta en la base de datos.
    :param query: Consulta SQL a ejecutar.
    :param params: Parámetros para la consulta.
    :param many: Booleano, si se deben ejecutar múltiples parámetros (usualmente para `executemany`).
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()
        logging.info("Conexión exitosa a la base de datos.")

        if many and params:
            cursor.executemany(query, params)
        elif params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        connection.commit()
        cursor.close()
        connection.close()
        logging.info("Consulta ejecutada correctamente.")
    except Exception as e:
        logging.error(f"Error al ejecutar la consulta: {e}")

def fetch_query(query):
    """
    Ejecuta una consulta de tipo SELECT y devuelve los resultados.
    :param query: Consulta SQL de tipo SELECT.
    """
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        logging.info("Conexión exitosa a la base de datos.")

        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        connection.close()
        return data
    except Exception as e:
        logging.error(f"Error al obtener los datos: {e}")
        return []