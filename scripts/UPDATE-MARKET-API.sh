vi /usr/local/bin/update_market_data.sh

#!/bin/bash

# Registrar el resumen del mercado
curl -X POST http://127.0.0.1:8001/api/v1/market/summary

# Registrar los datos de las acciones
curl -X POST http://127.0.0.1:8001/api/v1/market/stocks

chmod +x /usr/local/bin/update_market_data.sh

vi /etc/systemd/system/market-api-update.service

[Unit]
Description=Market API Data Updater
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/update_market_data.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target

vi /etc/systemd/system/market-api-update.timer

[Unit]
Description=Run Market API Data Updater every minute

[Timer]
OnBootSec=1min
OnUnitActiveSec=1min
Unit=market-api-update.service

[Install]
WantedBy=timers.target

systemctl daemon-reload
systemctl enable market-api-update.timer
systemctl start market-api-update.timer

systemctl list-timers --all | grep market-api-update
journalctl -u market-api-update.service


