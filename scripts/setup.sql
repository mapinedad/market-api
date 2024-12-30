CREATE DATABASE IF NOT EXISTS bcv_market;

USE bcv_market;

CREATE TABLE IF NOT EXISTS market_summary (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operaciones INT NOT NULL,
    titulos_negociados BIGINT NOT NULL,
    monto_efectivo DECIMAL(15,2) NOT NULL,
    hora_24 TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    simbolo VARCHAR(50) NOT NULL,
    ultimo_precio DECIMAL(10,4) NOT NULL,
    monto_efectivo DECIMAL(15,2) NOT NULL,
    variacion DECIMAL(10,4) NOT NULL,
    titulos_negociados BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
