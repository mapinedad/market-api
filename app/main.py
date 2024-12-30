from fastapi import FastAPI
from app.routes import market

app = FastAPI(title="BCV Market API")

# Registrar las rutas con el prefijo "/api/v1"
app.include_router(market.router, prefix="/api/v1", tags=["Market"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)