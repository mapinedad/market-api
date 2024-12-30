from bs4 import BeautifulSoup
import requests


# URL de la página
URL = "https://www.bolsadecaracas.com/resumen-mercado/"


def scrape_market_summary():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Resumen general del mercado
    table_summary = soup.find("table", {"class": "table-hover"})
    rows = table_summary.find_all("tr")

    summary = []
    for row in rows[1:]:  # Omitir el encabezado
        cols = row.find_all("td")
        summary.append({
            "operaciones": cols[0].text.strip(),
            "titulos_negociados": cols[1].text.strip(),
            "monto_efectivo": cols[2].text.strip(),
            "titulos_en": cols[3].text.strip(),
            "hora_24": cols[4].text.strip()
        })

    return summary

data = scrape_market_summary()
print(data)