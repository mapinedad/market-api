import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from app.crud import get_market_summary

def summary_dashboard():
    # Obtener los datos desde la base de datos
    data = get_market_summary()

    if data:
        # Crear el DataFrame
        df = pd.DataFrame(data)
        
        # Gráfico de líneas: Evolución del monto efectivo en el tiempo
        fig_line = px.line(
            df, x="created_at", y="monto_efectivo", 
            title="Evolución del Monto Efectivo en el Tiempo",
            labels={"created_at": "Fecha", "monto_efectivo": "Monto Efectivo (Bs.)"}
        )

        # Gráfico de líneas: Evolución de títulos negociados
        fig_titulos = px.line(
            df, x="created_at", y="titulos_negociados",
            title="Evolución de Títulos Negociados en el Tiempo",
            labels={"created_at": "Fecha", "titulos_negociados": "Títulos Negociados"}
        )

    else:
        fig_line = {}
        fig_titulos = {}

    return html.Div([
        dbc.Row(dbc.Col(html.H1("Resumen del Mercado"))),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_line), width=6),
            dbc.Col(dcc.Graph(figure=fig_titulos), width=6),
        ]),
    ])