from bs4 import BeautifulSoup
import requests
import logging
from app.config.settings import MARKET_SUMMARY_URL, MARKET_STOCKS_ENDPOINT, HEADERS
from app.utils.parsers import parse_number_stocks, parse_number_summary


# Configuración básica de logging
logging.basicConfig(level=logging.INFO)


# Scraping del resumen del mercado
def scrape_market_summary():
    try:
        response = requests.get(MARKET_SUMMARY_URL, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        table_summary = soup.find("table", {"class": "table-hover"})

        if not table_summary:
            raise ValueError("No se encontró la tabla de resumen del mercado.")

        rows = table_summary.find_all("tr")
        if len(rows) < 2:
            raise ValueError("La tabla de resumen del mercado está vacía o tiene formato incorrecto.")

        cols = rows[1].find_all("td")
        if len(cols) < 5:
            raise ValueError(f"Fila con datos incompletos: se esperaban 5 columnas, pero solo se encontraron {len(cols)}.")

        data = {
            "operaciones": parse_number_summary(cols[0].text.strip(), int),
            "titulos_negociados": parse_number_summary(cols[1].text.strip(), int),
            "monto_efectivo": parse_number_summary(cols[2].text.strip(), float),
            "hora_24": cols[4].text.strip()
        }
        logging.info("Resumen del mercado obtenido correctamente.")
        return data
    except Exception as e:
        logging.error(f"Error al obtener el resumen del mercado: {e}")
        return None

# Scraping de datos de acciones
def scrape_market_stocks():
    """Obtiene los datos del endpoint y los transforma para la base de datos."""
    try:
        response = requests.get(MARKET_STOCKS_ENDPOINT, headers=HEADERS)
        response.raise_for_status()
        
        # Parsear JSON
        data = response.json()
        if not isinstance(data, list) or not data:
            raise ValueError("El endpoint devolvió datos inválidos o vacíos.")

        # Transformar datos para la base de datos
        stocks = []
        for stock in data:
            stocks.append({
                "nombre": stock["DESC_SIMB"],
                "simbolo": stock["COD_SIMB"],
                "ultimo_precio": parse_number_stocks(stock["PRECIO"], float, 0.0),
                "monto_efectivo": parse_number_stocks(stock["MONTO_EFECTIVO"], float, 0.0),
                "variacion": parse_number_stocks(stock["VAR_ABS"], float, 0.0),
                "titulos_negociados": parse_number_stocks(stock["VOLUMEN"], int, 0),
            })
        logging.info(f"{len(stocks)} registros obtenidos del endpoint.")
        return stocks
    except Exception as e:
        logging.error(f"Error al obtener los datos del mercado: {e}")
        return []


# Probar funciones de scraping
if __name__ == "__main__":
    logging.info("Iniciando pruebas de scraping...")

    summary = scrape_market_summary()
    if summary:
        logging.info(f"Resumen del mercado: {summary}")
    else:
        logging.warning("No se pudo obtener el resumen del mercado.")

    stocks = scrape_market_stocks()
    if stocks:
        logging.info(f"Primeras 3 acciones obtenidas: {stocks[:3]}")
    else:
        logging.warning("No se encontraron datos de acciones.")
