from app.dashboards.layout_stocks_dashboard import create_stocks_layout
from app.dashboards.callbacks_stocks_dashboard import register_stocks_callbacks

def stocks_dashboard(app):
    app.layout = create_stocks_layout()
    register_stocks_callbacks(app)
