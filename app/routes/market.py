from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.scraping import scrape_market_summary, scrape_market_stocks
from app.crud import insert_market_summary, insert_stocks, get_market_summary, get_stocks

router = APIRouter()

@router.post("/market/summary")
async def store_market_summary():
    data = scrape_market_summary()
    insert_market_summary(data)
    return {"message": "Market summary stored successfully"}

@router.post("/market/stocks")
async def store_market_stocks():
    """Obtiene datos del mercado y los inserta en la base de datos."""
    data = scrape_market_stocks()
    if not data:
        return {"message": "No se encontraron datos para insertar."}
    
    try:
        insert_stocks(data)
        return {"message": "Market stocks stored successfully", "records_inserted": len(data)}
    except Exception as e:
        return {"message": f"Error al insertar los datos: {e}"}


# Nuevas rutas GET
@router.get("/market/summary")
async def fetch_market_summary():
    """Obtiene el resumen del mercado desde la base de datos."""
    data = get_market_summary()

    if data:
        return {"market_summary": data}

    return {"message": "No se encontraron datos de resumen del mercado."}

@router.get("/market/stocks")
async def fetch_market_stocks():
    """Obtiene acciones del mercado desde la base de datos"""
    data = get_stocks()

    if data:
        return {"stocks": data}

    return {"message": "No se encontraron datos de acciones del mercado."}