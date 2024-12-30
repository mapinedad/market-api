import requests

# URL de la página
URL = "https://www.bolsadecaracas.com/resumen-mercado/"

response = requests.get(URL)
if "ALZ.B" in response.text:  # Cambia "ABC.A" por un símbolo de empresa visible en la tabla
    print("Los datos están presentes en el HTML inicial.")
else:
    print("Los datos se generan dinámicamente.")
