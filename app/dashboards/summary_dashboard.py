from dash import html
from app.dashboards.layout_summary_dashboard import create_summary_layout
from app.dashboards.callbacks_summary_dashboard import register_summary_callbacks

def summary_dashboard(app):
    layout = create_summary_layout()
    register_summary_callbacks(app)
    return layout