# Usar la api para hacer POST hacia la BD:
# Summary:
curl -X POST http://127.0.0.1:8001/api/v1/market/summary && curl -X POST http://127.0.0.1:8001/api/v1/market/summary
# Stocks
curl -X POST http://127.0.0.1:8001/api/v1/market/summary && curl -X POST http://127.0.0.1:8001/api/v1/market/stocks

# automatizar para obtener varios registros:
for i in {1..50}
do 
	curl -X POST http://127.0.0.1:8001/api/v1/market/summary && curl -X POST http://127.0.0.1:8001/api/v1/market/stocks
done


# Usar la api para hacer GET desde la BD:
# Summary:
curl -X GET http://127.0.0.1:8001/api/v1/market/summary && curl -X GET http://127.0.0.1:8001/api/v1/market/summary
# Stocks
curl -X GET http://127.0.0.1:8001/api/v1/market/summary && curl -X GET http://127.0.0.1:8001/api/v1/market/stocks

# automatizar para obtener varios registros:
for i in {1..50}
do 
	curl -X GET http://127.0.0.1:8001/api/v1/market/summary && curl -X GET http://127.0.0.1:8001/api/v1/market/stocks
done

# Ruta de los dos dashboards SUMMARY y STOCKS
http://127.0.0.1:8001/dash