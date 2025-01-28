from dash import dcc, html
import dash_bootstrap_components as dbc

summary_layout = html.Div([
    dbc.Row([
        dbc.Col(dcc.DatePickerRange(
            id="date-picker-range",
            display_format="YYYY-MM-DD",
            start_date_placeholder_text="Inicio",
            end_date_placeholder_text="Fin",
        ), width=6),
        dbc.Col(dcc.RangeSlider(
            id="operation-slider",
            min=0, max=1000, step=10,
            marks={i: str(i) for i in range(0, 1001, 100)},
            tooltip={"placement": "bottom", "always_visible": True},
        ), width=6),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id="line-chart-amount"), width=6),
        dbc.Col(dcc.Graph(id="line-chart-operations"), width=6),
    ]),
])
