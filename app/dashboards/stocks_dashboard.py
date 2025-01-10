import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from app.crud import get_stocks

def stocks_dashboard():
    # Obtener los datos desde la base de datos
    data = get_stocks()

    if data:
        # Crear el DataFrame
        df = pd.DataFrame(data)
        
        # Gráfico de barras: Comparación de títulos negociados por stock
        fig_barras = px.bar(
            df, x="nombre", y="titulos_negociados",
            title="Títulos Negociados por Stock",
            labels={"nombre": "Nombre del Stock", "titulos_negociados": "Títulos Negociados"},
        )

        # Tabla dinámica
        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

    else:
        fig_barras = {}
        table = html.Div("No hay datos disponibles.")

    return html.Div([
        dbc.Row(dbc.Col(html.H1("Stocks"))),
        dbc.Row(dbc.Col(dcc.Graph(figure=fig_barras))),
        dbc.Row(dbc.Col(table)),
    ])