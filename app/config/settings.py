# config/settings.py

# Base URL de la página de la Bolsa de Caracas
BASE_URL = "https://www.bolsadecaracas.com/"
MARKET_SUMMARY_URL = f"{BASE_URL}resumen-mercado/"
MARKET_STOCKS_ENDPOINT = f"{BASE_URL}wp-admin/admin-ajax.php?action=resumenMercadoRentaVariable"

# Headers comunes para las solicitudes HTTP
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
