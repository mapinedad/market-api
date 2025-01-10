from fastapi import FastAPI
from app.routes import market
from fastapi.routing import APIRoute
from app.dashboards.dash_integration import init_dash

app = FastAPI(title="BCV Market API")

# Inicializar Dash
init_dash(app)

# Registrar las rutas con el prefijo "/api/v1"
app.include_router(market.router, prefix="/api/v1", tags=["Market"])

@app.get("/")
def list_routes():
    routes = []
    for route in app.routes:
        if isinstance(route, APIRoute):
            routes.append({
                "path": route.path,
                "methods": list(route.methods)
            })

    # Agregar la ruta del dashboard
    routes.append({
        "path": "/dash",
        "methods": ["GET"],  # Puedes ajustar los métodos según sea necesario
        "description": "Dashboard route"
    })
    return routes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)