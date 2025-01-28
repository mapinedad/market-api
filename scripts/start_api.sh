#!/bin/bash

cd /home/marcos/Documents/market-api/scripts
source /home/marcos/Documents/market-api/.venv/bin/activate
exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001 app.main:app
