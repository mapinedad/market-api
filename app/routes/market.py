from fastapi import APIRouter
from app.services.scraping import scrape_market_summary, scrape_market_stocks
from app.crud import insert_market_summary, insert_stocks

router = APIRouter()

@router.post("/market/summary")
def store_market_summary():
    data = scrape_market_summary()
    insert_market_summary(data)
    return {"message": "Market summary stored successfully"}

@router.post("/market/stocks")
def store_market_stocks():
    """Obtiene datos del mercado y los inserta en la base de datos."""
    data = scrape_market_stocks()
    if not data:
        return {"message": "No se encontraron datos para insertar."}
    
    try:
        insert_stocks(data)
        return {"message": "Market stocks stored successfully", "records_inserted": len(data)}
    except Exception as e:
        return {"message": f"Error al insertar los datos: {e}"}