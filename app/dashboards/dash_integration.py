from dash import Dash, html
from starlette.middleware.wsgi import WSGIMiddleware
from fastapi import FastAPI
from app.dashboards.layouts.summary_layout import summary_layout
from app.dashboards.layouts.stocks_layout import stocks_layout
from app.dashboards.callbacks.summary_callbacks import register_summary_callbacks
from app.dashboards.callbacks.stocks_callbacks import register_stocks_callbacks

def create_dash_app():
    app = Dash(__name__, requests_pathname_prefix="/dash/")
    app.layout = html.Div([
        summary_layout,
        html.Hr(),
        stocks_layout,
    ])
    register_summary_callbacks(app)
    register_stocks_callbacks(app)
    return app

def init_dash(fastapi_app: FastAPI):
    dash_app = create_dash_app()
    fastapi_app.mount("/dash", WSGIMiddleware(dash_app.server))
