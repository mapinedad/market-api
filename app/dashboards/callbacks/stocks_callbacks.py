import pandas as pd
from dash.dependencies import Input, Output
from app.crud import get_stocks
import plotly.express as px
from dash import html
import dash_bootstrap_components as dbc

def register_stocks_callbacks(app):
    @app.callback(
        [Output("stocks-bar-chart", "figure"),
         Output("stocks-table-container", "children")],
        [Input("date-picker-range", "start_date"),
         Input("date-picker-range", "end_date")]
    )
    def update_stocks_dashboard(start_date, end_date):
        data = get_stocks()

        if not data:
            return {}, html.Div("No hay datos disponibles.")

        df = pd.DataFrame(data)

        # Aplicar filtro de rango de fechas
        if start_date and end_date:
            df = df[(df["created_at"] >= start_date) & (df["created_at"] <= end_date)]

        # Gráfico de barras
        fig_barras = px.bar(
            df, x="nombre", y="titulos_negociados",
            title="Títulos Negociados por Stock",
            labels={"nombre": "Nombre del Stock", "titulos_negociados": "Títulos Negociados"},
        )

        # Tabla dinámica
        table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
        return fig_barras, table
