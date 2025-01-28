import pandas as pd
from dash.dependencies import Input, Output
from app.crud import get_market_summary
import plotly.express as px

def register_summary_callbacks(app):
    @app.callback(
        [Output("line-chart-amount", "figure"),
         Output("line-chart-operations", "figure")],
        [Input("date-picker-range", "start_date"),
         Input("date-picker-range", "end_date"),
         Input("operation-slider", "value")]
    )
    def update_summary(start_date, end_date, operation_range):
        # Obtener datos de la base de datos
        data = get_market_summary()

        if not data:
            return {}, {}

        df = pd.DataFrame(data)

        # Filtro por rango de fechas
        if start_date and end_date:
            df = df[(df["created_at"] >= start_date) & (df["created_at"] <= end_date)]

        # Gráfico de monto efectivo (afectado por rango de fechas)
        fig_amount = px.line(
            df, x="created_at", y="monto_efectivo",
            title="Evolución del Monto Efectivo en el Tiempo",
            labels={"created_at": "Fecha", "monto_efectivo": "Monto Efectivo (Bs.)"}
        )

        # Gráfico de operaciones (afectado por rango de fechas y rango de operaciones)
        if operation_range:
            df_operations = df[df["operaciones"] <= operation_range[1]]
        else:
            df_operations = df

        fig_operations = px.line(
            df_operations, x="created_at", y="operaciones",
            title="Evolución de Operaciones en el Tiempo",
            labels={"created_at": "Fecha", "operaciones": "Operaciones"}
        )

        return fig_amount, fig_operations
