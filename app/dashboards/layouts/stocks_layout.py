from dash import dcc, html
import dash_bootstrap_components as dbc

stocks_layout = html.Div([
    dbc.Row(dbc.Col(html.H1("Stocks"))),
    dbc.Row(dbc.Col(dcc.Graph(id="stocks-bar-chart"))),
    dbc.Row(dbc.Col(html.Div(id="stocks-table-container"))),
])
