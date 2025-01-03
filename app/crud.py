from app.database import get_connection, execute_query, fetch_query
import logging


def insert_market_summary(data):
    query = """
    INSERT INTO market_summary (operaciones, titulos_negociados, monto_efectivo, hora_24)
    VALUES (%s, %s, %s, %s)
    """
    params = (data["operaciones"], data["titulos_negociados"], data["monto_efectivo"], data["hora_24"])
    execute_query(query, params)

def insert_stocks(data):
    query = """
    INSERT INTO stocks (nombre, simbolo, ultimo_precio, monto_efectivo, variacion, titulos_negociados)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = [
        (stock["nombre"], stock["simbolo"], stock["ultimo_precio"], stock["monto_efectivo"], stock["variacion"], stock["titulos_negociados"])
        for stock in data
    ]
    execute_query(query, params, many=True)

def get_market_summary():
    query = "SELECT * FROM market_summary"
    return fetch_query(query)

def get_stocks():
    query = "SELECT * FROM stocks"
    return fetch_query(query)
