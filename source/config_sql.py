from dotenv import load_dotenv
import os

load_dotenv()

SQL_SERVER_CONFIG = {
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "driver": os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server"),
}
