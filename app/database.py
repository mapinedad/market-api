import mysql.connector
from mysql.connector import pooling

DATABASE_CONFIG = {
    "host": "localhost",
    "user": "mapinedad",
    "password": "RRHHS3n1a72024*-2",
    "database": "bcv_market",
    "charset": "utf8mb4",  # Charset compatible
    "collation": "utf8mb4_general_ci",  # Forzar la collation
}

connection_pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                              pool_size=5,
                                              **DATABASE_CONFIG)

def get_connection():
    return connection_pool.get_connection()
