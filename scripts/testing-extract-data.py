import requests

def fetch_market_data():
	url = "https://www.bolsadecaracas.com/wp-admin/admin-ajax.php?action=resumenMercadoRentaVariable"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5678.108 Safari/537.36",
        "Accept": "application/json",
	}

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()

		data = response.json()

		if isinstance(data, list) and data:
			return data
		else:
			return {"error": "No se encontraron datos validos"}
	except requests.exceptions.RequestException as e:
		return {"error": f"Error al obtener los datos: {e}"}


if __name__ == '__main__':

	print(fetch_market_data())