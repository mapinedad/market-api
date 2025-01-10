from dash import Dash, html
from starlette.middleware.wsgi import WSGIMiddleware
from fastapi import FastAPI
from app.dashboards.summary_dashboard import summary_dashboard
from app.dashboards.stocks_dashboard import stocks_dashboard

def create_dash_app():
    app = Dash(__name__, requests_pathname_prefix="/dash/")
    app.layout = html.Div([
        summary_dashboard(),
        html.Hr(),
        stocks_dashboard(),
    ])
    return app

def init_dash(fastapi_app: FastAPI):
    dash_app = create_dash_app()
    fastapi_app.mount("/dash", WSGIMiddleware(dash_app.server))